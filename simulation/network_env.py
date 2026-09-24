import gymnasium as gym
import numpy as np
from gymnasium import spaces
import json
import os
import sys

# Add parent directory to path to import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.pcap_logger import generate_pcap_trace

class NetworkEnv(gym.Env):
    """
    Simulates a 5G Network Link with a Bottleneck Bandwidth and a Buffer Queue.
    """
    def __init__(self, output_dir, name="baseline"):
        super(NetworkEnv, self).__init__()
        
        # Network characteristics
        self.max_bandwidth = 100  # Max packets that can be processed per step
        self.buffer_size = 50     # Size of the queue (Bufferbloat occurs when full)
        
        # State
        self.current_buffer = 0
        self.step_count = 0
        self.max_steps = 200
        
        # Action Space: How many packets to send this step (0 to 200)
        self.action_space = spaces.Box(low=0, high=200, shape=(1,), dtype=np.float32)
        
        # Observation Space: [current_buffer_occupancy, last_dropped_packets]
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(2,), dtype=np.float32)
        
        self.output_dir = output_dir
        self.name = name
        self.telemetry = []

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_buffer = 0
        self.step_count = 0
        self.telemetry = []
        return np.array([0.0, 0.0], dtype=np.float32), {}

    def step(self, action):
        send_rate = int(action[0])
        
        # Simulate network bottleneck processing
        total_in_system = self.current_buffer + send_rate
        processed = min(total_in_system, self.max_bandwidth)
        leftover = total_in_system - processed
        
        # Calculate drops and new buffer size
        dropped = max(0, leftover - self.buffer_size)
        self.current_buffer = min(leftover, self.buffer_size)
        
        # AI Reward Function: 
        # + Reward for processing packets (Throughput)
        # - Heavy Penalty for dropped packets
        # - Small Penalty for filling the buffer (Bufferbloat/Latency)
        reward = processed - (dropped * 10) - (self.current_buffer * 0.5)
        
        # Log data for Blender 3D and Wireshark
        self.telemetry.append({
            "step": self.step_count,
            "sent": send_rate,
            "processed": processed,
            "dropped": dropped,
            "buffer": self.current_buffer,
            "reward": reward
        })
        
        self.step_count += 1
        done = self.step_count >= self.max_steps
        
        if done:
            self._save_telemetry()
            
        return np.array([self.current_buffer, dropped], dtype=np.float32), reward, done, False, {}
        
    def _save_telemetry(self):
        # 1. Save JSON for Blender 3D Animation
        json_path = os.path.join(self.output_dir, f"../blender/{self.name}_telemetry.json")
        with open(json_path, "w") as f:
            json.dump(self.telemetry, f, indent=4)
            
        # 2. Save PCAP for Wireshark
        pcap_path = os.path.join(self.output_dir, f"../pcap/{self.name}_trace.pcap")
        generate_pcap_trace(self.telemetry, pcap_path)

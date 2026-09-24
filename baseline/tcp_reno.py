import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from simulation.network_env import NetworkEnv

def run_tcp_reno():
    print("Starting TCP Reno (Baseline) Simulation...")
    # Initialize environment
    env = NetworkEnv(output_dir=os.path.dirname(__file__), name="tcp_reno")
    obs, _ = env.reset()
    
    cwnd = 10  # Initial Congestion Window
    ssthresh = 64 # Slow start threshold
    
    done = False
    while not done:
        # Reno Logic: Additive Increase, Multiplicative Decrease (AIMD)
        dropped_packets = obs[1]
        
        if dropped_packets > 0:
            # Packet loss detected (Multiplicative Decrease)
            ssthresh = max(cwnd // 2, 1)
            cwnd = ssthresh
        else:
            # No packet loss
            if cwnd < ssthresh:
                cwnd *= 2 # Slow start
            else:
                cwnd += 1 # Congestion avoidance (Additive Increase)
                
        # Take step in environment
        obs, reward, done, _, _ = env.step([cwnd])
        
    print("TCP Reno Simulation Complete! Check /blender for JSON and /pcap for Wireshark files.")

if __name__ == "__main__":
    run_tcp_reno()

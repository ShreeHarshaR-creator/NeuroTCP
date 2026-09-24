import sys
import os
from stable_baselines3 import PPO

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from simulation.network_env import NetworkEnv

def train_neurotcp():
    print("Initializing NeuroTCP Training Environment...")
    env = NetworkEnv(output_dir=os.path.dirname(__file__), name="neuro_tcp")
    
    # Initialize the Reinforcement Learning Agent (PPO - Proximal Policy Optimization)
    model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="../results/tensorboard/")
    
    print("Training AI Agent (This may take a few seconds)...")
    # Train for 10,000 steps (Can be increased for better performance)
    model.learn(total_timesteps=10000)
    
    # Save the trained brain
    model.save("neurotcp_model")
    print("Model saved to neurotcp_model.zip")
    
    # Run a test simulation to generate telemetry/PCAP
    print("Running evaluation simulation with trained AI...")
    obs, _ = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, done, _, _ = env.step(action)
        
    print("NeuroTCP Simulation Complete! Check /blender for JSON and /pcap for Wireshark files.")

if __name__ == "__main__":
    train_neurotcp()

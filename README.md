# NeuroTCP 🧠⚡

Traditional TCP congestion control algorithms (like Reno or Cubic) rely on static, mathematically rigid rules. While effective for early internet infrastructure, they struggle on modern, erratic networks (like 5G, Starlink, or heavy IoT networks), leading to severe **Bufferbloat**—high latency and jitter caused by overflowing network buffers.

**NeuroTCP** replaces these static rules with an Artificial Intelligence agent. By utilizing **Reinforcement Learning (RL)**, NeuroTCP observes real-time network states (Round Trip Time, Packet Loss, Delivery Rate) and dynamically predicts the optimal Congestion Window (`cwnd`) to maximize throughput while keeping latency near zero.

## 🎯 Project Objectives
1. **The Baseline:** Simulate a network environment and implement a standard mathematical congestion control algorithm to demonstrate its drawbacks (Bufferbloat/Packet Loss).
2. **The Environment:** Build a custom `gymnasium` network simulation environment to train the AI.
3. **The Solution:** Train a Reinforcement Learning agent (e.g., PPO/DQN) to manage data flow.
4. **The Benchmark:** Compare NeuroTCP against the baseline protocol, visualizing the improvements in throughput and latency.

## 📂 Repository Structure
*   `/simulation` - The custom OpenAI Gym environment simulating latency, bandwidth, and packet loss.
*   `/agent` - The Reinforcement Learning model architecture and training scripts.
*   `/baseline` - The standard TCP simulation (for performance comparison).
*   `/results` - Benchmark graphs, PCAP files, and performance metrics.

## 🛠️ Technology Stack
*   **Python 3.x**
*   **Gymnasium** (for the RL Environment)
*   **Stable-Baselines3 / PyTorch** (for the RL Agent)
*   **Matplotlib** (for visualizing the performance benchmark)

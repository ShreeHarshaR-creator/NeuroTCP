# NeuroTCP 🧠⚡

Traditional TCP congestion control algorithms (like Reno or Cubic) rely on static, mathematically rigid rules. While effective for early internet infrastructure, they struggle on modern, erratic networks (like 5G, Starlink, or heavy IoT networks), leading to severe **Bufferbloat**—high latency and jitter caused by overflowing network buffers.

**NeuroTCP** replaces these static rules with an Artificial Intelligence agent. By utilizing **Reinforcement Learning (RL)**, NeuroTCP observes real-time network states (Round Trip Time, Packet Loss, Delivery Rate) and dynamically predicts the optimal Congestion Window (`cwnd`) to maximize throughput while keeping latency near zero.

## 🌟 Vision & Architecture
This project features a multi-layered architecture, combining raw packet-level networking, deep reinforcement learning, and a cinematic 3D presentation layer.

1. **The Network Core:** A custom `gymnasium` environment simulates a 5G-equipped Smart City network link.
2. **The AI Agent:** A Reinforcement Learning model (PPO/DQN) that adjusts flow control millisecond-by-millisecond.
3. **Wireshark Deep Packet Inspection:** The simulation generates real `TCP/IP` packet traces (`.pcap`) via Scapy, proving the AI's effectiveness at the lowest OSI layers.
4. **Blender 3D Visualization:** A programmatic Blender integration that takes JSON telemetry from the AI and dynamically animates a 3D Smart City. It visually contrasts the "Traffic Jams" (Bufferbloat) of standard TCP against the smooth, laser-like flow of NeuroTCP.

## 📂 Repository Structure
*   `/simulation` - The OpenAI Gym environment simulating latency, bandwidth, and packet loss.
*   `/agent` - The RL model architecture and training scripts.
*   `/baseline` - The standard TCP Reno simulation (for performance comparison).
*   `/blender` - Python scripts for Blender (`bpy`) to animate the smart city based on telemetry data.
*   `/pcap` - Generated network trace files for Wireshark analysis.
*   `/results` - Benchmark graphs, telemetry JSON, and performance metrics.

## 🛠️ Technology Stack
*   **AI/Simulation:** Python 3.x, Gymnasium, Stable-Baselines3, PyTorch
*   **Networking:** Scapy (PCAP Generation), Wireshark
*   **Visualization:** Blender 3D, Blender Python API (`bpy`), Matplotlib

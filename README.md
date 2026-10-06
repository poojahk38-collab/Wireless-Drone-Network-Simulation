Wireless Drone Network Simulation

Project Description

Wireless Drone Network Simulation is a Python-based simulation that demonstrates communication between multiple drones in a wireless network.

The simulation models drone movement, wireless communication range, packet transmission, packet loss, and dynamic route discovery using an AODV-style routing approach.

Objectives

- To simulate communication between wireless drones.
- To model the movement of drones in a defined area.
- To establish wireless communication based on transmission range.
- To demonstrate packet transmission between a source and destination.
- To implement an AODV-style route discovery mechanism.
- To calculate network performance using Packet Delivery Ratio (PDR).

Technologies Used

- Python
- Matplotlib
- Math
- Random
- Time
- Collections

Simulation Parameters

Parameter| Value
Simulation Area| 500 × 500 meters
Number of Nodes| 5
Transmission Range| 150 meters
Packet Size| 512 bytes
Packet Interval| 0.05 seconds
Traffic Start| 1.0 seconds
Traffic Stop| 4.5 seconds
Simulation Time| 6.0 seconds
Movement Speed| 10.0

Network Nodes

Node| Name| Role
Node 0| DRONE-1| Source / Data-generating node
Node 1| DRONE-2| Wireless forwarding node
Node 2| DRONE-3| Wireless forwarding node
Node 3| DRONE-4| Wireless forwarding node
Node 4| CONTROL-STATION| Destination / Receiving node

Routing

The simulation uses a BFS-based route discovery mechanism to represent AODV-style on-demand routing.

When a packet is generated, the program searches for a path from DRONE-1 to the CONTROL-STATION through available wireless neighbours.

Performance Metric

The simulation calculates Packet Delivery Ratio (PDR) using:

PDR = (Packets Received / Packets Sent) × 100

The program also displays the number of packets sent, received, and lost.

How to Run

1. Install Python

Install Python on your computer.

2. Install Matplotlib

Open a terminal and run:

pip install matplotlib

3. Run the simulation

Navigate to the project directory and run:

python wireless_drone_simulation.py

Output

The program displays the wireless drone network using Matplotlib.

The visualization shows:

- Drone positions
- Control station
- Wireless communication links
- Simulation time
- Dynamic changes in node positions

The terminal displays packet transmission information and final network performance results.

Project Structure

Wireless-Drone-Network-Simulation/
│
├── wireless_drone_simulation.py
└── README.md

Conclusion

This project demonstrates how a wireless drone network can be simulated using Python. It models node movement, wireless connectivity, packet transmission, route discovery, packet loss, and Packet Delivery Ratio.

Author

Your Name

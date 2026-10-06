# ============================================================
# Wireless Drone Network Simulation
# Python Implementation
# ============================================================

import math
import time
import random
from collections import deque

import matplotlib.pyplot as plt


# ============================================================
# Simulation Parameters
# ============================================================

AREA_WIDTH = 500
AREA_HEIGHT = 500

NUMBER_OF_NODES = 5

# Wireless communication range
TRANSMISSION_RANGE = 150.0

# Packet configuration
PACKET_SIZE = 512
PACKET_INTERVAL = 0.05

# Traffic start and stop time
TRAFFIC_START = 1.0
TRAFFIC_STOP = 4.5

# Total simulation time
SIMULATION_TIME = 6.0

# Movement speed
MOVEMENT_SPEED = 10.0


# ============================================================
# Node Information
# ============================================================

nodes = [
    {
        "name": "DRONE-1",
        "x": 50.0,
        "y": 100.0,
        "color": "red"
    },

    {
        "name": "DRONE-2",
        "x": 150.0,
        "y": 200.0,
        "color": "blue"
    },

    {
        "name": "DRONE-3",
        "x": 250.0,
        "y": 100.0,
        "color": "green"
    },

    {
        "name": "DRONE-4",
        "x": 350.0,
        "y": 200.0,
        "color": "yellow"
    },

    {
        "name": "CONTROL-STATION",
        "x": 450.0,
        "y": 100.0,
        "color": "magenta"
    }
]


# ============================================================
# Movement Information
# ============================================================

movements = [
    {
        "node": 0,
        "time": 0.5,
        "x": 150.0,
        "y": 200.0
    },

    {
        "node": 1,
        "time": 1.5,
        "x": 250.0,
        "y": 100.0
    },

    {
        "node": 2,
        "time": 2.5,
        "x": 350.0,
        "y": 200.0
    },

    {
        "node": 3,
        "time": 3.5,
        "x": 450.0,
        "y": 100.0
    }
]


# ============================================================
# Packet Statistics
# ============================================================

packets_sent = 0
packets_received = 0
packets_lost = 0


# ============================================================
# Calculate Distance Between Two Nodes
# ============================================================

def distance(node1, node2):

    dx = node1["x"] - node2["x"]
    dy = node1["y"] - node2["y"]

    return math.sqrt(dx * dx + dy * dy)


# ============================================================
# Find Wireless Neighbours
# ============================================================

def find_neighbors(node_index):

    neighbors = []

    for i in range(NUMBER_OF_NODES):

        if i == node_index:
            continue

        d = distance(nodes[node_index], nodes[i])

        if d <= TRANSMISSION_RANGE:
            neighbors.append(i)

    return neighbors


# ============================================================
# AODV-Style Route Discovery
# ============================================================

def find_route(source, destination):

    """
    Finds a route from source to destination.

    This uses a simple Breadth First Search (BFS)
    to represent on-demand route discovery.
    """

    queue = deque()

    queue.append([source])

    visited = set()

    visited.add(source)

    while queue:

        path = queue.popleft()

        current_node = path[-1]

        # Destination reached
        if current_node == destination:
            return path

        neighbors = find_neighbors(current_node)

        for neighbor in neighbors:

            if neighbor not in visited:

                visited.add(neighbor)

                new_path = path + [neighbor]

                queue.append(new_path)

    # No route available
    return None


# ============================================================
# Move Drones
# ============================================================

def update_movement(current_time):

    for movement in movements:

        node_id = movement["node"]

        movement_time = movement["time"]

        if current_time >= movement_time:

            nodes[node_id]["x"] = movement["x"]
            nodes[node_id]["y"] = movement["y"]


# ============================================================
# Send Packet
# ============================================================

def send_packet():

    global packets_sent
    global packets_received
    global packets_lost

    source = 0
    destination = 4

    packets_sent += 1

    # Discover route using AODV-style routing
    route = find_route(source, destination)

    if route is not None:

        # Packet successfully reaches destination
        packets_received += 1

        print(
            f"Packet {packets_sent}: "
            f"DRONE-1 -> CONTROL-STATION "
            f"Route: {route}"
        )

    else:

        # No route available
        packets_lost += 1

        print(
            f"Packet {packets_sent}: "
            f"Route unavailable - Packet Lost"
        )


# ============================================================
# Display Network
# ============================================================

def draw_network():

    plt.clf()

    # Draw wireless links
    for i in range(NUMBER_OF_NODES):

        for j in range(i + 1, NUMBER_OF_NODES):

            d = distance(nodes[i], nodes[j])

            if d <= TRANSMISSION_RANGE:

                x_values = [
                    nodes[i]["x"],
                    nodes[j]["x"]
                ]

                y_values = [
                    nodes[i]["y"],
                    nodes[j]["y"]
                ]

                plt.plot(
                    x_values,
                    y_values,
                    linestyle="--",
                    linewidth=1
                )

    # Draw nodes
    for i, node in enumerate(nodes):

        plt.scatter(
            node["x"],
            node["y"],
            s=300,
            color=node["color"],
            edgecolors="black"
        )

        plt.text(
            node["x"],
            node["y"] + 15,
            node["name"],
            ha="center",
            fontsize=9,
            fontweight="bold"
        )

    plt.xlim(0, AREA_WIDTH)
    plt.ylim(0, AREA_HEIGHT)

    plt.xlabel("X Position (meters)")
    plt.ylabel("Y Position (meters)")

    plt.title("Wireless Drone Network Simulation")

    plt.grid(True)

    plt.pause(0.01)


# ============================================================
# Main Simulation
# ============================================================

def run_simulation():

    global packets_sent
    global packets_received
    global packets_lost

    print()
    print("=" * 50)
    print("       WIRELESS DRONE NETWORK SIMULATION")
    print("=" * 50)
    print()

    print("Network Area       : 500 x 500 meters")
    print("Number of Nodes    : 5")
    print("Routing Protocol   : AODV-style routing")
    print("Packet Size        :", PACKET_SIZE, "bytes")
    print("Packet Interval    :", PACKET_INTERVAL, "seconds")
    print("Traffic Start      :", TRAFFIC_START, "seconds")
    print("Traffic Stop       :", TRAFFIC_STOP, "seconds")
    print()

    plt.figure(figsize=(9, 7))

    current_time = 0.0

    next_packet_time = TRAFFIC_START

    movement_index = 0

    while current_time <= SIMULATION_TIME:

        # ----------------------------------------------------
        # Update drone positions
        # ----------------------------------------------------

        update_movement(current_time)

        # ----------------------------------------------------
        # Generate packets
        # ----------------------------------------------------

        if (
            current_time >= TRAFFIC_START
            and current_time < TRAFFIC_STOP
            and current_time >= next_packet_time
        ):

            send_packet()

            next_packet_time += PACKET_INTERVAL

        # ----------------------------------------------------
        # Update visualization
        # ----------------------------------------------------

        draw_network()

        # Display simulation time
        plt.text(
            10,
            470,
            f"Simulation Time: {current_time:.2f} s",
            fontsize=11
        )

        # Move simulation forward
        current_time += 0.05

        time.sleep(0.02)

    # ========================================================
    # Calculate Packet Delivery Ratio
    # ========================================================

    if packets_sent > 0:

        pdr = (
            packets_received /
            packets_sent
        ) * 100

    else:

        pdr = 0


    # ========================================================
    # Display Final Results
    # ========================================================

    print()
    print("=" * 50)
    print("       NETWORK PERFORMANCE RESULTS")
    print("=" * 50)

    print(
        f"Packets Sent          : {packets_sent}"
    )

    print(
        f"Packets Received      : {packets_received}"
    )

    print(
        f"Packets Lost          : {packets_lost}"
    )

    print(
        f"Packet Delivery Ratio : {pdr:.2f}%"
    )

    print("=" * 50)

    plt.show()


# ============================================================
# Start Simulation
# ============================================================

if __name__ == "__main__":

    run_simulation()
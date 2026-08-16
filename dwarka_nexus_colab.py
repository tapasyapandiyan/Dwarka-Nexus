# Install Qiskit and plotting tools
!pip install qiskit qiskit-aer matplotlib


import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt

# 1. Defining Archaeological Coordinates (Dwarka Subsea Nodes)
nodes = {
    "Node 0": "Submerged Bastion A (7.0m depth)",
    "Node 1": "Stone Anchor Zone B (8.5m depth)",
    "Node 2": "Foundation Wall C (6.8m depth)",
    "Node 3": "Deep Anomaly D (11.2m depth)"
}

print("=== DWARKA SUBSEA SURVEY NODES ===")
for key, value in nodes.items():
    print(f"{key}: {value}")

# 2. Building Quantum Circuit
qc = QuantumCircuit(4, 4)

# Applying Hadamard gates for superposition (evaluate all nodes simultaneously)
for i in range(4):
    qc.h(i)

# Phase shifts for acoustic signal simulation
qc.cp(np.pi / 2, 0, 1)
qc.cp(np.pi / 4, 1, 2)

# Entangling linked masonry structures (Wall C linked to Bastion A)
qc.cx(0, 2)
qc.cx(1, 3)

# Measuring state
qc.measure(range(4), range(4))

# 3. Executing on Local Quantum Simulator
simulator = Aer.get_backend('qasm_simulator')
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts(qc)

print("\n=== QUANTUM SIMULATION RESULTS (1024 Shots) ===")
for state, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(f"State |{state}> : {count} shots ({(count/1024)*100:.1f}%)")


# Visualizing the Quantum Distribution
plt.figure(figsize=(8, 4))
plt.bar(counts.keys(), counts.values(), color='#1D4ED8')
plt.xlabel("Quantum Grid States (|Node3 Node2 Node1 Node0>)")
plt.ylabel("Measurement Frequency")
plt.title("Dwarka Subsea Grid - Quantum State Probability")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


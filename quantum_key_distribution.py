import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Step 1: Generate random bits and bases for Alice
def generate_key_and_bases(length):
    key = np.random.randint(2, size=length)
    bases = np.random.randint(2, size=length)  # 0 = rectilinear, 1 = diagonal
    return key, bases

# Step 2: Simulate sending qubits
def prepare_qubits(key, bases):
    circuits = []
    for bit, basis in zip(key, bases):
        qc = QuantumCircuit(1, 1)
        if bit == 1:
            qc.x(0)
        if basis == 1:
            qc.h(0)
        circuits.append(qc)
    return circuits

# Step 3: Simulate Bob's measurements
def measure_qubits(circuits, bases):
    simulator = AerSimulator()
    results = []
    for qc, basis in zip(circuits, bases):
        if basis == 1:
            qc.h(0)
        qc.measure(0, 0)
        # Transpile the circuit for the simulator
        transpiled_qc = transpile(qc, simulator)
        # Run the transpiled circuit on the simulator
        result = simulator.run(transpiled_qc, shots=1).result()
        counts = result.get_counts()
        results.append(int(max(counts, key=counts.get)))
    return results

if __name__ == "__main__":
    key_length = 10
    alice_key, alice_bases = generate_key_and_bases(key_length)
    bob_bases = np.random.randint(2, size=key_length)
    circuits = prepare_qubits(alice_key, alice_bases)
    bob_results = measure_qubits(circuits, bob_bases)
    print("Alice's Key:", alice_key)
    print("Bob's Results:", bob_results)

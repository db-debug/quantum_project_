
**Quantum Key Distribution (QKD) Protocol Simulation**

**About the Project**

Quantum Key Distribution (QKD) leverages the principles of quantum mechanics to establish a secure communication channel. This simulation focuses on the BB84 protocol, which uses quantum bits (qubits) to transmit cryptographic keys securely. The project demonstrates how quantum states can be used to detect eavesdropping and ensure secure key exchange.

This project simulates the BB84 Quantum Key Distribution protocol using Qiskit. The BB84 protocol enables two parties, Alice and Bob, to securely share a cryptographic key while detecting any eavesdropping attempts.
## Features:
- **Quantum Circuit**: A custom quantum circuit that simulates a harmonic oscillator using rotations (Rx gates) and entanglement (CX gates).
- **AerSimulator**: The simulation is run on the **AerSimulator** backend of Qiskit, providing accurate and efficient quantum state evolution.
- **Flexible Parameters**: Users can specify the number of qubits, simulation steps, and rotation angle to explore various quantum system configurations.

## Installation:
1. Clone the repository:
   
   git clone git repo
   cd quantum_key_distribution
  

2. Set up a Python environment (optional but recommended):
  
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  

3. Install dependencies:
   
   pip install -r requirements.txt


4. Ensure that Qiskit and the AerSimulator backend are installed:
   
   pip install qiskit
   

## Usage:
To run the quantum harmonic oscillator simulation, execute the following Python script:

python quantum_harmonic_oscillator.py


The simulation will run for the specified number of steps and qubits, and it will display a histogram of the measurement outcomes.


## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


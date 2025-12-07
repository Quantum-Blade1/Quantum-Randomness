# qrng.py - Qiskit 2.x compatible QRNG

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import argparse

def generate_random_bits(n_qubits: int = 8, shots: int = 1):
    qc = QuantumCircuit(n_qubits, n_qubits)

    # Apply Hadamard to all qubits (superposition)
    for q in range(n_qubits):
        qc.h(q)

    qc.measure(range(n_qubits), range(n_qubits))

    # Aer simulator
    backend = Aer.get_backend("aer_simulator")

    # Transpile circuit for backend
    tqc = transpile(qc, backend)

    # Run
    job = backend.run(tqc, shots=shots)
    result = job.result()
    counts = result.get_counts()

    # For QRNG, take the one produced bitstring
    if shots == 1:
        return list(counts.keys())[0]
    else:
        return counts

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QRNG using Qiskit 2.x (Hadamard on each qubit)")
    parser.add_argument('--n', type=int, default=8, help='number of qubits / bits (default 8)')
    parser.add_argument('--shots', type=int, default=1, help='number of circuit runs (default 1)')
    args = parser.parse_args()

    bits = generate_random_bits(n_qubits=args.n, shots=args.shots)
    print("Random bit output:", bits)

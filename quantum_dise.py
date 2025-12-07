from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def quantum_dice_roll():
    qc = QuantumCircuit(3,3)   # 3 qubits, 3 classical bits
    qc.h([0,1,2])              # Put all qubits in superposition
    qc.measure([0,1,2], [0,1,2])

    backend = AerSimulator()
    job = backend.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()
    bitstring = list(counts.keys())[0]
    number = int(bitstring, 2) + 1  # Convert from binary to decimal, range 1–8
    return number

if __name__ == "__main__":
    print("Welcome to Quantum Dice Roll!")
    input("Press Enter to roll the quantum dice...")
    outcome = quantum_dice_roll()
    print(f"Quantum Dice Outcome: {outcome}")

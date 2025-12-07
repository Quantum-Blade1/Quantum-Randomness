from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def quantum_coin_flip():
    qc = QuantumCircuit(1,1)   # 1 qubit, 1 classical bit
    qc.h(0)                     # Hadamard → superposition (50/50)
    qc.measure(0,0)

    backend = AerSimulator()
    job = backend.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()
    return list(counts.keys())[0]

if __name__ == "__main__":
    print("Welcome to Quantum Coin Flip!")
    choice = input("Heads (0) or Tails (1)? ")
    outcome = quantum_coin_flip()
    print(f"Quantum Flip Result: {outcome}")
    if choice == outcome:
        print("You Win! 🎉")
    else:
        print("You Lose 😢")

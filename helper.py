import json
import random
import uuid
from qiskit import assemble
from qiskit.assembler import disassemble
from qiskit.qobj import QasmQobj


## Generate a UUID based unique key
def generate_short_key():
    return str(uuid.uuid4())[:8]  # First 8 characters of a UUID


## Generate random list of n-bit strings of length atmost 4
def generate_random_n_bit_strings(n):
    # Step 1: Generate a random number x less than 4
    if n <= 3:
        x = 1
    else:
        x = random.randint(1, 4)

    # Step 2: Generate x random n-bit binary strings
    n_bit_strings = [format(random.randint(0, 2**n - 1), f"0{n}b") for _ in range(x)]

    return n_bit_strings


## Generate Json objects for storing quantum circuits.
def get_circuit_list_for_json(quantum_circuits):
    circuits = []
    for ckt in quantum_circuits:
        json_str = json.dumps(assemble(ckt).to_dict())
        circuits.append(json_str)
    return circuits


## Generate quantum circuits from Json objects.
def get_quantum_circuit_from_json(json_list):
    circuits = []
    for json_str in json_list:
        qasm_dict = json.loads(json_str)
        ckt, _, __ = disassemble(QasmQobj.from_dict(qasm_dict))
        circuits.append(ckt[0])
    return circuits


## Helper function to calculate accuracy
def calculate_accuracy(counts, target_states):
    target_counts = 0
    if counts:
        total_counts = sum(counts.values())
        target_counts = sum(counts.get(str(state)) for state in target_states)
        accuracy = target_counts / total_counts if total_counts > 0 else 0.0
        return accuracy, total_counts
    return 0.0, 0


## Calculating accuracy for given measurement probabilities and target states
def update_accuracy_shots(df, df_input):
    for idx, row in df.iterrows():
        key = row["key"]
        target_states = df_input[df_input["key"] == key]["target_states"].iloc[0]
        accuracy, shots = calculate_accuracy(row["counts"], target_states)
        df.loc[idx, "accuracy"] = accuracy
        df.loc[idx, 'shots'] = shots
    return

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
    if n<=3:
        x = 1
    else:
        x = random.randint(1, 4)
    
    # Step 2: Generate x random n-bit binary strings
    n_bit_strings = [format(random.randint(0, 2**n - 1), f'0{n}b') for _ in range(x)]
    
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


""" This code is an adaptation of Grover's algorithm implemented by IBM in qiskit tutorials. 
Source - https://learning.quantum.ibm.com/tutorial/grovers-algorithm """

import math
from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator, MCMT, ZGate

# Build a Grover oracle for multiple marked/target states
def grover_oracle(marked_states):
    if not isinstance(marked_states, list):
        marked_states = [marked_states]
    # Compute the number of qubits in circuit
    num_qubits = len(marked_states[0])

    qc = QuantumCircuit(num_qubits)
    # Mark each target state in the input list
    for target in marked_states:
        # Flip target bit-string to match Qiskit bit-ordering
        rev_target = target[::-1]
        # Find the indices of all the '0' elements in bit-string
        zero_inds = [ind for ind in range(num_qubits) if rev_target.startswith("0", ind)]
        # Add a multi-controlled Z-gate with pre- and post-applied X-gates (open-controls) where the target bit-string has a '0' entry
        if len(zero_inds) != 0:
            qc.x(zero_inds)
        qc.compose(MCMT(ZGate(), num_qubits - 1, 1), inplace=True)
        if len(zero_inds) != 0:
            qc.x(zero_inds)
    return qc

# Get the optimal number of iterations 
def get_optimal_iterations(marked_states, grover_op):
    optimal_num_iterations = math.floor(
        math.pi / (4 * math.asin(math.sqrt(len(marked_states) / 2**grover_op.num_qubits)))
    )
    return optimal_num_iterations

# Build the Grover's circuit for given target states
def grover_circuit(target_states):
    oracle = grover_oracle(target_states)
    grover_op = GroverOperator(oracle)
    opt = get_optimal_iterations(target_states, grover_op)
    
    # Full Grover's circuit
    qc = QuantumCircuit(grover_op.num_qubits)
    qc.h(range(grover_op.num_qubits))
    qc.compose(grover_op.power(opt), inplace=True)  # Apply Grover operator the optimal number of times
    qc.measure_all()
    
    return qc

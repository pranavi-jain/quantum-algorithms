import time
from qiskit_braket_provider import BraketLocalBackend, BraketProvider, to_braket


# Run circuits on AWS local simulator (zero noise model)
def aws_local_simulator(key_circuit):
    output = []
    local_simulator = BraketLocalBackend()
    for key, qc in key_circuit:
        start_time = time.time()  # Start Time
        task = local_simulator.run(qc, shots=1024)
        counts = task.result().get_counts()
        end_time = time.time()  # End Time
        exc_time = end_time - start_time
        output.append((key, qc.depth(), counts, exc_time))

    return output


# Run circuits on AWS local simulator (zero noise model)
def aws_online_simulator(key_circuit, simulator):
    output = []
    provider = BraketProvider()
    sv1 = provider.get_backend(simulator)
    sv1_supported_gates = sv1._get_gateset()
    for key, qc in key_circuit:
        braket_circuit = to_braket(qc, basis_gates=sv1_supported_gates)
        start_time = time.time()  # Start Time
        task = sv1.run(qc, shots=1024)
        counts = task.result().get_counts()
        end_time = time.time()  # End Time
        exc_time = end_time - start_time
        output.append((key, braket_circuit.depth, counts, exc_time))

    return output


# Run circuits on AWS linked hardware
def aws_run_task(key_circuit, device, shots):
    output = []
    provider = BraketProvider()
    backend = provider.get_backend(device)
    supported_gates = backend._get_gateset()
    for key, qc in key_circuit:
        braket_circuit = to_braket(qc, basis_gates=supported_gates)
        task = backend.run(qc, shots=shots)
        task_arn = task.job_id()
        output.append((key, braket_circuit.depth, task_arn))

    return output



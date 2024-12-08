import time
from qiskit import transpile
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import Session, SamplerV2 as Sampler


# Run the sampler job locally using AerSimulator without noise.
def aer_without_noise(key_circuit):
    output = []
    aer = AerSimulator()
    pm = generate_preset_pass_manager(backend=aer, optimization_level=1)
    with Session(backend=aer) as session:
        for key, qc in key_circuit:
            isa_qc = pm.run(qc)
            depth = isa_qc.depth()  # Storing depth of transpiled circuit
            start_time = time.time()
            result = Sampler().run([isa_qc]).result()
            counts = result[0].data.meas.get_counts()
            end_time = time.time()
            exc_time = end_time - start_time
            output.append((key, depth, counts, exc_time))

    return output


# Run the sampler job locally using AerSimulator with noise model.
def aer_noisy(key_circuit, backend):
    output = []
    aer_noisy = AerSimulator.from_backend(backend)
    pm = generate_preset_pass_manager(backend=aer_noisy, optimization_level=1)
    with Session(backend=aer_noisy) as session:
        for key, qc in key_circuit:
            isa_qc = pm.run(qc)
            depth = isa_qc.depth()  # Storing depth of transpiled circuit
            start_time = time.time()
            result = Sampler(mode=aer_noisy).run([isa_qc]).result()
            counts = result[0].data.meas.get_counts()
            end_time = time.time()
            exc_time = end_time - start_time
            output.append((key, depth, counts, exc_time))

    return output


# Run jobs on actual IBM device.
def run_backend_job(key_circuit, backend):
    output = []
    with Session(backend=backend):
        for key, qc in key_circuit:
            tqc = transpile(qc, backend)  ## Optional - can skip transpilation
            job = Sampler().run([tqc], shots=1024)
            job_id = job.job_id()
            output.append((key, job_id, tqc.depth()))

    return output

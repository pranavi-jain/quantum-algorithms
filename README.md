# Towards Benchmarking Quantum Computers: Implementing Quantum Algorithms via Qiskit and AWS Braket SDK
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Qiskit](https://img.shields.io/badge/Qiskit-1.3.0-red)
![AWS_Braket](https://img.shields.io/badge/AWS_Braket-1.88.3-red)

**Author:** Pranavi Jain
**Affiliation:** University of Southern California

---

## Table of Contents

- [Overview](#overview)
- [Algorithms Implemented](#quantum-algorithms-implemented)
- [Implementation](#implementation)
- [Results](#results)
- [Future Work](#future-work)

## Overview
This project focuses on understanding the
complexity of benchmarking quantum systems. It aims to provide insights into the challenges and methodologies associated with benchmarking quantum hardware and highlight its importance in the context of noisy intermediate-scale quantum (NISQ) devices.

Currently, this project explores the benchmarking of quantum computers, using various quantum algorithms as a test case. By leveraging available quantum hardware platforms like IBM Quantum, IonQ and IQM via AWS Braket, we analyze their performance concerning computational scalability. 

## Quantum Algorithms Implemented
1.  **Grover's Algorithm** - It is a foundational quantum algorithm designed to solve the unstructured search problem with quadratic speedup. Given an unsorted database of N items, Grover’s algorithm identifies the target element in O(√N) queries, compared to O(N) queries required by classical methods. This efficiency makes it a key benchmark for evaluating quantum systems’ practical capabilities [[1](https://dl.acm.org/doi/pdf/10.1145/237814.237866)], [[2](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE?utm_campaign=shareaholic&utm_medium=copy_link&utm_source=bookmark)].


## Implementation
### Running Grover's circuit on IBM devices, AWS Braket Simulators and AWS Braket linked quantum hardware:
```
# Algorithm: Grover's Algorithm IBM and AWS Braket using qiskit
Inputs: n_max (maximum number of qubits), backends (quantum devices)
Outputs: Performance metrics (transpiled circuit depth, accuracy)

1. Initialize global data structures:
    - param_df to store circuit parameters.
    - output_df to store execution results.

2. Generate target states for qubits 2 to n_max:
    For each qubit number n in [2, n_max]:
        Generate random target states.
        Construct Grover's circuit using Qiskit.
        Store circuit details in param_df.

3. Execute circuits on simulators:
    For each circuit in param_df:
        Run on Qiskit Aer (noiseless and noisy).
        Run on AWS Braket local and state-vector simulators.
        Store execution results in output_df.

4. Execute circuits on quantum hardware:
    For each backend in backends (IBM, IonQ, IQM):
        Submit circuits for execution.
        Record job details and results in output_df.

5. Save results to JSON and CSV files.

6. Analyze results:
    Calculate accuracy metrics for each simulator and backend.
```

## Results
The results from the benchmarking experiments are analyzed to evaluate the performance of quantum simulators and hardware. Key observations include:

1. **Accuracy vs. Number of Qubits**: Shown in Figure 1 below, simulators without noise achieved near-perfect accuracy for all qubit numbers. As the number of qubits increased, noisy simulators and quantum hardware showed a significant drop in accuracy due to error accumulation and limited coherence times.
<img src="/img/accuracy%20vs%20num_qubits.png" alt="Figure 1" width="600"/>

3. **Accuracy vs. Circuit Depth**: Accuracy decreased with increasing circuit depth as shown in Figure 2 below, highlighting the impact of noise and gate errors. In general, quantum hardware with higher Quantum Volume exhibited better accuracy for deeper circuits.
<img src="/img/accuracy%20vs%20circuit_depth.png" alt="Figure 1" width="600"/>

5. **Cross-Platform Performance**: IBM Quantum backends generally outperformed IonQ and IQM in terms of accuracy for larger qubit counts, which was attributed to better noise mitigation and error correction strategies. This can be better noted from Figure 3 below showing the accuracy vs. transpiled circuit depth. The depth of transpiled circuits for superconducting qubits (IBM, IQM) increases faster than for trapped-ion-based devices (IonQ), yet IBM backends exhibit higher accuracy.
<img src="/img/accuracy%20vs%20trans_circuit_depth%20-%20all.png" alt="Figure 1" width="600"/>


## Future Work
1. *Extended Benchmarking* - To include additional quantum algorithms, such as Variational Quantum Eigensolvers (VQE) and Quantum Approximate Optimization Algorithm (QAOA), to evaluate device performance on a broader range of use cases.
2. *Error Correction and Mitigation* - Exploring and implementing advanced error correction and mitigation strategies to note the improvement in accuracy.
3. *Open-Source Benchmarks Suites*: Implementing open-source benchmark suites such as [Supermarq](https://github.com/Infleqtion/client-superstaq/tree/main/supermarq-benchmarks), [Quark](https://github.com/QUARK-framework/QUARK), and [QASMBench](https://github.com/pnnl/QASMBench) to obtain more accurate and practical benchmarking results for comparison.

---

# Nats Playground

A collection of hands-on experiments with [nats.py](https://nats-io.github.io/nats.py/) to explore distributed messaging patterns, scalability, and asynchronous communication.

## Experiments

### 1. Hello World (The Basics)

A foundational script implementing the complete NATS connection workflow based on the official documentation.

- **Key Features:** Remote connection to the `demo.nats.io` server, subscription handling, and basic message publishing.
- **Concepts:** Connection lifecycle, subjects, and byte encoding.

### 2. Native Load Balancer (Queue Groups)

An advanced demonstration of NATS's built-in horizontal scaling capabilities.

- **The Scenario:** Simulating a log processing system where multiple workers share the load to prevent duplicate processing.

- **Implementation:**
    - **Workers:** Three independent processes created using the `multiprocessing` library, all joined in a single Queue Group (`log_workers`).
    - **Publisher:** Dispatches 30 rapid-fire messages to the `logs.process` subject.

- **Key Insight:** Demonstrates how NATS automatically handles load distribution (balanced delivery) between active workers. If one worker fails, the others seamlessly take over the traffic.

## Installation
```bash
pip install nats-py
```

# subnet-automation-tool

# Enterprise Network Subnet Auditing Tool

A modular, fault-tolerant Python utility designed to calculate IPv4 subnet parameters and audit bulk device inventories against target corporate network boundaries. This tool is built following modern NetDevOps standards, decoupling core network execution logic from the user interface layout.

## Key Features
- **Modular Architecture:** Core math engine (`subnet_engine.py`) is completely decoupled from the terminal command-line interface layout (`cli.py`).
- **Defensive Error Handling:** Built-in fault tolerance using structured `try/except` exceptions to safely catch rogue IP assets, network boundary violations, and formatting typos without loop or runtime crashes.
- **Data Sanitization:** Automatically cleanses line streams from bulk files, stripping unexpected whitespaces and skipping empty rows.
- **Persistent Compliance Logging:** Appends timestamped auditing reports directly to a local file vault (`subnet_audit.txt`) for engineering review.

## System Components
- `subnet_engine.py`: Uses the native `ipaddress` library to calculate Network IDs, netmasks, broadcast boundaries, and track host membership.
- `cli.py`: Evaluates user execution inputs using `argparse` flags for single-device verification or bulk-file sweeps.
- `devices.txt`: An external network inventory container holding targeted device IPs.

## Getting Started

### Prerequisites
- Python 3.6 or higher installed.

### Installation
Clone the repository and navigate into the project workspace directory:
```bash
git clone [https://github.com/gulshannarain199/subnet-automation-tool.git](https://github.com/gulshannarain199/subnet-automation-tool.git)
cd subnet-automation-tool
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

![License](https://img.shields.io/badge/License-Educational-green)

# Port Scanner

A modular TCP Port Scanner written in Python.

The purpose of this project is not only to build a working port scanner, but also to understand the networking concepts behind professional security tools such as Nmap.

---

# Project Goal

Develop a modular port scanner in Python that can:

- Scan single hosts
- Scan multiple ports
- Detect open and closed ports
- Perform banner grabbing
- Resolve DNS names
- Detect running services
- Produce clean and readable scan results

The project is designed as a learning journey through networking, Python and cybersecurity.

---

# Technologies

- Python 3
- Ubuntu
- Kali Linux
- Git
- GitHub

---

# Project Structure

```
PortScanner/

│── p_scanner.py          # Main program

│── requirements.txt      # Required Python libraries

│── .gitignore            # Files ignored by Git

│── README.md             # Project documentation

│
├── config/               # Configuration files
├── docs/                 # Documentation
├── logs/                 # Log files
├── scans/                # Saved scan results
├── src/                  # Source code modules
└── tests/                # Unit tests
```

---

# File Description

### p_scanner.py

Main entry point of the application.

### requirements.txt

Contains all Python dependencies required for this project.

### .gitignore

Specifies which files and directories Git should ignore.

### docs/

Contains technical documentation and project notes.

### config/

Stores configuration files.

### logs/

Stores generated log files.

### scans/

Stores scan results.

### src/

Contains the scanner modules and project source code.

### tests/

Contains unit tests and integration tests.

---

# Development Roadmap

## Phase 1 – Basics & Project Structure

- Development environment
- Git & GitHub
- Repository structure
- Project setup

## Phase 2 – Simple TCP Port Scanner

- Socket programming
- Scan single ports
- Detect open and closed ports

## Phase 3 – Multi-Port Scanner

- Loops
- Port ranges
- Improved output

## Phase 4 – Performance

- Multi-threading
- Timeouts
- Performance optimisation

## Phase 5 – Advanced Features

- Banner grabbing
- DNS resolution
- Service detection

## Phase 6 – Professionalisation

- Logging
- Configuration files
- Error handling
- Unit testing
- Documentation

---

# Future Features

- UDP scanning
- OS detection
- IPv6 support
- Export results as JSON
- Export results as CSV
- Command-line arguments
- Progress bar
- Scan statistics

---

# License

This project is created for educational purposes.

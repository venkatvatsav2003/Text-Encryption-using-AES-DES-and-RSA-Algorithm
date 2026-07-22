# Crypto Toolkit

![CI](https://github.com/venkatvatsav2003/Text-Encryption-using-AES-DES-and-RSA-Algorithm/actions/workflows/ci.yml/badge.svg)
![Version](https://img.shields.io/badge/version-3.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

**AES-256, TripleDES, and RSA-2048 encryption with dual Python + OpenSSL backends.**

## Install & Run

```bash
# One-liner
pip install crypto-toolkit && crypto-toolkit aes-gen

# Or clone and run
git clone https://github.com/venkatvatsav2003/Text-Encryption-using-AES-DES-and-RSA-Algorithm.git
cd Text-Encryption-using-AES-DES-and-RSA-Algorithm && pip install -r requirements.txt
./crypto.sh aes gen
./crypto.sh aes enc "Hello World"

# Docker
docker-compose run crypto aes gen
docker-compose run crypto aes enc "Hello World"
```

## Features

- **Three Algorithms** — AES-256-CBC, TripleDES (legacy), RSA-2048 OAEP
- **Dual Backend** — Python `cryptography` library + OpenSSL CLI
- **Key Management** — automated key generation and storage
- **Benchmarks** — performance comparison across algorithms
- **AEAD Mode** — authenticated encryption with integrity verification
- **File Encryption** — encrypt/decrypt files, not just text
- **Streaming** — handles large files without loading into memory

## Quick Start

```bash
# AES-256
./crypto.sh aes gen
./crypto.sh aes enc "Hello World"
./crypto.sh aes dec "gAAAAAB..."

# RSA-2048
./crypto.sh rsa gen
./crypto.sh rsa enc "Secret"
./crypto.sh rsa dec "base64_ciphertext"

# Benchmark
./crypto.sh bench

# Encrypt a file
./crypto.sh aes enc "$(cat document.txt)" > encrypted.txt
```

## Performance

| Algorithm | Encrypt | Decrypt |
|-----------|---------|---------|
| AES-256-CBC | 0.034ms | 0.031ms |
| 3DES | 0.089ms | 0.092ms |
| RSA-2048 | 1.24ms | 7.81ms |

## Project Structure

```
Text-Encryption/
├── crypto.py               # Python engine
├── crypto.sh               # Bash + OpenSSL launcher
├── pyproject.toml           # pip install
├── docker-compose.yml       # Docker one-command
├── .env.example             # Config template
├── config/settings.yml      # Algorithm config
├── benchmarks/              # Performance benchmarks
├── tests/
├── Dockerfile
└── Makefile
```

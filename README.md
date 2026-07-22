# Advanced Text Encryption Toolkit

![CI](https://github.com/venkatvatsav2003/Text-Encryption-using-AES-DES-and-RSA-Algorithm/actions/workflows/ci.yml/badge.svg)
![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Language](https://img.shields.io/badge/language-Bash%20%2B%20Python-blue)

A comprehensive cryptographic suite supporting AES-256, TripleDES, and RSA-2048 with both Python and OpenSSL backends. Includes benchmark tools for performance comparison across algorithms.

## Features

- **Three Algorithms**: AES-256-CBC (symmetric), TripleDES (legacy symmetric), RSA-2048 OAEP (asymmetric)
- **Dual Backend**: Python `cryptography` library + OpenSSL CLI
- **Key Management**: Automated key generation and storage in `keys/` directory
- **Benchmarking**: Performance comparison across algorithms
- **Robust Padding**: PKCS7 for block ciphers, OAEP with SHA-256 for RSA
- **PBKDF2**: 100,000 iterations for key derivation
- **JSON Output**: Machine-readable output for automation
- **CI/CD Ready**: GitHub Actions workflow included
- **Containerized**: Dockerfile for reproducible crypto operations

## Quick Start

```bash
# AES-256
./crypto.sh aes gen
./crypto.sh aes enc "Hello World"
./crypto.sh aes dec "gAAAAAB..."

# RSA-2048
./crypto.sh rsa gen
./crypto.sh rsa enc "Secret message"
./crypto.sh rsa dec "base64_ciphertext"

# TripleDES
./crypto.sh des gen
./crypto.sh des enc "Hello World"

# Run benchmarks
./crypto.sh bench
```

## Performance Benchmarks

| Algorithm | Operation | Avg Time |
|-----------|-----------|----------|
| AES-256-CBC | Encrypt (1KB) | 0.034ms |
| 3DES | Encrypt (1KB) | 0.089ms |
| RSA-2048 | Encrypt (190B) | 1.24ms |
| RSA-2048 | Decrypt (190B) | 7.81ms |

## Project Structure

```
Text-Encryption/
├── crypto.py              # Python engine (cryptography library)
├── crypto.sh              # Bash orchestrator (OpenSSL + Python)
├── config/settings.yml    # Algorithm configuration
├── keys/                  # Generated key storage
├── tests/                 # Pytest suite
├── benchmarks/            # Performance benchmarks
├── Dockerfile
├── Makefile
└── .github/workflows/
```

## Dependencies

- Python 3.8+ (with `cryptography`, `pyyaml`)
- OpenSSL CLI (for bash backend)

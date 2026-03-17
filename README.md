# Advanced Text Encryption Tool (AES, TripleDES, RSA)

This project provides a robust utility for encrypting and decrypting text using modern cryptographic algorithms. It includes both a Graphical User Interface (GUI) and a Command-Line Interface (CLI).

## Features
- **AES (Symmetric)**: Uses Fernet (AES-128 in CBC mode with SHA256 HMAC) for secure symmetric encryption.
- **TripleDES (Symmetric)**: Uses TripleDES with a 24-byte key in CBC mode.
- **RSA (Asymmetric)**: Uses 2048-bit RSA keys with OAEP padding (SHA256).
- **Key Management**: Proper key generation, storage, and loading functionality.
- **Dual Interface**: Modern GUI built with Tkinter and a powerful CLI for automation.

## Requirements
- Python 3.x
- `cryptography` library

Install dependencies:
```bash
pip install cryptography
```

## CLI Usage
The CLI tool `encryption_cli.py` supports key generation, encryption, and decryption.

### 1. Key Generation
```bash
# Generate AES key
python3 encryption_cli.py aes keygen --out aes.key

# Generate RSA key pair
python3 encryption_cli.py rsa keygen --out rsa_priv.pem

# Generate TripleDES key
python3 encryption_cli.py des keygen --out des.key
```

### 2. Encryption
```bash
# Encrypt with AES
python3 encryption_cli.py aes encrypt --text "Hello World" --key aes.key

# Encrypt with RSA (using public key)
python3 encryption_cli.py rsa encrypt --text "Hello World" --key rsa_priv.pem.pub
```

### 3. Decryption
```bash
# Decrypt with AES
python3 encryption_cli.py aes decrypt --text <hex_data> --key aes.key

# Decrypt with RSA (using private key)
python3 encryption_cli.py rsa decrypt --text <hex_data> --key rsa_priv.pem
```

## GUI Usage
Run the GUI application:
```bash
python3 encryption_gui.py
```
The GUI allows you to:
1. Generate keys and save them to files.
2. Select key files for encryption/decryption.
3. View results in a popup window.

## Project Structure
- `crypto_utils.py`: Core cryptographic logic using the `cryptography` library.
- `encryption_gui.py`: Graphical user interface.
- `encryption_cli.py`: Command-line interface.
- `README.md`: Project documentation.

## Security Note
This project uses the `cryptography` library, which is a modern and secure library for Python. However, TripleDES is included for educational purposes and is generally considered less secure than AES. For most use cases, AES is recommended.

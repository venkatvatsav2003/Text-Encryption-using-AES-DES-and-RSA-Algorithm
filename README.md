# Advanced Text Encryption Tool (AES, TripleDES, RSA)

A shell-based cryptographic utility using OpenSSL for symmetric and asymmetric encryption.

## Ideology
Encryption is a fundamental building block of information security. Understanding how different algorithms serve different purposes — symmetric for speed (AES, 3DES), asymmetric for key exchange (RSA) — is essential for designing secure systems.

## Algorithms
| Algorithm | Type | Key Size | Use Case |
|-----------|------|----------|----------|
| AES-256 | Symmetric | 256-bit | General-purpose encryption |
| TripleDES | Symmetric | 192-bit | Legacy system compatibility |
| RSA | Asymmetric | 2048-bit | Key exchange, digital signatures |

## Usage
```bash
chmod +x crypto.sh

# AES
./crypto.sh aes-gen
./crypto.sh aes-enc "Hello World"
./crypto.sh aes-dec "U2FsdGVkX1..."

# TripleDES
./crypto.sh des-gen
./crypto.sh des-enc "Hello World"
./crypto.sh des-dec "base64_ciphertext"

# RSA
./crypto.sh rsa-gen
./crypto.sh rsa-enc "Secret message"
./crypto.sh rsa-dec "base64_ciphertext"
```

## Key Management
Keys are stored in `./keys/` directory:
- `aes.key` — AES-256 key (base64)
- `des.key` — 3DES key (base64)
- `rsa_priv.pem` — RSA private key
- `rsa_pub.pem` — RSA public key

## Security Notes
- Uses PBKDF2 with 100,000 iterations for key derivation
- RSA uses OAEP padding with SHA-256
- 3DES included for educational purposes — AES is recommended for production

## Dependencies
- OpenSSL (`openssl` CLI)
- `base64` (GNU coreutils)

# Crypto Toolkit — Design Document

## Problem Statement
Developers need a simple, auditable encryption toolkit that supports multiple algorithms for different use cases without requiring deep cryptographic expertise.

## Algorithm Selection Rationale

| Algorithm | Type | Use Case | Security Level |
|-----------|------|----------|----------------|
| AES-256 | Symmetric | General encryption | High (recommended) |
| TripleDES | Symmetric | Legacy compatibility | Moderate (deprecated) |
| RSA-2048 | Asymmetric | Key exchange, signatures | High |

## Architecture

```
┌─────────────┐
│  CLI Input  │  crypto.sh or crypto.py
└──────┬──────┘
       ▼
┌─────────────┐
│  Router     │  Routes to algorithm module
└──────┬──────┘
       │
    ┌──┴──┐
    ▼     ▼
┌──────┐ ┌──────┐
│Python│ │OpenSSL│
│Engine│ │Engine │
│      │ │       │
│ crypt│ │openssl│
│ography│ │enc/  │
│      │ │pkeyutl│
└──────┘ └──────┘
    │        │
    └──┬─────┘
       ▼
┌─────────────┐
│   Output    │  stdout, file, JSON
└─────────────┘
```

## Security Considerations
- **Key Isolation**: Keys stored in dedicated `keys/` directory
- **No Hardcoded Keys**: Every key is generated, never shipped
- **Modern Padding**: OAEP with SHA-256 for RSA, PKCS7 for block ciphers
- **Iterations**: 100,000 PBKDF2 rounds for key derivation
- **3DES Warning**: Included for legacy compatibility only — not recommended for new systems

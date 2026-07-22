#!/usr/bin/env bash
set -euo pipefail

echo "=== Cryptography Benchmarks ==="
echo ""

echo "AES-256-CBC Encryption (100 iterations)..."
python3 -c "
import time, os
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
data = os.urandom(1024)
start = time.perf_counter()
for _ in range(100):
    f.encrypt(data)
elapsed = (time.perf_counter() - start) / 100
print(f'  Avg: {elapsed*1000:.3f}ms')
"

echo ""
echo "RSA-2048 Encryption (10 iterations)..."
python3 -c "
import time, os, base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
priv = rsa.generate_private_key(65537, 2048)
pub = priv.public_key()
data = b'Short test data for RSA'
start = time.perf_counter()
for _ in range(10):
    ct = pub.encrypt(data, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
elapsed = (time.perf_counter() - start) / 10
print(f'  Avg: {elapsed*1000:.3f}ms')
"

echo ""
echo "Done."

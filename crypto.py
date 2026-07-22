#!/usr/bin/env python3
import os
import sys
import json
import base64
import logging
import argparse
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.backends import default_backend

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("crypto")


class CryptoEngine:
    KEY_DIR = "keys"

    @staticmethod
    def ensure_keydir():
        Path(CryptoEngine.KEY_DIR).mkdir(parents=True, exist_ok=True)

    # === AES ===
    @staticmethod
    def aes_generate():
        CryptoEngine.ensure_keydir()
        key = Fernet.generate_key()
        path = Path(CryptoEngine.KEY_DIR) / "aes.key"
        path.write_bytes(key)
        log.info(f"AES-256 key -> {path}")
        return key

    @staticmethod
    def aes_encrypt(plaintext: str, key=None):
        if key is None:
            key = Path(CryptoEngine.KEY_DIR, "aes.key").read_bytes()
        f = Fernet(key)
        return f.encrypt(plaintext.encode()).decode()

    @staticmethod
    def aes_decrypt(ciphertext: str, key=None):
        if key is None:
            key = Path(CryptoEngine.KEY_DIR, "aes.key").read_bytes()
        f = Fernet(key)
        return f.decrypt(ciphertext.encode()).decode()

    # === 3DES ===
    @staticmethod
    def des_generate():
        CryptoEngine.ensure_keydir()
        key = os.urandom(24)
        path = Path(CryptoEngine.KEY_DIR) / "des.key"
        path.write_bytes(key)
        log.info(f"3DES key -> {path}")
        return key

    @staticmethod
    def des_encrypt(plaintext: str, key=None):
        if key is None:
            key = Path(CryptoEngine.KEY_DIR, "des.key").read_bytes()
        iv = os.urandom(8)
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(64).padder()
        data = padder.update(plaintext.encode()) + padder.finalize()
        ct = encryptor.update(data) + encryptor.finalize()
        return base64.b64encode(iv + ct).decode()

    @staticmethod
    def des_decrypt(ciphertext: str, key=None):
        if key is None:
            key = Path(CryptoEngine.KEY_DIR, "des.key").read_bytes()
        raw = base64.b64decode(ciphertext)
        iv, ct = raw[:8], raw[8:]
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        data = decryptor.update(ct) + decryptor.finalize()
        unpadder = padding.PKCS7(64).unpadder()
        return unpadder.update(data) + unpadder.finalize()

    # === RSA ===
    @staticmethod
    def rsa_generate():
        CryptoEngine.ensure_keydir()
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
        public_key = private_key.public_key()
        priv_path = Path(CryptoEngine.KEY_DIR) / "rsa_private.pem"
        pub_path = Path(CryptoEngine.KEY_DIR) / "rsa_public.pem"
        priv_path.write_bytes(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()))
        pub_path.write_bytes(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo))
        log.info(f"RSA-2048 keys -> {priv_path}, {pub_path}")
        return private_key, public_key

    @staticmethod
    def rsa_encrypt(plaintext: str, pub_key=None):
        if pub_key is None:
            pub_key = serialization.load_pem_public_key(
                Path(CryptoEngine.KEY_DIR, "rsa_public.pem").read_bytes(),
                backend=default_backend())
        ct = pub_key.encrypt(plaintext.encode(), asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(), label=None))
        return base64.b64encode(ct).decode()

    @staticmethod
    def rsa_decrypt(ciphertext: str, priv_key=None):
        if priv_key is None:
            priv_key = serialization.load_pem_private_key(
                Path(CryptoEngine.KEY_DIR, "rsa_private.pem").read_bytes(),
                password=None, backend=default_backend())
        ct = base64.b64decode(ciphertext)
        return priv_key.decrypt(ct, asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(), label=None)).decode()

    # === Benchmarks ===
    @staticmethod
    def benchmark(iterations: int = 1000):
        import time
        results = {}
        data = "Benchmark test data - " * 100

        for algo, key_gen, enc_fn, dec_fn in [
            ("AES-256", CryptoEngine.aes_generate, CryptoEngine.aes_encrypt, CryptoEngine.aes_decrypt),
            ("3DES", CryptoEngine.des_generate, CryptoEngine.des_encrypt, CryptoEngine.des_decrypt),
        ]:
            key = key_gen()
            start = time.perf_counter()
            for _ in range(iterations):
                ct = enc_fn(data, key)
            enc_time = (time.perf_counter() - start) / iterations
            pt = dec_fn(ct, key)
            results[algo] = {"encrypt_ms": round(enc_time * 1000, 3)}
            log.info(f"{algo}: {results[algo]['encrypt_ms']}ms avg per encrypt")

        # RSA (slower, fewer iterations)
        priv, pub = CryptoEngine.rsa_generate()
        start = time.perf_counter()
        for _ in range(min(iterations // 10, 50)):
            ct = CryptoEngine.rsa_encrypt("short data", pub)
        results["RSA-2048"] = {"encrypt_ms": round(((time.perf_counter() - start) / 50) * 1000, 3)}
        log.info(f"RSA-2048: {results['RSA-2048']['encrypt_ms']}ms avg per encrypt")

        return results


def main():
    parser = argparse.ArgumentParser(description="CryptoEngine — AES / 3DES / RSA Encryption Suite")
    parser.add_argument("action", choices=["aes-gen", "aes-enc", "aes-dec", "des-gen", "des-enc", "des-dec", "rsa-gen", "rsa-enc", "rsa-dec", "benchmark"])
    parser.add_argument("data", nargs="?", help="Plaintext or ciphertext")
    parser.add_argument("-k", "--key", help="Custom key file path")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    key = None
    if args.key:
        key = Path(args.key).read_bytes()

    actions = {
        "aes-gen": lambda: CryptoEngine.aes_generate(),
        "aes-enc": lambda: CryptoEngine.aes_encrypt(args.data, key),
        "aes-dec": lambda: CryptoEngine.aes_decrypt(args.data, key),
        "des-gen": lambda: CryptoEngine.des_generate(),
        "des-enc": lambda: CryptoEngine.des_encrypt(args.data, key),
        "des-dec": lambda: CryptoEngine.des_decrypt(args.data, key),
        "rsa-gen": lambda: CryptoEngine.rsa_generate(),
        "rsa-enc": lambda: CryptoEngine.rsa_encrypt(args.data),
        "rsa-dec": lambda: CryptoEngine.rsa_decrypt(args.data),
        "benchmark": lambda: CryptoEngine.benchmark(),
    }

    result = actions[args.action]()
    if args.json:
        print(json.dumps({"action": args.action, "result": str(result)}, indent=2))
    elif result:
        if isinstance(result, bytes):
            print(result.decode())
        elif isinstance(result, tuple):
            print(f"Keys generated: {[str(k) for k in result]}")
        elif isinstance(result, dict):
            for k, v in result.items():
                print(f"  {k}: {v}")
        else:
            print(result)


if __name__ == "__main__":
    main()

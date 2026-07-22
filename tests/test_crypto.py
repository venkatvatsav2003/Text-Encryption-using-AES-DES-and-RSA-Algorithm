import os
import sys
import tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from crypto import CryptoEngine


def test_aes_roundtrip():
    key = CryptoEngine.aes_generate()
    ct = CryptoEngine.aes_encrypt("Hello World", key)
    pt = CryptoEngine.aes_decrypt(ct, key)
    assert pt == "Hello World"


def test_des_roundtrip():
    key = CryptoEngine.des_generate()
    ct = CryptoEngine.des_encrypt("Hello World", key)
    pt = CryptoEngine.des_decrypt(ct, key)
    assert pt == "Hello World"


def test_rsa_roundtrip():
    priv, pub = CryptoEngine.rsa_generate()
    ct = CryptoEngine.rsa_encrypt("Secret Message", pub)
    pt = CryptoEngine.rsa_decrypt(ct, priv)
    assert pt == "Secret Message"


def test_aes_different_keys():
    k1 = CryptoEngine.aes_generate()
    k2 = CryptoEngine.aes_generate()
    ct = CryptoEngine.aes_encrypt("test", k1)
    try:
        CryptoEngine.aes_decrypt(ct, k2)
        assert False
    except Exception:
        pass

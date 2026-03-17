import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class CryptoUtils:
    @staticmethod
    def generate_aes_key():
        return Fernet.generate_key()

    @staticmethod
    def save_key(key, filename):
        with open(filename, "wb") as key_file:
            key_file.write(key)

    @staticmethod
    def load_key(filename):
        with open(filename, "rb") as key_file:
            return key_file.read()

    @staticmethod
    def encrypt_aes(text, key):
        f = Fernet(key)
        return f.encrypt(text.encode())

    @staticmethod
    def decrypt_aes(encrypted_text, key):
        f = Fernet(key)
        return f.decrypt(encrypted_text).decode()

    @staticmethod
    def generate_rsa_keys():
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def save_rsa_private_key(private_key, filename):
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(filename, "wb") as f:
            f.write(pem)

    @staticmethod
    def save_rsa_public_key(public_key, filename):
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(filename, "wb") as f:
            f.write(pem)

    @staticmethod
    def load_rsa_private_key(filename):
        with open(filename, "rb") as key_file:
            return serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )

    @staticmethod
    def load_rsa_public_key(filename):
        with open(filename, "rb") as key_file:
            return serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )

    @staticmethod
    def encrypt_rsa(text, public_key):
        return public_key.encrypt(
            text.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def decrypt_rsa(encrypted_text, private_key):
        return private_key.decrypt(
            encrypted_text,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

    @staticmethod
    def generate_des_key():
        # DES is 8 bytes. For TripleDES it is 16 or 24 bytes.
        # We use TripleDES from hazmat because it is safer than plain DES.
        return os.urandom(24)

    @staticmethod
    def encrypt_des(text, key):
        iv = os.urandom(8)
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        # Padding is needed for CBC
        pad_len = 8 - (len(text.encode()) % 8)
        padded_text = text.encode() + bytes([pad_len] * pad_len)
        ciphertext = encryptor.update(padded_text) + encryptor.finalize()
        return iv + ciphertext

    @staticmethod
    def decrypt_des(encrypted_data, key):
        iv = encrypted_data[:8]
        ciphertext = encrypted_data[8:]
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_text = decryptor.update(ciphertext) + decryptor.finalize()
        pad_len = padded_text[-1]
        return padded_text[:-pad_len].decode()

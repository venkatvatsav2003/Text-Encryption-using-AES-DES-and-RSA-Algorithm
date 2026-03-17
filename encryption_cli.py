import argparse
import os
from crypto_utils import CryptoUtils

def main():
    parser = argparse.ArgumentParser(description="Advanced Encryption Tool")
    parser.add_argument("algorithm", choices=["aes", "rsa", "des"], help="Encryption algorithm")
    parser.add_argument("action", choices=["encrypt", "decrypt", "keygen"], help="Action to perform")
    parser.add_argument("--text", help="Text to encrypt/decrypt")
    parser.add_argument("--key", help="Path to key file")
    parser.add_argument("--out", help="Path to output file")

    args = parser.parse_args()

    if args.action == "keygen":
        if args.algorithm == "aes":
            key = CryptoUtils.generate_aes_key()
            path = args.out or "aes.key"
            CryptoUtils.save_key(key, path)
            print(f"AES key saved to {path}")
        elif args.algorithm == "rsa":
            priv_path = args.out or "rsa_priv.pem"
            pub_path = (args.out + ".pub") if args.out else "rsa_pub.pem"
            priv, pub = CryptoUtils.generate_rsa_keys()
            CryptoUtils.save_rsa_private_key(priv, priv_path)
            CryptoUtils.save_rsa_public_key(pub, pub_path)
            print(f"RSA keys saved to {priv_path} and {pub_path}")
        elif args.algorithm == "des":
            key = CryptoUtils.generate_des_key()
            path = args.out or "des.key"
            CryptoUtils.save_key(key, path)
            print(f"DES (TripleDES) key saved to {path}")

    elif args.action == "encrypt":
        if not args.text:
            print("Error: --text is required for encryption")
            return
        if not args.key:
            print("Error: --key is required for encryption")
            return
        
        if args.algorithm == "aes":
            key = CryptoUtils.load_key(args.key)
            encrypted = CryptoUtils.encrypt_aes(args.text, key)
            print(f"Encrypted (hex): {encrypted.hex()}")
        elif args.algorithm == "rsa":
            pub_key = CryptoUtils.load_rsa_public_key(args.key)
            encrypted = CryptoUtils.encrypt_rsa(args.text, pub_key)
            print(f"Encrypted (hex): {encrypted.hex()}")
        elif args.algorithm == "des":
            key = CryptoUtils.load_key(args.key)
            encrypted = CryptoUtils.encrypt_des(args.text, key)
            print(f"Encrypted (hex): {encrypted.hex()}")

    elif args.action == "decrypt":
        if not args.text:
            print("Error: --text (hex) is required for decryption")
            return
        if not args.key:
            print("Error: --key is required for decryption")
            return
        
        try:
            encrypted_data = bytes.fromhex(args.text)
            if args.algorithm == "aes":
                key = CryptoUtils.load_key(args.key)
                decrypted = CryptoUtils.decrypt_aes(encrypted_data, key)
                print(f"Decrypted: {decrypted}")
            elif args.algorithm == "rsa":
                priv_key = CryptoUtils.load_rsa_private_key(args.key)
                decrypted = CryptoUtils.decrypt_rsa(encrypted_data, priv_key)
                print(f"Decrypted: {decrypted}")
            elif args.algorithm == "des":
                key = CryptoUtils.load_key(args.key)
                decrypted = CryptoUtils.decrypt_des(encrypted_data, key)
                print(f"Decrypted: {decrypted}")
        except Exception as e:
            print(f"Decryption failed: {e}")

if __name__ == "__main__":
    main()

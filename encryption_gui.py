from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import tkinter as tk
from tkinter import simpledialog, messagebox

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encryption GUI")
        self.root.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter text to encrypt:").pack()
        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.pack()
        
        self.aes_button = tk.Button(self.root, text="Encrypt with AES", command=self.encrypt_aes, bg='lightblue')
        self.aes_button.pack(pady=10)
        
        self.des_button = tk.Button(self.root, text="Encrypt with DES", command=self.encrypt_des, bg='lightgreen')
        self.des_button.pack(pady=10)
        
        self.rsa_button = tk.Button(self.root, text="Encrypt with RSA", command=self.encrypt_rsa, bg='lightcoral')
        self.rsa_button.pack(pady=10)

    def encrypt_aes(self):
        text = self.text_entry.get().encode()
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(text)
        messagebox.showinfo("AES Encryption", f"Ciphertext: {ciphertext.hex()}\nKey: {key.hex()}")

    def encrypt_des(self):
        text = self.text_entry.get().encode()
        key = get_random_bytes(8)
        cipher = DES.new(key, DES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(text)
        messagebox.showinfo("DES Encryption", f"Ciphertext: {ciphertext.hex()}\nKey: {key.hex()}")

    def encrypt_rsa(self):
        text = self.text_entry.get().encode()
        key = RSA.generate(2048)
        public_key = key.publickey()
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext = cipher.encrypt(text)
        messagebox.showinfo("RSA Encryption", f"Ciphertext: {ciphertext.hex()}\nPublic Key: {public_key.export_key().decode()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()


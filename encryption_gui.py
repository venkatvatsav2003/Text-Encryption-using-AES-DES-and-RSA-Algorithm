import tkinter as tk
from tkinter import messagebox, filedialog
from crypto_utils import CryptoUtils

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Encryption GUI")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Encryption Tool", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)

        tk.Label(self.root, text="Text to Encrypt/Decrypt (or Hex for Decryption):", bg="#f0f0f0").pack()
        self.text_entry = tk.Text(self.root, height=5, width=60)
        self.text_entry.pack(pady=5)

        # AES Section
        aes_frame = tk.LabelFrame(self.root, text="AES (Symmetric)", bg="#f0f0f0", padx=10, pady=10)
        aes_frame.pack(fill="x", padx=20, pady=5)
        
        tk.Button(aes_frame, text="Gen Key", command=lambda: self.gen_key("aes"), bg="lightblue").pack(side="left", padx=5)
        tk.Button(aes_frame, text="Encrypt", command=lambda: self.encrypt("aes"), bg="lightblue").pack(side="left", padx=5)
        tk.Button(aes_frame, text="Decrypt", command=lambda: self.decrypt("aes"), bg="lightblue").pack(side="left", padx=5)

        # DES Section
        des_frame = tk.LabelFrame(self.root, text="DES (TripleDES)", bg="#f0f0f0", padx=10, pady=10)
        des_frame.pack(fill="x", padx=20, pady=5)
        
        tk.Button(des_frame, text="Gen Key", command=lambda: self.gen_key("des"), bg="lightgreen").pack(side="left", padx=5)
        tk.Button(des_frame, text="Encrypt", command=lambda: self.encrypt("des"), bg="lightgreen").pack(side="left", padx=5)
        tk.Button(des_frame, text="Decrypt", command=lambda: self.decrypt("des"), bg="lightgreen").pack(side="left", padx=5)

        # RSA Section
        rsa_frame = tk.LabelFrame(self.root, text="RSA (Asymmetric)", bg="#f0f0f0", padx=10, pady=10)
        rsa_frame.pack(fill="x", padx=20, pady=5)
        
        tk.Button(rsa_frame, text="Gen Keys", command=lambda: self.gen_key("rsa"), bg="lightcoral").pack(side="left", padx=5)
        tk.Button(rsa_frame, text="Encrypt (Pub)", command=lambda: self.encrypt("rsa"), bg="lightcoral").pack(side="left", padx=5)
        tk.Button(rsa_frame, text="Decrypt (Priv)", command=lambda: self.decrypt("rsa"), bg="lightcoral").pack(side="left", padx=5)

    def gen_key(self, algo):
        if algo == "aes":
            key = CryptoUtils.generate_aes_key()
            filename = filedialog.asksaveasfilename(defaultextension=".key", title="Save AES Key")
            if filename:
                CryptoUtils.save_key(key, filename)
                messagebox.showinfo("Success", f"AES key saved to {filename}")
        elif algo == "des":
            key = CryptoUtils.generate_des_key()
            filename = filedialog.asksaveasfilename(defaultextension=".key", title="Save DES Key")
            if filename:
                CryptoUtils.save_key(key, filename)
                messagebox.showinfo("Success", f"DES key saved to {filename}")
        elif algo == "rsa":
            priv, pub = CryptoUtils.generate_rsa_keys()
            priv_file = filedialog.asksaveasfilename(defaultextension=".pem", title="Save RSA Private Key")
            if priv_file:
                CryptoUtils.save_rsa_private_key(priv, priv_file)
                pub_file = priv_file + ".pub"
                CryptoUtils.save_rsa_public_key(pub, pub_file)
                messagebox.showinfo("Success", f"RSA keys saved:\n{priv_file}\n{pub_file}")

    def encrypt(self, algo):
        text = self.text_entry.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Enter text to encrypt")
            return

        key_file = filedialog.askopenfilename(title=f"Select Key for {algo.upper()}")
        if not key_file:
            return

        try:
            if algo == "aes":
                key = CryptoUtils.load_key(key_file)
                result = CryptoUtils.encrypt_aes(text, key)
            elif algo == "des":
                key = CryptoUtils.load_key(key_file)
                result = CryptoUtils.encrypt_des(text, key)
            elif algo == "rsa":
                pub_key = CryptoUtils.load_rsa_public_key(key_file)
                result = CryptoUtils.encrypt_rsa(text, pub_key)
            
            self.display_result("Encrypted (Hex)", result.hex())
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self, algo):
        hex_data = self.text_entry.get("1.0", tk.END).strip()
        if not hex_data:
            messagebox.showwarning("Warning", "Enter hex data to decrypt")
            return

        key_file = filedialog.askopenfilename(title=f"Select Key for {algo.upper()}")
        if not key_file:
            return

        try:
            encrypted_data = bytes.fromhex(hex_data)
            if algo == "aes":
                key = CryptoUtils.load_key(key_file)
                result = CryptoUtils.decrypt_aes(encrypted_data, key)
            elif algo == "des":
                key = CryptoUtils.load_key(key_file)
                result = CryptoUtils.decrypt_des(encrypted_data, key)
            elif algo == "rsa":
                priv_key = CryptoUtils.load_rsa_private_key(key_file)
                result = CryptoUtils.decrypt_rsa(encrypted_data, priv_key)
            
            self.display_result("Decrypted Text", result)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def display_result(self, title, content):
        result_win = tk.Toplevel(self.root)
        result_win.title(title)
        tk.Label(result_win, text=title).pack()
        text_area = tk.Text(result_win, height=10, width=50)
        text_area.insert(tk.END, content)
        text_area.pack(padx=10, pady=10)
        tk.Button(result_win, text="Close", command=result_win.destroy).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()

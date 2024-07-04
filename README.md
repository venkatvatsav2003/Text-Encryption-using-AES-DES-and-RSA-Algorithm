# Text-Encryption-using-AES-DES-and-RSA-Algorithm


### Detailed Information on Encryption GUI Project

#### Overview
The Encryption GUI project aims to create a utility that encrypts text using different encryption algorithms (AES, DES, RSA) and displays the encrypted text and keys in a user-friendly graphical user interface (GUI). This project is built using Python's Tkinter library for the GUI and the PyCryptodome library for the cryptographic functions.

#### Objectives
1. **Encrypt Text**: Allow users to encrypt input text using AES, DES, and RSA encryption algorithms.
2. **Display Encrypted Data**: Show the encrypted text and the corresponding keys in the GUI.
3. **User-Friendly Interface**: Create an intuitive and colorful interface for users to interact with.

#### Project Structure
1. **Setup Python Environment**: Ensure all necessary packages are installed.
2. **Encryption Logic**: Develop the backend logic to encrypt text using AES, DES, and RSA.
3. **Design the GUI**: Use Tkinter to design the user interface.
4. **Integration**: Connect the backend logic with the GUI.
5. **Enhancement**: Add colorful and user-friendly elements.
6. **Testing**: Thoroughly test the application to ensure it works as expected.

### Detailed Steps

#### 1. Setup Python Environment
Ensure you have Python, Tkinter, and PyCryptodome installed on your system:

- **Python Installation**: Make sure Python3 is installed on your system. You can install it using `sudo apt install python3`.
- **Pip Installation**: Ensure pip (Python package installer) is installed using `sudo apt install python3-pip`.
- **Tkinter Installation**: Install Tkinter using `sudo apt install python3-tk`.
- **PyCryptodome Installation**: Install PyCryptodome using `pip3 install pycryptodome`.

#### 2. Encryption Logic
Develop the backend logic to encrypt text using AES, DES, and RSA:

- **AES Encryption**: Uses a 16-byte key and the EAX mode for authenticated encryption.
- **DES Encryption**: Uses an 8-byte key and the EAX mode for authenticated encryption.
- **RSA Encryption**: Generates a 2048-bit RSA key pair and uses PKCS1_OAEP for encryption.

#### 3. Design the GUI using Tkinter
Design a user-friendly GUI with Tkinter:

- **Main Window**: Create the main application window with a title and size.
- **Text Entry**: Add an entry widget for users to input their text.
- **Encrypt Buttons**: Add buttons for each encryption algorithm (AES, DES, RSA).
- **Message Box**: Display the encrypted text and keys in a message box.

#### 4. Integrate Logic with GUI
Connect the backend logic with the GUI:

- **Button Click Event**: When the user clicks an encryption button, the input text is encrypted using the corresponding algorithm.
- **Display Results**: Show the encrypted text and keys in a message box.

#### 5. Add Colorful and User-friendly Elements
Enhance the user experience by adding colors and fonts:

- **Background Colors**: Use light colors for the encryption buttons to differentiate between them (e.g., light blue for AES, light green for DES, light coral for RSA).
- **Fonts**: Use a readable font like Arial with varying sizes for different elements to improve readability and aesthetics.

#### 6. Testing the Application
Thoroughly test the application to ensure it works as expected:

- **Run the Application**: Execute the Python script to launch the application.
- **Test Various Inputs**: Enter various texts to check if the encryption is accurate and the results are displayed correctly.
- **User Feedback**: Gather feedback from users to improve the application.

### Additional Features (Optional)
1. **Save Encrypted Data**: Allow users to save the encrypted text and keys to a file.
2. **Decrypt Functionality**: Add functionality to decrypt the encrypted text using the provided keys.
3. **Customization**: Allow users to customize the encryption settings (e.g., key size, encryption mode).
4. **Advanced Encryption Options**: Provide additional encryption algorithms and modes for users to choose from.

### Conclusion
This project provides a comprehensive introduction to encryption and GUI development with Python, helping users understand the basics of cryptography and how to implement it in a user-friendly application. By following these detailed steps, you can develop a functional and user-friendly encryption GUI that enhances security awareness and provides practical encryption tools.

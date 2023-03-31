import tkinter as tk
from tkinter import messagebox
from morse import MorseCode


class MorseCodeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Morse Code Converter")

        # Create label and entry for text input
        input_label = tk.Label(self.window, text="Enter text:")
        input_label.grid(row=0, column=0, padx=10, pady=10)
        self.input_entry = tk.Entry(self.window, width=50)
        self.input_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create label and entry for morse code output
        output_label = tk.Label(self.window, text="Morse code:")
        output_label.grid(row=1, column=0, padx=10, pady=10)
        self.output_entry = tk.Entry(self.window, width=50, state='readonly')
        self.output_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create encrypt button
        encrypt_button = tk.Button(self.window, text="Encrypt", command=self.encrypt)
        encrypt_button.grid(row=2, column=0, padx=10, pady=10)

        # Create decrypt button
        decrypt_button = tk.Button(self.window, text="Decrypt", command=self.decrypt)
        decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky="E")

        # Run the main loop
        self.window.mainloop()

    def encrypt(self):
        """Encrypts text to Morse Code and displays in output entry"""
        text = self.input_entry.get()
        morse_code = MorseCode(text).encrypt()
        self.output_entry.configure(state='normal')
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, morse_code)
        self.output_entry.configure(state='readonly')

    def decrypt(self):
        """Decrypts Morse Code to text and displays in output entry"""
        morse_code = self.input_entry.get()
        try:
            text = MorseCode(morse_code).decrypt()
            self.output_entry.configure(state='normal')
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, text)
            self.output_entry.configure(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Invalid Morse code")

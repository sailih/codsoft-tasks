import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")

        # Create labels and entries
        tk.Label(self.window, text="Password Length:").grid(row=0, column=0)
        self.length_entry = tk.Entry(self.window)
        self.length_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Include Uppercase Letters:").grid(row=1, column=0)
        self.uppercase_var = tk.BooleanVar()
        tk.Checkbutton(self.window, variable=self.uppercase_var).grid(row=1, column=1)

        tk.Label(self.window, text="Include Numbers:").grid(row=2, column=0)
        self.numbers_var = tk.BooleanVar()
        tk.Checkbutton(self.window, variable=self.numbers_var).grid(row=2, column=1)

        tk.Label(self.window, text="Include Special Characters:").grid(row=3, column=0)
        self.special_var = tk.BooleanVar()
        tk.Checkbutton(self.window, variable=self.special_var).grid(row=3, column=1)

        # Create generate password button
        tk.Button(self.window, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2)

        # Create password label
        self.password_label = tk.Label(self.window, text="")
        self.password_label.grid(row=5, column=0, columnspan=2)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                messagebox.showerror("Error", "Password length must be at least 8 characters.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid password length.")
            return

        characters = string.ascii_lowercase
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.numbers_var.get():
            characters += string.digits
        if self.special_var.get():
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text="Generated Password: " + password)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()
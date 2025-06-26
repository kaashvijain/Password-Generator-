import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_set = ''
    if use_upper:
        character_set += string.ascii_uppercase
    if use_lower:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def generate_multiple_passwords(count, length, use_upper, use_lower, use_digits, use_symbols):
    return [generate_password(length, use_upper, use_lower, use_digits, use_symbols) for _ in range(count)]

def generate():
    try:
        length = int(length_entry.get())
        count = int(count_entry.get())
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        passwords = generate_multiple_passwords(count, length, use_upper, use_lower, use_digits, use_symbols)
        result_text.delete(1.0, tk.END)  # Clear previous results
        for pwd in passwords:
            result_text.insert(tk.END, pwd + '\n')
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Password Generator")

#labels
tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

tk.Label(root, text="Number of Passwords:").grid(row=1, column=0)
count_entry = tk.Entry(root)
count_entry.grid(row=1, column=1)

#checkboxes
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).grid(row=2, columnspan=2)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).grid(row=3, columnspan=2)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=4, columnspan=2)
tk.Checkbutton(root, text="Include Special Characters", variable=symbols_var).grid(row=5, columnspan=2)

#button
generate_button = tk.Button(root, text="Generate Passwords", command=generate)
generate_button.grid(row=6, columnspan=2)

#results
result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=7, columnspan=2)

root.mainloop()

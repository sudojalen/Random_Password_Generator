import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 8:
            result_label.config(text="Password must be at least 8 characters.", fg="red")
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        result_label.config(text=password, fg="green")
        copy_btn.config(state=tk.NORMAL)
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg="red")
        copy_btn.config(state=tk.DISABLED)

def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        window.update()
        copy_btn.config(text="Copied!", fg="blue")
        window.after(1500, lambda: copy_btn.config(text="Copy to Clipboard", fg="black"))

# Create the main window
window = tk.Tk()
window.title("🔐 Password Generator")
window.geometry("400x240")
window.resizable(False, False)

# Title
title_label = tk.Label(window, text="Random Password Generator", font=("Helvetica", 14))
title_label.pack(pady=10)

# Prompt label
prompt_label = tk.Label(window, text="Enter desired password length:")
prompt_label.pack()

# Entry
entry_length = tk.Entry(window, width=10, justify='center')
entry_length.pack()
entry_length.insert(0, "12")

# Generate button
generate_btn = tk.Button(window, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

# Result
result_label = tk.Label(window, text="", font=("Courier", 12), wraplength=380)
result_label.pack(pady=5)

# Copy button
copy_btn = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_btn.pack()

# Run
window.mainloop()

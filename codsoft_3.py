import tkinter as tk
import random
import string

def generate_password():
    user_name = user_name_entry.get()
    password_length = int(length_entry.get())

    if password_length < 8:
        password_output.config(text="Password length should be at least 8 characters")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        password_output.config(text=generated_password)

def reset_password():
    user_name_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_output.config(text="")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set the window size and position
window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and place widgets
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

user_name_label = tk.Label(root, text="User Name:")
user_name_label.pack()

user_name_entry = tk.Entry(root)
user_name_entry.pack()

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_output = tk.Label(root, text="", wraplength=250, justify="center", font=("Courier", 12))
password_output.pack(pady=20)

accept_button = tk.Button(root, text="Accept", command=root.quit)
accept_button.pack(side="left", padx=10)

reset_button = tk.Button(root, text="Reset", command=reset_password)
reset_button.pack(side="right", padx=10)

# Start the GUI event loop
root.mainloop()

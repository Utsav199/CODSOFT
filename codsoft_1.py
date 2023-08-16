import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

def clear_all():
    listbox.delete(0, tk.END)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("TO-DO List App")
root.geometry("400x400")

# Create listbox to display tasks
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=20)

# Create entry field to input new tasks
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create buttons for adding, removing, and clearing tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(root, text="Clear All", command=clear_all)
clear_button.pack(side=tk.LEFT, padx=10)

# Close the window gracefully
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the main event loop
root.mainloop()

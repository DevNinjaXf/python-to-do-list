import tkinter as tk
from tkinter import messagebox

# Add task
def add_task():
    task = entry.get()
    if task.strip():
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Delete task 
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Hover effects
def on_enter(e):
    e.widget['background'] = '#ff6b81'

def on_leave(e):
    e.widget['background'] = '#ff4757'

# main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("340x500")
root.config(bg="#f1f2f6") 

# Header
navbar = tk.Frame(root, bg="#3742fa", height=60)
navbar.pack(fill="x")

title_label = tk.Label(navbar, text="📋 To-Do List", font=("Arial", 16, "bold"), bg="#3742fa", fg="white")
title_label.pack(pady=10)

# Entry widget 
entry = tk.Entry(root, width=25, font=("Arial", 12), bg="#dff9fb", fg="#130f40", 
                 relief="solid", bd=2, justify="center", highlightthickness=2, highlightbackground="#3742fa")
entry.pack(pady=15, ipady=5)

# Add Button
add_button = tk.Button(root, text="➕ Add Task", font=("Arial", 10, "bold"), bg="#ff4757", fg="white", relief="flat", command=add_task)
add_button.pack(pady=5, ipadx=10, ipady=5)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

# Delete Button
delete_button = tk.Button(root, text="🗑 Delete Task", font=("Arial", 10, "bold"), bg="#ff4757", fg="white", relief="flat", command=delete_task)
delete_button.pack(pady=5, ipadx=10, ipady=5)
delete_button.bind("<Enter>", on_enter)
delete_button.bind("<Leave>", on_leave)

# Listbox
listbox = tk.Listbox(root, width=25, height=15, font=("Arial", 11), bg="#ced6e0", fg="#2f3542", 
                     selectbackground="#3742fa", selectforeground="white", relief="flat", justify="center")
listbox.pack(pady=15)

#  Tkinter loop
root.mainloop()

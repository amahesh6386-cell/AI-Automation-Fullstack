import tkinter as tk
from tkinter import messagebox

def submit_data():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    qualification = qualification_entry.get()
    skills = skills_entry.get()
    address = address_text.get("1.0", tk.END)

    result = f"""
----- BIO DATA -----
Name: {name}
Age: {age}
Gender: {gender}
Qualification: {qualification}
Skills: {skills}
Address: {address}
----------------------
"""
    messagebox.showinfo("Bio Data Submitted", result)

# Create main window
root = tk.Tk()
root.title("Bio Data Form")
root.geometry("400x500")

# Labels and Input Fields
tk.Label(root, text="Bio Data Form", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root, width=40)
age_entry.pack()

tk.Label(root, text="Gender:").pack()
gender_entry_

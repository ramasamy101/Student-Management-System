
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Management System")
root.geometry("400x400")

students = []

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Mark").pack()
mark_entry = tk.Entry(root)
mark_entry.pack()

text_area = tk.Text(root, height=10)
text_area.pack()

def add_student():
    name = name_entry.get()
    mark = mark_entry.get()
    
    if name == "" or mark == "":
        messagebox.showwarning("Error", "Fill all fields")
        return
    
    students.append({"name": name, "mark": mark})
    messagebox.showinfo("Success", "Student Added")
    
    name_entry.delete(0, tk.END)
    mark_entry.delete(0, tk.END)

def view_students():
    text_area.delete("1.0", tk.END)
    
    for s in students:
        text_area.insert(tk.END, f"{s['name']} - {s['mark']}\n")

def delete_student():
    name = name_entry.get()
    
    for s in students:
        if s["name"] == name:
            students.remove(s)
            messagebox.showinfo("Deleted", "Student Deleted")
            return
    
    messagebox.showerror("Error", "Student not found")

tk.Button(root, text="Add", command=add_student).pack()
tk.Button(root, text="View", command=view_students).pack()
tk.Button(root, text="Delete", command=delete_student).pack()

root.mainloop()

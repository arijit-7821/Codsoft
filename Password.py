import tkinter as tk
from tkinter import messagebox
import string
import secrets

def generate_password():
    password_length = int(length_entry.get())
    
    if password_length <= 0:
        messagebox.showerror("Invalid Length", "Password length must be greater than 0.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(secrets.choice(characters) for _ in range(password_length))
    
    password_result.set(generated_password)
#change background colour
def change_background_color():
    try:
        color = color_entry.get()
        app.config(bg=color)
    except:
        tk.messagebox.showinfo("Invalid Syntax","Please enter a valid colour name")

# Create  window
app = tk.Tk()
app.title("Password Generator")
app.geometry("370x370")
app.resizable(False,False)
# Create widgets
Name_label = tk.Label(app, text="Name")
Name_label.pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)
Adress_label = tk.Label(app, text="Adress:")
Adress_label.pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)
length_label = tk.Label(app, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)

# colour
color_label = tk.Label(app, text="Enter Background Color:")
color_label.pack(pady=5)
color_entry = tk.Entry(app)
color_entry.pack(pady=5)

change_button = tk.Button(app, text="Change Color", command=change_background_color)
change_button.pack(pady=10)
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_result = tk.StringVar()
password_result_label = tk.Label(app, textvariable=password_result)
password_result_label.pack(pady=5)

app.mainloop()

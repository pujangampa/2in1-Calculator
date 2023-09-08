import tkinter as tk
import subprocess

# Function to handle Button 1 click event
# Function to launch project 1
def launch_project1():
    subprocess.call(["python", r"C:\Users\owner\OneDrive\Desktop\PY Projects\2 in 1 Calci\Calculator\Calci.py"])

# Function to launch project 2
def launch_project2():
    subprocess.call(["python", r"C:\Users\owner\OneDrive\Desktop\PY Projects\2 in 1 Calci\Conv\conv.py"])

# Create the home page window
root = tk.Tk()
root.title("Home Page")

# Set the background color
root.configure(bg='Black')
root.geometry("300x300")
root.resizable(0,0)

# Create the title label
title_label = tk.Label(root, text="Hello Geeks!", height=1, width=10, padx=10,pady=5,font=('verdana',20,'bold'), bg="#FDF6E3", fg="Black")
title_label.pack(pady=50)

title_label = tk.Label(root, text="Projects By Pujan Gampa", height=1, width=50, padx=5,pady=10,font=('verdana',10,'bold'), bg="#FDF6E3", fg="Black")
title_label.pack(pady=60)

button_frame = tk.Frame(root, bg="Black")
button_frame.pack(pady=100)

# Create Button 1
button1 = tk.Button(button_frame, text="CALCULATOR",  font=("verdana bold", 8), bd=2, bg='#00a65a', fg="white", padx=20, pady=10, command=launch_project1)
button1.pack(side=tk.LEFT, padx=10)

# Create Button 2
button2 = tk.Button(button_frame, text="CONVERTER", font=("verdana bold", 8), bd=2,bg='#00a65a', fg="white", padx=20, pady=10, command=launch_project2)
button2.pack(side=tk.LEFT, padx=10)

# Center the button frame horizontally
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# Start the tkinter event loop
root.mainloop()

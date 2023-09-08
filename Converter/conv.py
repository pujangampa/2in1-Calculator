import tkinter as tk

def convert_number():
    number = int(entry.get())
    if var.get() == 1:
        result = bin(number)[2:]  # Remove '0b' prefix
    else:
        result = str(int(str(number), 2))

    result_entry.delete(0, tk.END)
    result_entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Converter")
window.geometry('300x200')
window.configure(background='Black')
window.resizable(0,0)

# Create and pack the number entry widget
label = tk.Label(window, text="Enter a number:")
label.grid(row=0, column=0, padx=15, pady=10)
entry = tk.Entry(window)
entry.grid(row=0, column=1)

# Create and pack the conversion type radio buttons in one row
var = tk.IntVar()
var.set(1)  # Default to Decimal to Binary
decimal_to_binary_radio = tk.Radiobutton(window, text="Decimal to Binary", variable=var, value=1)
decimal_to_binary_radio.grid(row=1, column=0, padx=15, pady=5)
binary_to_decimal_radio = tk.Radiobutton(window, text="Binary to Decimal", variable=var, value=2)
binary_to_decimal_radio.grid(row=1, column=1)

# Create and pack the convert button
button = tk.Button(window, text="Convert", command=convert_number)
button.grid(row=2, columnspan=2, pady=10)

# Create and pack the result entry widget
result_entry = tk.Entry(window)
result_entry.grid(row=3, columnspan=2, pady=10)

# Start the main event loop
window.mainloop()

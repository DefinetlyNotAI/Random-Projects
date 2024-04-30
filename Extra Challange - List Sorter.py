import tkinter as tk
from tkinter import messagebox

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def sort_inputs():
    inputs = input_entry.get("1.0", "end-1c").split("\n")
    if inputs[-1] == "":
        inputs.pop()
    order = order_var.get()
    if order == "Numeric":
        numeric_inputs = [x for x in inputs if x.isdigit()]
        if len(numeric_inputs) == len(inputs):
            inputs = list(map(int, inputs))
            bubble_sort(inputs)
            output_text.delete("1.0", "end")
            output_text.insert("end", "Sorted inputs: " + str(inputs))
        else:
            messagebox.showerror("Error", "Some of the inputs are not numeric.")
    elif order == "Alphabetic":
        bubble_sort(inputs)
        output_text.delete("1.0", "end")
        output_text.insert("end", "Sorted inputs: " + str(inputs))
    else:
        messagebox.showerror("Error", "Invalid choice. Please select 'Numeric' or 'Alphabetic'.")

root = tk.Tk()
root.title("Input Sorter")

input_label = tk.Label(root, text="Enter values:")
input_label.pack()

input_entry = tk.Text(root, height=4, width=30)
input_entry.pack()

order_label = tk.Label(root, text="Sort order:")
order_label.pack()

order_var = tk.StringVar(root)
order_var.set("Numeric")
order_option = tk.OptionMenu(root, order_var, "Numeric", "Alphabetic")
order_option.pack()

sort_button = tk.Button(root, text="Sort", command=sort_inputs)
sort_button.pack()

output_label = tk.Label(root, text="Output:")
output_label.pack()

output_text = tk.Text(root, height=4, width=30)
output_text.pack()

root.mainloop()
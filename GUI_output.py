import tkinter as tk
from tkinter import filedialog, messagebox

def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return

    try:
        with open(filepath, "r") as file:
            numbers = [int(line.strip()) for line in file]

        numbers.sort()
        avg = sum(numbers) / len(numbers)
        max_num = max(numbers)

        output.delete("1.0", tk.END)
        output.insert(tk.END, "Sorted numbers:\n")
        for n in numbers:
            output.insert(tk.END, f"{n}\n")

        output.insert(tk.END, f"\nAverage: {avg}\n")
        output.insert(tk.END, f"Maximum: {max_num}\n")
    except ValueError:
        messagebox.showerror("Error", "File contains non-numeric lines!")

# GUI
root = tk.Tk()
root.title("Number Processing")

label = tk.Label(root, text="Select output.txt to process:")
label.pack(pady=10)

button = tk.Button(root, text="Load file", command=load_file)
button.pack(pady=5)

output = tk.Text(root, width=40, height=15)
output.pack(padx=10, pady=10)

root.mainloop()

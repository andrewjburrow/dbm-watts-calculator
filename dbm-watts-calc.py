import tkinter as tk
import math

def dbm_to_watts(dbm):
    return 10 ** ((dbm - 30) / 10)

def watts_to_dbm(watts):
    return 10 * math.log10(watts) + 30

def convert():
    try:
        value = float(entry.get())
        if mode.get() == "dbm":
            result = dbm_to_watts(value)
            output_label.config(text=f"{result:.8f} W")
        else:
            result = watts_to_dbm(value)
            output_label.config(text=f"{result:.2f} dBm")
    except:
        output_label.config(text="Invalid input")

def main():
    global entry, output_label, mode

    root = tk.Tk()
    root.title("dBm / Watts Converter")
    root.geometry("300x200")

    mode = tk.StringVar(value="dbm")  # default mode

    tk.Label(root, text="Enter value:", font=("Arial", 12)).pack()
    entry = tk.Entry(root, font=("Arial", 16))
    entry.pack(pady=5)

    # Radio buttons to switch modes
    tk.Radiobutton(root, text="dBm ➜ Watts", variable=mode, value="dbm").pack()
    tk.Radiobutton(root, text="Watts ➜ dBm", variable=mode, value="watts").pack()

    # Convert button
    tk.Button(root, text="Convert", command=convert).pack(pady=10)

    # Output display
    output_label = tk.Label(root, text="", font=("Arial", 14))
    output_label.pack()

    root.mainloop()

main()

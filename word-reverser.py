import tkinter as tk
from tkinter import messagebox

def reverse_words():
    input_text = entry.get()
    if not input_text.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    reversed_text = ' '.join(word[::-1] for word in input_text.split())
    output_label.config(text=reversed_text)

# Colors
bg_color = "#1e1e1e"
fg_color = "#f5f5f5"
button_color = "#3c3c3c"
highlight_color = "#007acc"

# GUI setup
root = tk.Tk()
root.title("Word Reverser")
root.geometry("500x250")
root.configure(bg=bg_color)

# Labels and Entry
tk.Label(root, text="Enter a sentence:", bg=bg_color, fg=fg_color, font=("Segoe UI", 10)).pack(pady=(15, 5))

entry = tk.Entry(root, width=50, bg=button_color, fg=fg_color, insertbackground=fg_color,
                 highlightbackground=highlight_color, highlightcolor=highlight_color, relief="flat", font=("Segoe UI", 10))
entry.pack(pady=5)

# Button
tk.Button(root, text="Reverse Words", command=reverse_words, bg=highlight_color, fg="white",
          activebackground="#005f9e", relief="flat", font=("Segoe UI", 10)).pack(pady=15)

# Output Label
output_label = tk.Label(root, text="", bg=bg_color, fg=highlight_color, font=("Segoe UI", 12), wraplength=460)
output_label.pack(pady=5)

root.mainloop()

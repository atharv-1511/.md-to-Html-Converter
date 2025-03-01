import os
import markdown
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import webbrowser

def convert_markdown_to_html(md_file_path, output_folder):
    try:
        if not os.path.exists(md_file_path):
            messagebox.showerror("Error", "Markdown file not found!")
            return

        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        
        html_content = markdown.markdown(md_content)
        
        output_file = os.path.join(output_folder, os.path.basename(md_file_path).replace(".md", ".html"))
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
        
        messagebox.showinfo("Success", f"Conversion successful! Output saved at: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_markdown_file():
    file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
    entry_md_path.delete(0, tk.END)
    entry_md_path.insert(0, file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    entry_output_folder.delete(0, tk.END)
    entry_output_folder.insert(0, folder_path)

def convert_file():
    md_file_path = entry_md_path.get()
    output_folder = entry_output_folder.get()
    if not md_file_path or not output_folder:
        messagebox.showwarning("Warning", "Please select both input file and output folder.")
        return
    convert_markdown_to_html(md_file_path, output_folder)

def open_portfolio(event):
    webbrowser.open_new("https://atharvraskar.me/")

# Create GUI window
root = tk.Tk()
root.title("Markdown to HTML Converter")
root.geometry("600x400")
root.configure(bg="#2c3e50")

style = ttk.Style()
style.configure("TButton", font=("Arial", 11, "bold"), padding=6)
style.configure("TLabel", font=("Arial", 11), background="#2c3e50", foreground="white")
style.configure("TEntry", font=("Arial", 10), padding=5)

# Title Label
title_label = tk.Label(root, text="Markdown to HTML Converter", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=15)

# Main frame
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=10, padx=20, fill="x")

# Adjust grid layout for alignment
frame.columnconfigure(1, weight=1)

# Markdown file selection
label_md = ttk.Label(frame, text="Markdown File:")
label_md.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_md_path = ttk.Entry(frame, width=45)
entry_md_path.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
btn_browse_md = ttk.Button(frame, text="Browse", command=select_markdown_file)
btn_browse_md.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

# Output folder selection
label_output = ttk.Label(frame, text="Output Folder:")
label_output.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_output_folder = ttk.Entry(frame, width=45)
entry_output_folder.grid(row=1, column=1, padx=1.0, pady=10, sticky="ew")
btn_browse_output = ttk.Button(frame, text="Browse", command=select_output_folder)
btn_browse_output.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

# Convert button
btn_convert = ttk.Button(root, text="Convert", command=convert_file, style="TButton")
btn_convert.pack(pady=20)

# Footer Label with Clickable Link
footer_frame = tk.Frame(root, bg="#2c3e50")
footer_frame.pack(side="bottom", pady=10)

footer_label = tk.Label(footer_frame, text="Developed by ", font=("Arial", 10), bg="#2c3e50", fg="white")
footer_label.pack(side="left")

portfolio_link = tk.Label(footer_frame, text="Atharv Raskar", font=("Arial", 10, "underline"), bg="#2c3e50", fg="white", cursor="hand2")
portfolio_link.pack(side="left")
portfolio_link.bind("<Button-1>", open_portfolio)

# Run the application
root.mainloop()
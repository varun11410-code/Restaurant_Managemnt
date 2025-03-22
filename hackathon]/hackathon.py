import tkinter as tk
from tkinterweb import HtmlFrame
import os

# Create main application window
root = tk.Tk()
root.title("Hotel Project")
root.geometry("800x600")  # Set window size

# Create an HTML display frame
frame = HtmlFrame(root)  
frame.pack(fill="both", expand=True)

# Load the local HTML file
file_path = os.path.abspath("index.html")  # Ensure correct path
frame.load_file(file_path)

# Run the app
root.mainloop()

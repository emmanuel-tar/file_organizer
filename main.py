
import os
import shutil
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog, messagebox
import logging

# Configure logging
logging.basicConfig(
    filename="file_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_file_access_time(file_path):
    """Get the last access time of a file."""
    return os.path.getatime(file_path)

def organize_folder_by_usage(directory, threshold_days):
    """Organize files and folders by usage frequency."""
    try:
        # Create folders for organization
        frequently_used_dir = os.path.join(directory, "Frequently_Used")
        least_used_dir = os.path.join(directory, "Least_Used")

        os.makedirs(frequently_used_dir, exist_ok=True)
        os.makedirs(least_used_dir, exist_ok=True)

        # Calculate threshold time
        threshold_time = datetime.now() - timedelta(days=threshold_days)

        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):  # Only organize files
                access_time = datetime.fromtimestamp(get_file_access_time(item_path))
                if access_time > threshold_time:
                    shutil.move(item_path, frequently_used_dir)
                else:
                    shutil.move(item_path, least_used_dir)

        logging.info(f"Files in {directory} organized successfully.")
        return True
    except Exception as e:
        logging.error(f"Error organizing folder {directory}: {e}")
        return False

def browse_directory():
    """Browse and select a directory."""
    folder_selected = filedialog.askdirectory()
    entry_directory.delete(0, tk.END)
    entry_directory.insert(0, folder_selected)

def start_organization():
    """Start the folder organization process."""
    directory = entry_directory.get()
    if not os.path.exists(directory):
        messagebox.showerror("Error", "Selected directory does not exist.")
        return

    try:
        threshold_days = int(entry_days.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of days.")
        return

    success = organize_folder_by_usage(directory, threshold_days)
    if success:
        messagebox.showinfo("Success", f"Files in {directory} organized successfully!")
    else:
        messagebox.showerror("Error", f"An error occurred while organizing {directory}.")

# GUI Setup
root = tk.Tk()
root.title("File Organizer by Usage Frequency")

# Directory Selection
tk.Label(root, text="Select Directory:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_directory = tk.Entry(root, width=50)
entry_directory.grid(row=0, column=1, padx=10, pady=10)
btn_browse = tk.Button(root, text="Browse", command=browse_directory)
btn_browse.grid(row=0, column=2, padx=10, pady=10)

# Threshold Days
tk.Label(root, text="Threshold Days (e.g., 30):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_days = tk.Entry(root, width=10)
entry_days.insert(0, "30")  # Default value
entry_days.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Start Button
btn_start = tk.Button(root, text="Organize", command=start_organization)
btn_start.grid(row=2, column=1, pady=20)

root.mainloop()


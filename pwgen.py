# Import required libraries
import os
import random
import tkinter as tk
import tkinter.messagebox as mbox
# Import the ttk module for themed widgets
from tkinter import ttk
import json
from tkinter import filedialog

# Function to generate a password
def generate_password():
    # Define possible characters for the password
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!§$%&_()@."

    # Combine all possible characters into a single string
    string = lower + upper + numbers + symbols
    length = 18
    # Generate a random password of length 16 using the characters in the string
    password = "".join(random.sample(string, length))

    # Delete any previous text in the password_text widget and insert the new password
    password_text.delete('1.0', tk.END)
    password_text.insert(tk.END, password)

# Function to copy the password to the clipboard
def copy_to_clipboard():
    # Get the password from the password_text widget
    password = password_text.get("1.0", "end-1c")
    # Clear the clipboard and append the password to it
    root.clipboard_clear()
    root.clipboard_append(password)
    # Show an information message to the user that the password has been copied to the clipboard
    mbox.showinfo("Password Generator", "Password copied to clipboard.")

# Function to save the password to a file
def save_password():
    # Get the password from the password_text widget and the username from the username_entry widget
    password = password_text.get("1.0", "end-1c")
    username = username_entry.get()

    # If no username was entered, show an error message to the user and return
    if not username:
        mbox.showerror("Error", "Please enter a username.")
        return

    # If the file to store the passwords doesn't exist, prompt the user to select a location to save the file
    if not os.path.isfile('passwords.json'):
        file_path = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[("JSON Files", "*.json")], initialdir=os.getcwd())
        if not file_path:
            # If no file was selected, return
            return
        else:
            # If a file was selected, create an empty dictionary and store it in the file
            with open(file_path, 'w') as file:
                json.dump({}, file)

    # Read the existing file to get the passwords that have already been saved
    with open('passwords.json', 'r') as file:
        data = json.load(file)

    # Add the new password to the dictionary of passwords, using the username as the key
    if username in data:
        # If the username already exists in the file, show an error message to the user and return
        mbox.showerror("Error", "Username already exists.")
        return
    else:
        data[username] = password

    # Write the updated dictionary to the file
    with open('passwords.json', 'w') as file:
        json.dump(data, file)

    # Show an information message to the user that the password has been saved
    mbox.showinfo("Password Generator", "Password saved.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a style for the themed widgets
style = ttk.Style()

# Configure the style for the label and entry widgets
style.configure("TLabel", font=("Helvetica", 14), foreground="#FFFFFF", background="#333333")
style.configure("TEntry", font=("Helvetica", 14), foreground="#333333", background="#FFFFFF")

# Create a frame to hold the password display and entry widgets
frame = ttk.Frame(root, borderwidth=2, relief="groove", padding=10)
frame.pack(pady=10)

# Create a label and entry for the username
username_label = ttk.Label(frame, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = ttk.Entry(frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a label and text box for the generated password
password_label = ttk.Label(frame, text="Generated Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_text = tk.Text(frame, height=1, width=20, font=("Helvetica", 14), foreground="#333333", background="#FFFFFF")
password_text.grid(row=1, column=1, padx=5, pady=5)

# Create a button to generate a new password
generate_button = ttk.Button(root, text="Generate Password", command=generate_password, style="Accent.TButton")
generate_button.pack(pady=5)

# Create a button to copy the password to the clipboard
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, style="Accent.TButton")
copy_button.pack(pady=5)

# Create a button to save the password
save_button = ttk.Button(root, text="Save Password", command=save_password, style="Accent.TButton")
save_button.pack(pady=5)

# Configure the style for the themed buttons
style.configure("Accent.TButton", font=("Helvetica", 14), foreground="#333333", background="#008CBA", padding=10, borderwidth=2, relief="groove")

# Configure the style for the window
style.configure("TFrame", background="#333333")

# Start the GUI
root.mainloop()

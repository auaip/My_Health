import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3
from os import path


class AddressBook(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Address Book")
        self.geometry("800x600")

        self.address_text = tk.Text(self, height=30, width=100)
        self.address_text.pack(padx=20, pady=20)

        self.load_address_book()

        self.btn_delete = tk.Button(self, text="Delete from Address Book", command=self.delete_selected)
        self.btn_delete.pack(pady=10)

    def load_address_book(self):
        try:
            with open("AddressBook.txt", "r") as file:
                content = file.read()
                self.address_text.insert(tk.END, content)
        except FileNotFoundError:
            self.address_text.insert(tk.END, "Address Book not found.")

    def delete_selected(self):
        # Get current selection in the Text widget
        selection = self.address_text.tag_ranges(tk.SEL)
        if not selection:
            messagebox.showerror("Error", "Please select a doctor's entry to delete.")
            return

        start, end = selection
        selected_text = self.address_text.get(start, end)

        # Ask for confirmation before deletion
        confirmed = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete this entry?\n\n{selected_text}")
        if confirmed:
            # Delete the selected text
            self.address_text.delete(start, end)
            messagebox.showinfo("Success", "Doctor's entry deleted from Address Book.")
            # Delete the selected text from the Text widget
            self.address_text.delete(start, end)

            # Delete the selected entry from AddressBook.txt
            self.delete_entry_from_file(selected_text)

            messagebox.showinfo("Success", "Doctor's entry deleted from Address Book.")

    def delete_entry_from_file(self, entry_text):
        try:
            with open("AddressBook.txt", "r") as file:
                lines = file.readlines()

            with open("AddressBook.txt", "w") as file:
                for line in lines:
                    if line.strip() != entry_text.strip():  # Skip the line to delete
                        file.write(line)
        except FileNotFoundError:
            messagebox.showerror("Error", "Address Book not found.")

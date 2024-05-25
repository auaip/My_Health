import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3
from os import path


class DoctorResearch(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Doctor Research")
        self.geometry("600x400")

        self.label_specialty = tk.Label(self, text="Specialty:")
        self.label_specialty.pack(pady=10)

        self.entry_specialty = tk.Entry(self)
        self.entry_specialty.pack(pady=10)

        self.btn_search = tk.Button(self, text="Search", command=self.search_and_display)
        self.btn_search.pack(pady=10)

        self.result_listbox = tk.Listbox(self, height=10, width=60)
        self.result_listbox.pack(pady=20)

        self.btn_add_to_address_book = tk.Button(self, text="Add Selected to Address Book", command=self.add_selected_to_address_book)
        self.btn_add_to_address_book.pack(pady=10)

        self.selected_doctors = []  # To store selected doctors' information

    def search_and_display(self):
        specialty = self.entry_specialty.get()

        if not specialty:
            messagebox.showerror("Error", "Please enter a specialty.")
            return

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT name, specialty, distance FROM doctors WHERE specialty=?", (specialty,))
        doctors = c.fetchall()

        conn.close()

        self.result_listbox.delete(0, tk.END)  # Clear previous results

        if doctors:
            for i, doctor in enumerate(doctors, start=1):
                display_text = f"Name: {doctor[0]}, Specialty: {doctor[1]}, Distance: {doctor[2]} km"
                self.result_listbox.insert(tk.END, display_text)
            self.selected_doctors = doctors
        else:
            messagebox.showinfo("No Results", "No doctors found with that specialty.")

    def add_selected_to_address_book(self):
        selected_indices = self.result_listbox.curselection()

        if not selected_indices:
            messagebox.showerror("Error", "No doctors selected.")
            return

        try:
            with open("AddressBook.txt", "a") as file:
                #file.write("\nDoctors:\n")
                for index in selected_indices:
                    doctor = self.selected_doctors[index]
                    file.write(f"Name: {doctor[0]}, Specialty: {doctor[1]}, Distance: {doctor[2]} km\n\n")
            messagebox.showinfo("Success", "Selected doctors added to Address Book.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add doctors to Address Book: {str(e)}")


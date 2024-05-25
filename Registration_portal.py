import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3
from database import create_user_database, insert_example_results

class RegistrationPortal(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Registration")
        self.geometry("600x400")

        self.label_name = tk.Label(self, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        self.label_firstname = tk.Label(self, text="First name:")
        self.label_firstname.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.entry_firstname = tk.Entry(self)
        self.entry_firstname.grid(row=1, column=1, padx=10, pady=5)

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=2, column=1, padx=10, pady=5)

        self.label_national_registration_number = tk.Label(self, text="National Registration Number :")
        self.label_national_registration_number.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.entry_national_registration_number = tk.Entry(self)
        self.entry_national_registration_number.grid(row=3, column=1, padx=10, pady=5)

        self.label_date_of_birth = tk.Label(self, text="Date of Birth:")
        self.label_date_of_birth.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.entry_date_of_birth = tk.Entry(self)
        self.entry_date_of_birth.grid(row=4, column=1, padx=10, pady=5)

        self.btn_register = tk.Button(self, text="Register", command=self.register_user)
        self.btn_register.grid(row=6, columnspan=2, padx=10, pady=5)

    def register_user(self):
        name = self.entry_name.get()
        firstname= self.entry_firstname.get()
        password = self.entry_password.get()
        national_registration_number = self.entry_national_registration_number.get()
        date_of_birth = self.entry_date_of_birth.get()

        if not name or not firstname or not password or not national_registration_number or not date_of_birth:
            messagebox.showerror("Registration Failed", "Please fill in all fields.")
            return
    
        else:
        # Insert user information into the database
            with sqlite3.connect('database.db') as conn:
                c = conn.cursor()
                c.execute("INSERT INTO Patients (name, firstname, password, national_registration_number, date_of_birth) VALUES (?, ?, ?, ?, ?)", (name, firstname, password, national_registration_number, date_of_birth))
                conn.commit()
      
        create_user_database(national_registration_number)
        insert_example_results(national_registration_number)

        messagebox.showinfo("Registration Successful", "Registration done!")
        self.destroy()

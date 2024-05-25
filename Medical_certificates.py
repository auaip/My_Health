import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3
from os import path

class MedicalCertificate(tk.Toplevel):
    def __init__(self, master, national_registration_number) :
        super().__init__(master)
        self.title("Certificates")
        self.geometry("500x300")
        self.national_registration_number = national_registration_number

        self.result_text = tk.Text(self, height=10, width=60)
        self.result_text.pack(pady=20)

        # Fetch and display certificate data
        self.display_certificates(self.national_registration_number)

    def display_certificates(self, national_nb):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Select rows where type is 'Certificate'
        c.execute("SELECT * FROM prescriptions_certificates WHERE type=? AND registration_nb=?", ('Certificate',national_nb))
        certificates = c.fetchall()

        conn.close()

        if certificates:
            # Display the certificates
            display_text = ""
            for certificate in certificates:
                display_text += f"Type: {certificate[0]}\nLast Name: {certificate[1]}\nFirst Name: {certificate[2]}\nRegistration Number: {certificate[3]}\nDoctor: {certificate[4]}\nDate: {certificate[5]}\n\n"

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, display_text)
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "No certificates found for this registration number.")

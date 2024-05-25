import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3
from os import path

class OrganDonation(tk.Toplevel) :
    def __init__(self, master, national_registration_number):
        super().__init__(master)
        self.title("Organ Donation")
        self.geometry("500x300")
        self.national_registration_number = national_registration_number

    # Radio buttons for selecting donation

        self.donation = tk.Label(self, text="Do you accept to donate your organs ?")
        self.donation.grid(row=0, column=1)

        self.choice = tk.StringVar()
        self.choice.set(self.choice_saved())  # Default designation is yes

        self.admin_radio = tk.Radiobutton(self, text="Yes", variable=self.choice, value="Yes")
        self.admin_radio.grid(row=1, column=0, padx=10, pady=5)

        self.doctor_radio = tk.Radiobutton(self, text="No", variable=self.choice, value="No")
        self.doctor_radio.grid(row=1, column=1, padx=10, pady=5)

        self.patient_radio = tk.Radiobutton(self, text="My family can choose", variable=self.choice, value="My family can choose")
        self.patient_radio.grid(row=1, column=2, padx=10, pady=5)

        self.btn_login = tk.Button(self, text="Save", command=self.save)
        self.btn_login.grid(row=2, column=1, padx=10, pady=5)

    def choice_saved(self):
        self.data_file = f"{self.national_registration_number}.txt"
        self.data = {}
        try:
            with open(self.data_file, 'r') as f:
                for line in f:
                    if "=" in line:
                        key, value = line.strip().split('=')
                        self.data[key] = value
                    else : 
                        continue
        except FileNotFoundError:
            pass
        try :
            return self.data["Organs Donation"]
        except :
            return "My family can choose"

    def save (self):
        self.data_file = f"{self.national_registration_number}.txt"
        if path.exists(self.data_file) == False :
            with open(self.data_file, 'w') as file:
                file.close()
        with open(self.data_file, 'r') as file:
            lines = file.readlines()
            while len(lines)<11 :
                lines.append("\n")
        file.close()
        with open(self.data_file, 'w') as file:
            lines[9] = "Organs Donation="+self.choice.get() +"\n"
            file.writelines(lines)
        self.destroy()

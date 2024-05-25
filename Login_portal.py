import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3
from os import path
from Patients_portal import PatientPortal
from Registration_portal import RegistrationPortal

class LoginPortal:
    def __init__(self, master):
        # Initialize the login portal
        self.master = master
        
        # Connect to the database
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()

        #Create a credentials table
        self.conn.execute("CREATE TABLE IF NOT EXISTS Patients (name, firstname, password, national_registration_number, date_of_birth)")
        
        # Set up the main window
        self.master.title("Login Portal")
        
        # Create GUI elements for the login form
        self.create_widgets()

    def create_widgets(self):                                        
        self.textename = tk.Label(self.master, text="Name:")
        self.textename.pack()
        self.entry_name = tk.Entry(self.master)
        self.entry_name.pack()

        self.textefirstname = tk.Label(self.master, text="First name:")
        self.textefirstname.pack()
        self.entry_firstname = tk.Entry(self.master)
        self.entry_firstname.pack()
        
        self.text_national_registration_number = tk.Label(self.master, text="National Registration Number:")
        self.text_national_registration_number.pack()
        self.entry_national_registration_number = tk.Entry(self.master)
        self.entry_national_registration_number.pack()

        self.textpassword = tk.Label(self.master, text="Password:")
        self.textpassword.pack()
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack()

        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(self.master, text="Register", command=self.registration)
        self.register_button.pack()
        # anchor=tk.NE

        
    def login(self):
        
        name = self.entry_name.get()
        firstname = self.entry_firstname.get()
        password = self.entry_password.get()
        national_registration_number = self.entry_national_registration_number.get()
        if not name or not firstname or not password or not national_registration_number:
            if not name :
                self.message = tk.messagebox.showinfo(title=None, message="Please enter a name")
            elif not firstname :
                self.message = tk.messagebox.showinfo(title=None, message="Please enter a firstname")
            elif not national_registration_number:
                self.message = tk.messagebox.showinfo(title=None, message="Please enter a national registration number")

            elif not password :
                self.message = tk.messagebox.showinfo(title=None, message="Please enter your password")

        else :
            self.authentication(name, firstname, national_registration_number, password)
             

    def authentication(self, name, firstname, national_registration_number, password): 
        conn = sqlite3.connect('database.db')                         
        self.cur.execute("SELECT * FROM Patients WHERE name=? AND firstname=? AND national_registration_number = ? AND password=?", (name, firstname, national_registration_number,password))
        self.ID = self.cur.fetchone()
        conn.close()

        if self.ID :
            self.patient_portal(national_registration_number)
            return True, national_registration_number

        else :
            self.message = tk.messagebox.showwarning(title=None, message="There is a problem")
            #return False

    def patient_portal(self, national_registration_number):                                            
        PatientPortal(self.master, self.ID, national_registration_number) 
    
    def registration(self):
        RegistrationPortal(self.master)

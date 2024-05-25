import tkinter as tk
import sqlite3

class Prescriptions(tk.Toplevel):
    def __init__(self, master, national_registration_number) :
        super().__init__(master)
        self.title("Prescriptions")
        self.geometry("500x300")
        self.national_registration_number = national_registration_number

        self.result_text = tk.Text(self, height=10, width=60)
        self.result_text.pack(pady=20)

        # Fetch and display prescription data
        self.display_prescription(self.national_registration_number)
        
    def display_prescription(self, national_nb):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Select rows where type is 'Prescription' and the registration number matches the given national_nb
        c.execute("SELECT * FROM prescriptions_certificates WHERE type=? AND registration_nb=?", ('Prescription', national_nb))
        prescriptions = c.fetchall()

        conn.close()

        if prescriptions:
            # Display the prescriptions
            display_text = ""
            for prescription in prescriptions:
                display_text += f"Type: {prescription[0]}\nLast Name: {prescription[1]}\nFirst Name: {prescription[2]}\nRegistration Number: {prescription[3]}\nDoctor: {prescription[4]}\nPrescription: {prescription[5]}\n\n"

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, display_text)
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "No prescriptions found for this registration number.")

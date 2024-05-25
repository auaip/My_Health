import tkinter as tk
from tkinter import *
from os import path

class MedicalRecords(tk.Toplevel) :
    def __init__(self, master, national_registration_number):
        super().__init__(master)
        self.title("Medical Record Window")
        self.geometry("400x600")
        self.national_registration_number = national_registration_number
        self.open_data()
        self.initUI()

    def open_data(self):
        # Try to load the settings from a file named "national_registration_number.txt"
        data_file = f"{self.national_registration_number}.txt"
        self.data = {}
        try:
            with open(data_file, 'r') as f:
                for line in f:
                    if "=" in line:
                        key, value = line.strip().split('=')
                        self.data[key] = value
                    else : 
                        continue
        except FileNotFoundError:
            # If the file is not found, we'll just use empty settings
            self.data = {
                "Name": "",
                "Firstname": "",
                "National Registration Number": "",
                "Date of birth": "",
                "Weight": "",
                "Height": "",
                "Blood type": "",
                "Health issues": "",
                "Vaccines": ""
            }

    def initUI(self):
        # Labels and corresponding setting keys
        labels_and_keys = [
            ("Name:", "Name"),
            ("Firstname:", "Firstname"),
            ("National Registration Number:", "National Registration Number"),
            ("Date of birth:", "Date of birth"),
            ("Weight:", "Weight"),
            ("Height:", "Height"),
            ("Blood type:", "Blood type"),
            ("Health issues", "Health issues"),
            ("Vaccines", "Vaccines")
        ]

        self.text_fields = {}
        # Create rows with labels and text fields
        for label_text, data_key in labels_and_keys:
            # Add label to the row
            self.label = tk.Label(self, text=label_text)
            self.label.pack()

            # Add text field to the row with the corresponding setting value
            self.text_field = tk.Entry(self)
            self.value = (self.data.get(data_key, ""))
            self.text_field.insert(0,self.value)
            self.text_field.pack()
            self.text_fields[data_key] = self.text_field

        # Add Save button
        self.save_button = tk.Button(self, text="Save", command=self.save_data)
        self.save_button.pack()


    def save_data(self):
        # Construct the settings string
        settings_data = "\n".join([f"{key}={self.text_fields[key].get()}" for key in self.text_fields])

        #self.close()
        if path.exists(f"{self.national_registration_number}.txt") == False :
            with open(f"{self.national_registration_number}.txt", 'w') as file:
                file.close()
        with open(f"{self.national_registration_number}.txt", 'r') as file:
            lines = file.readlines()
            while len(lines)<11 :
                lines.append("\n")
        file.close()
        with open(f"{self.national_registration_number}.txt", 'w') as file:
            lines[0] = settings_data +"\n"
            del lines[1:9] #remove old item 
            file.writelines(lines)
        self.destroy()
        # liste des vaccins, opérations, problèmes de santé (asthme,...),...

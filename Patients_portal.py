import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Results import Results
from Medical_records import MedicalRecords
from Prescriptions import Prescriptions
from Medical_certificates import MedicalCertificate
from Doctor_research import DoctorResearch
from Address_book import AddressBook
from Organ_donation import OrganDonation
from database import *

def run_database() :
    create_prescription_certificate_table()
    create_doctors_table()

class PatientPortal(tk.Toplevel):
    def __init__(self, master, ID, national_registration_number):
        super().__init__(master)
        self.title("Patient Window")
        self.geometry("490x350")
        self.ID = ID
        self.national_registration_number = national_registration_number
        run_database()

        # Function to create a bordered frame
        def create_bordered_frame(parent):
            frame = tk.Frame(parent, bd=1, relief="solid")
            return frame

        # Button to see our adress book
        self.frame_adress_book = create_bordered_frame(self)
        self.frame_adress_book.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.button_adress_book = tk.Button(self.frame_adress_book, text="Adress Book", bg="thistle", command=self.open_adress_book)
        self.button_adress_book.pack(fill=tk.BOTH, expand=True)
        self.label_adress_book = tk.Label(self.frame_adress_book, text="View of the doctors \n added in your address book ")
        self.label_adress_book.pack(fill=tk.BOTH, expand=True)

        # Button to see the results
        self.frame_results = create_bordered_frame(self)
        self.frame_results.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        self.button_results = tk.Button(self.frame_results, text="See patient results", bg="thistle", command=self.open_results)
        self.button_results.pack(fill=tk.BOTH, expand=True)
        self.label_results = tk.Label(self.frame_results, text="View of the \n different medical results \n sorted by medical domain")
        self.label_results.pack(fill=tk.BOTH, expand=True)

        # Button to see the medical record
        self.frame_medical_record = create_bordered_frame(self)
        self.frame_medical_record.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        self.button_medical_record = tk.Button(self.frame_medical_record, text="Medical Record", bg="thistle", command=self.open_medical_record)
        self.button_medical_record.pack(fill=tk.BOTH, expand=True)
        self.label_medical_record = tk.Label(self.frame_medical_record, text="Complete or update \n your medical record")
        self.label_medical_record.pack(fill=tk.BOTH, expand=True)

        # Button to see my prescriptions
        self.frame_prescriptions = create_bordered_frame(self)
        self.frame_prescriptions.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.button_prescriptions = tk.Button(self.frame_prescriptions, text="Prescriptions", bg="thistle", command=self.open_prescriptions)
        self.button_prescriptions.pack(fill=tk.BOTH, expand=True)
        self.label_prescriptions = tk.Label(self.frame_prescriptions, text="List of my \n prescriptions per date")
        self.label_prescriptions.pack(fill=tk.BOTH, expand=True)

        # Button to see my medical certificates
        self.frame_medical_certificates = create_bordered_frame(self)
        self.frame_medical_certificates.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.button_medical_certificates = tk.Button(self.frame_medical_certificates, text="Medical Certificates", bg="thistle", command=self.open_medical_certif)
        self.button_medical_certificates.pack(fill=tk.BOTH, expand=True)
        self.label_medical_certificates = tk.Label(self.frame_medical_certificates, text="List of my \n certificates per date")
        self.label_medical_certificates.pack(fill=tk.BOTH, expand=True)

        # Documents officiels ? genre dont d'organes, donner son corps à la science etc
        self.frame_donation = create_bordered_frame(self)
        self.frame_donation.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        self.button_donation = tk.Button(self.frame_donation, text="Organ Donation", bg="thistle", command=self.organ_donation)
        self.button_donation.pack(fill=tk.BOTH, expand=True)
        self.label_donation = tk.Label(self.frame_donation, text="Update and view of \n your choice regarding \n organ donation ")
        self.label_donation.pack(fill=tk.BOTH, expand=True)

        # Button to search for a doctor
        self.frame_doctor = create_bordered_frame(self)
        self.frame_doctor.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        self.button_doctor = tk.Button(self.frame_doctor, text="Search for a Doctor", bg="thistle", command=self.search_doctor)
        self.button_doctor.pack(fill=tk.BOTH, expand=True)
        self.label_doctor = tk.Label(self.frame_doctor, text="You can find the \n doctors per specialty and \n have access to the \n distance from you \n and add it to \n an address book")
        self.label_doctor.pack(fill=tk.BOTH, expand=True)

    def open_results(self):
        Results(self.master, self.national_registration_number)

    def open_medical_record(self):
        MedicalRecords(self.master, self.national_registration_number)

    def open_prescriptions(self):
        Prescriptions(self.master, self.national_registration_number)

    def open_medical_certif(self):
        MedicalCertificate(self.master, self.national_registration_number)

    def search_doctor(self):
        DoctorResearch(self.master)

    def open_adress_book(self):
        AddressBook(self.master)

    def organ_donation(self):
        OrganDonation(self.master, self.national_registration_number)

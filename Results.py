import tkinter as tk
import sqlite3

class Results(tk.Toplevel):
    def __init__(self, master, national_registration_number):
        super().__init__(master)
        self.title("Patient Results")
        self.geometry("800x600")
        self.national_registration_number = national_registration_number

        # Create a text widget to display the results
        self.results_text = tk.Text(self, wrap="word")
        self.results_text.pack(expand=True, fill="both")

        # Fetch results from the database using the national registration number
        formatted_results = self.fetch_results_from_database(self.national_registration_number)
        # Display the formatted results
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", formatted_results)

    def fetch_results_from_database(self, national_registration_number):
        # Retrieve results from the user's database using the national registration number
        db_name = f"{national_registration_number}.db"
        with sqlite3.connect(db_name) as conn:
            c = conn.cursor()

            # Initialize formatted_results as an empty string
            formatted_results = ""
            # Fetch blood test results
            c.execute("SELECT * FROM BloodTestResults ORDER BY date DESC")
            blood_test_results = c.fetchall()

            # Format blood test results
            # Format the results into a string
            for result in blood_test_results:
                formatted_results += f" Blood Test Result: {result[1]}, Date: {result[0]} \n"

            # Fetch dermatology test results
            c.execute("SELECT * FROM DermatologyTestResults ORDER BY date DESC")
            dermatology_test_results = c.fetchall()

            # Format dermatology test results
            # Format the results into a string
            for result in dermatology_test_results:
                formatted_results += f" Dermatology Test Type: {result[1]}, Results: {result[2]}, Date: {result[0]}\n"

            # Fetch dermatology test results
            c.execute("SELECT * FROM CancerTestResults ORDER BY date DESC")
            cancer_test_results = c.fetchall()
            #Format cancer test results
            for result in cancer_test_results:
                formatted_results += f" Cancer Treatment Type: {result[1]}, Results: {result[2]}, Date: {result[0]}\n"

        return formatted_results

import sqlite3

# Create and populate the prescriptions database
def create_prescription_certificate_table():
   # conn = sqlite3.connect('prescriptions_certificates.db')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute(''' CREATE TABLE IF NOT EXISTS prescriptions_certificates (
            type TEXT,
            last_name TEXT,
            first_name TEXT,
            registration_nb REAL,
            doctor TEXT,
            prescription_certificate TEXT
        ) ''')
    
    prescription_data = [
    ("Prescription","Smith", "John", 123456, "Dr. Johnson", "Aspirin"),
    ("Prescription","Johnson", "Emily", 789012, "Dr. Smith", "Antibiotics"),
    ("Prescription","Williams", "Michael", 345678, "Dr. Brown", "Painkillers"),
    ("Prescription","Brown", "Jessica", 901234, "Dr. Williams", "Antihistamines"),
    ("Prescription","Jones", "Daniel", 567890, "Dr. Taylor", "Vitamins"),
    ("Prescription","Taylor", "Olivia", 234567, "Dr. Jones", "Cough syrup"),
    ("Prescription","Anderson", "William", 890123, "Dr. Martinez", "Eye drops"),
    ("Prescription","Martinez", "Sophia", 456789, "Dr. Anderson", "Antacids"),
    ("Prescription","Thomas", "Ava", 112233, "Dr. Garcia", "Insulin"),
    ("Prescription","Garcia", "Ethan", 998877, "Dr. Thomas", "Antidepressants")
]
    
    certificate_data = [
    ("Certificate","Smith", "John", 123456, "Dr. Johnson", "2023-05-12"),
    ("Certificate","Johnson", "Emily", 789012, "Dr. Smith", "2023-06-18"),
    ("Certificate","Williams", "Michael", 345678, "Dr. Brown", "2023-07-24"),
    ("Certificate","Brown", "Jessica", 901234, "Dr. Williams", "2023-08-30"),
    ("Certificate","Jones", "Daniel", 567890, "Dr. Taylor", "2023-09-05"),
    ("Certificate","Taylor", "Olivia", 234567, "Dr. Jones", "2023-10-11"),
    ("Certificate","Anderson", "William", 890123, "Dr. Martinez", "2023-11-17"),
    ("Certificate","Martinez", "Sophia", 456789, "Dr. Anderson", "2023-12-23"),
    ("Certificate","Thomas", "Ava", 112233, "Dr. Garcia", "2024-01-29"),
    ("Certificate","Garcia", "Ethan", 998877, "Dr. Thomas", "2024-02-04")
]

    for prescription in prescription_data:
        type,name, first_name, id, doctor, date = prescription
        c.execute("SELECT * FROM prescriptions_certificates WHERE type = ? AND last_name = ? AND registration_nb = ? AND prescription_certificate = ? AND doctor = ?", (type,name,id, date, doctor))
        existing_prescription = c.fetchone()

        if existing_prescription is None:
            c.execute("INSERT INTO prescriptions_certificates (type, last_name, first_name, registration_nb, doctor, prescription_certificate) VALUES (?,?, ?, ?, ?, ?)", (type,name, first_name, id, doctor, date))

    for certif in certificate_data:
        type,name, first_name, id, doctor, date = certif
        c.execute("SELECT * FROM prescriptions_certificates WHERE type = ? AND last_name = ? AND registration_nb = ? AND prescription_certificate = ? AND doctor = ?", (type,name,id, date, doctor))
        existing_certificate = c.fetchone()

        if existing_certificate is None:
            c.execute("INSERT INTO prescriptions_certificates (type, last_name, first_name, registration_nb, doctor, prescription_certificate) VALUES (?,?, ?, ?, ?, ?)", (type,name, first_name, id, doctor, date))

    conn.commit()
    conn.close()

    
def create_user_database(national_registration_number):
    # Create a database with the national registration number as its name
    db_name = f"{national_registration_number}.db"

    # Connect to the database
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Create tables and insert data
    c.execute("CREATE TABLE IF NOT EXISTS UserData (name TEXT, firstname TEXT, password TEXT, date_of_birth TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS BloodTestResults (date TEXT, result TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS DermatologyTestResults (date TEXT, test_type TEXT, results TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS CancerTestResults (date TEXT, test_type TEXT, results TEXT)")

    conn.commit()
    conn.close()

def insert_example_results(national_registration_number):
    # Define the example test results
    skin_results = [
        {"test_date": "2023-05-13","test_type": "Visual Examination", "results": "Suspicious mole on upper back, red, itchy patches on arms and legs"},
        {"test_date": "2023-05-15","test_type": "Skin Biopsy", "results": "Benign mole on upper back"},
        {"test_date": "2023-05-14","test_type": "Patch Testing", "results": "Allergic reaction to nickel"},
        {"test_date": "2023-05-13","test_type": "Blood Tests", "results": "Normal levels of antibodies, no signs of infection or autoimmune disorders"}
    ]

    blood_results = [
        {"test_date": "2023-01-24", "Blood test result": "Too much sugar !!lol"},
        {"test_date":"2024-04-30", "Blood test result":"Normal"}
    ]

    cancer_results = [
        {"test_date": "2022-03-14", "test_type": "Imaging (MRI/CT/PET)", "results": "Reduction in tumor size by 10'%' compared to previous scan, total of 30'%' reduction"},
        {"test_date": "2022-02-23", "test_type": "Imaging (MRI/CT/PET)", "results": "Reduction in tumor size by 20'%' compared to previous scan, total of 20'%' reduction"},
        {"test_date": "2022-03-15", "test_type": "Biopsy", "results": "Histopathology: Adenocarcinoma"},
        {"test_date": "2022-01-18", "test_type": "Biopsy", "results": "Histopathology: No malignant cells found"}
    ]

    # Connect to the user's database
    db_name = f"{national_registration_number}.db"
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()

        # Insert example skin test results
        for result in skin_results:
            c.execute("INSERT INTO DermatologyTestResults (date, test_type, results) VALUES (?, ?, ?)",
                      (result["test_date"], result["test_type"], result["results"]))

        # Insert example blood test results
        for result in blood_results:
            c.execute("INSERT INTO BloodTestResults (date, result) VALUES (?, ?)",
                      (result["test_date"], result["Blood test result"]))

        # Insert example cancer test results
        for result in cancer_results:
            c.execute("INSERT INTO CancerTestResults (date, test_type, results) VALUES (?, ?, ?)",
                      (result["test_date"], result["test_type"], result["results"]))

        conn.commit()


# Create and populate the doctors database
def create_doctors_table():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Create doctors table if it does not exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS doctors (
                name TEXT,
                phone TEXT,
                address TEXT,
                specialty TEXT,
                distance REAL,
                UNIQUE(name, phone)  -- Ensure unique combination of name and phone
            )
        ''')

        doctors_data = [
            ("Dr. Smith", "0412345678", "123 Main Street, Brussels", "Dermatologist", 5.2),
            ("Dr. Johnson", "0412345679", "456 Oak Avenue, Antwerp", "Gynecologist", 8.1),
            ("Dr. Williams", "0412345680", "789 Elm Road, Ghent", "Cardiologist", 10.5),
            ("Dr. Brown", "0412345681", "321 Maple Lane, Bruges", "Pediatrician", 3.3),
            ("Dr. Davis", "0412345682", "654 Pine Drive, Liege", "Orthopedic Surgeon", 6.8),
            ("Dr. Wilson", "0412345683", "987 Birch Boulevard, Namur", "Neurologist", 12.0),
            ("Dr. Sarkees Avoo", "0488920546", "46 Rue des Loups, Bruxelles", "Neurologist", 6.0), 
            ("Dr. Zinebi", "0476920546", "12 Mollestraat, Asse", "Pediatrician", 11.4), 
            ("Dr. Marchandise", "0496754602", "2 Avenue de l'université, Bruxelles", "Cardiologist", 4.2),
            ("Dr. De Boeck", "0488332788", "77 Rue du marche aux herbes, Bruxelles", "Orthopedic Surgeon", 1.7)
        ]

        for doctor in doctors_data:
            name, phone, address, specialty, distance = doctor
            # Check if the doctor with the same name and phone already exists
            c.execute("SELECT * FROM doctors WHERE name = ? AND phone = ?", (name, phone))
            existing_doctor = c.fetchone()

            if existing_doctor is None:
                # Doctor does not exist, so insert into database
                c.execute("INSERT INTO doctors (name, phone, address, specialty, distance) VALUES (?, ?, ?, ?, ?)",
                          (name, phone, address, specialty, distance))
                

        conn.commit()
        conn.close()
    

    except sqlite3.Error as e:
        print(f"Error: {e}")

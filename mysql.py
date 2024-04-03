import sqlite3

def connect_database():
    global conn, cur
       
    conn = sqlite3.connect('patient_information.db') # will connect to db if exists, or create a new one.

    cur = conn.cursor()    
    
def create_database():
    cur.execute('''DROP TABLE IF EXISTS patient information;''')
    cur.execute('''CREATE TABLE IF NOT EXISTS "patient information" (
            "Patient_Id"	    TEXT NOT NULL,
            "First_Name"	    TEXT NOT NULL,
            "Middle_Name"	    TEXT,
            "Last_Name"	        TEXT NOT NULL,
            "Preferred_Name"	TEXT NULL,
            "Street_Address"	TEXT NOT NULL,
            "Apt_Suite_Unit"	TEXT NOT NULL,
            "City"	            TEXT NOT NULL,
            "Province"	        TEXT NOT NULL,
            "Postal_Code"	    TEXT NOT NULL,
            "Date_of_Birth"	    INTERGER NOT NULL,
            "Gender"	        TEXT NOT NULL,
            PRIMARY KEY("Patient_Id")
            );''')
    
    
    cur.execute('''INSERT INTO hospital ('Hospital_Id', 'Hospital_Name', 'Bed_Count') VALUES
                ('1', 'Toronto General Hospital', '471'),
                ('2', "St. Joseph's Health Centre", '376'),
                ('3', 'Mississauga Hospital', '751'),
                ('4', 'Credit Valley Hospital', '382')''')
    

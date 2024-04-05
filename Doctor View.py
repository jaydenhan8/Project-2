import tkinter
from tkinter import ttk
import sqlite3

### make connection with sqlite database ###
conn = sqlite3.connect('clinic.db')
cursor = conn.cursor()

cursor.execute("SELECT * From c_column")

for row in cursor.fetchall():
  patient_number = row[0]
  preferred_name = row[1]

print("Patient Number:", patient_number)
print("Preferred Name:", preferred_name)
      

window = tkinter.Tk()
window.title("Doctor View")

frame = tkinter.Frame(window)
frame.pack()

patient_info_frame =tkinter.LabelFrame(frame, text="Patient Information")
patient_info_frame.grid(row=0, column=0, padx=25, pady=25)

### show patient number which is id number ###
patient_number_label = tkinter.Label(patient_info_frame, text="Patient Number")
patient_number_label.grid(row=0, column=0)

### show patient name information ###
preferred_name_label = tkinter.Label(patient_info_frame, text="Preferred Name")
preferred_name_label.grid(row=1, column=0)

first_name_label = tkinter.Label(patient_info_frame, text="First Name")
first_name_label.grid(row=1, column=1)

middle_name_label = tkinter.Label(patient_info_frame, text="Middle Name")
middle_name_label.grid(row=1, column=2)

last_name_label = tkinter.Label(patient_info_frame, text="Last Name")
last_name_label.grid(row=1, column=3)

### gender birthday and postal code information ###
gender_label = tkinter.Label(patient_info_frame, text="Gender")
gender_label.grid(row=2, column=0)

dob_label = tkinter.Label(patient_info_frame, text="DOB")
dob_label.grid(row=2, column=1)

postal_code_label = tkinter.Label(patient_info_frame, text="Postal Code")
postal_code_label.grid(row=2, column=2)

### medical history ###
medical_history = tkinter.Label(patient_info_frame, text="Medical History")
medical_history.grid(row=5, column=0)



### close connection with mysql ###
conn.close()
### infinite loop that runs until user exit ###
window.mainloop()

from tkinter import ttk
import tkinter as tk
import sqlite3



class Clinic_Forum(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1280x720")

        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Page1, Page2, Page3, Page4, Page5):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(Page1)


    def show_frame(self,cont):

        frame = self.frames[cont]

        frame.tkraise()


class Menu_Clinic():

    def __int__(self, parent):
        self.parent = parent
        self.clinic_menu()

        def clinic_menu(self):

            self.menubar = tk.Menu(self.parent)
            self.parent.config(menu=self.menubar)

            menuFile = Menu(self.menubar)
            menuFile.add_command(label="Save", command=None)
            self.menubar.add_cascade(label="File", menu=menuFile)


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        self.menu = Menu_Clinic()


        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Clinic Form 1")
        label.pack(pady=10,padx=10)

        c_columns = ["Patient Information", "Billing Information", "Insurance Information", "Insured Information (if other than patient)"]
            #for loop for iterating all of the columns
        #creating specific for loops for each section of the form
        for column in c_columns:
            if column == "Patient Information":
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')


                #creating title entry using combox,allowing user to select
                title_label = tk.Label(self, text="Title")
                title_label.pack(anchor='w', padx=10)
                title_combobox = ttk.Combobox(self,
                                              values=["Mr", "Ms", "Mrs", "Miss", "Master", "Madam", "Sir", "Other"])
                title_combobox.pack(anchor='w', padx=10)
                title_combobox.set("Select Title")

                #creating entries under patient information
                firstn_label = tk.Label(self, text="First Name")
                firstn_label.pack(anchor='w', padx=10)
                firstn_entry = tk.Entry(self)
                firstn_entry.pack(anchor='w', padx=10)

                middlen_label = tk.Label(self, text="Middle Name")
                middlen_label.pack(anchor='w', padx=10)
                middlen_entry = tk.Entry(self)
                middlen_entry.pack(anchor='w', padx=10)

                lastn_label = tk.Label(self, text="Last Name")
                lastn_label.pack(anchor='w', padx=10)
                lastn_entry = tk.Entry(self)
                lastn_entry.pack(anchor='w', padx=10)

                prefferedn_label = tk.Label(self, text="Preferred Name (optional)")
                prefferedn_label.pack(anchor='w', padx=10)
                prefferedn_entry = tk.Entry(self)
                prefferedn_entry.pack(anchor='w', padx=10)

                #creating label for adress section
                address_label = tk.Label(self, text="Address:")
                address_label.pack(anchor='w', padx=10)
                street_label=tk.Label(self, text="Street Address:")
                street_label.pack(anchor='w', padx=10)
                street_entry = tk.Entry(self)
                street_entry.pack(anchor='w', padx=10)

                asu_label=tk.Label(self, text="Apt/Suite/Unit")
                asu_label.pack(anchor='w', padx=10)
                asu_entry = tk.Entry(self)
                asu_entry.pack(anchor='w', padx=10)

                city_label=tk.Label(self, text="City")
                city_label.pack(anchor='w', padx=10)
                city_entry =tk.Entry(self)
                city_entry.pack(anchor='w', padx=10)

                Province_label = tk.Label(self, text="Province")
                Province_label.pack(anchor='w', padx=10)
                Province_entry = tk.Entry(self)
                Province_entry.pack(anchor='w', padx=10)

                Postcode_label = tk.Label(self, text="Postal Code")
                Postcode_label.pack(anchor='w', padx=10)
                Postcode_entry = tk.Entry(self)
                Postcode_entry.pack(anchor='w', padx=10)

                birth_label = tk.Label(self, text="Date of Birth:")
                birth_label.pack(anchor='w', padx=10)
                birthday_label = tk.Label(self, text="dd/mm/yyyy")
                birthday_label.pack(anchor='w', padx=10)
                birthday_entry = tk.Entry(self)
                birthday_entry.pack(anchor='w', padx=10)

                #creating gender options through var (allowing toggle box/select through button)
                gender_label = tk.Label(self, text="Gender:")
                gender_label.pack(anchor='w', padx=10)
                gender_var = tk.StringVar()
                male_radio = tk.Radiobutton(self, text="Male", variable=gender_var, value="Male")
                male_radio.pack(anchor='w', padx=10, side="left")
                female_radio = tk.Radiobutton(self, text="Female", variable=gender_var, value="Female")
                female_radio.pack(anchor='w', padx=10, side="left")
                other_radio = tk.Radiobutton(self, text="Other", variable=gender_var, value="Other")
                other_radio.pack(anchor='w', padx=10, side="left")




        button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
        button.pack(side="left", padx=5, pady=5)

        button = tk.Button(self, text="Go to Page 3", command=lambda: controller.show_frame(Page3))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_frame(Page4))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 5", command=lambda: controller.show_frame(Page5))
        button.pack(side="left", padx=5, pady=5)


        button = tk.Button(self, text="Submit", width=10, command=lambda: entries(Page1, Page2))
        button.pack()


        def entries(self):
        #getting all of the data in the first page
            first_n = firstn_entry.get()
            middle_n = middlen_entry.get()
            last_n = lastn_entry.get()
            preffered_n = prefferedn_entry.get()
            address_n = street_entry.get()
            asu_n = asu_entry.get()
            city_n = city_entry.get()
            province_n = Province_entry.get()
            postal_n = Postcode_entry.get()
            birth_n = birthday_entry.get()
            gender_n = gender_var.get()

            print("First Name:", first_n)
            print("Middle Name:", middle_n)
            print("Last Name:", last_n)
            print("Preferred Name:", preffered_n)
            print("Gender:", gender_n)
            print("Birthday:", birth_n)
            print("Postal Code:", postal_n)

            conn = sqlite3.connect("clinicform.db") #created a different file for the table bc i was havign trouble seeing entries being updated in the other file/table there..
            cursor = conn.cursor()

            #creating table for pateint information, we can create other tables for other sections to reduce data redundancy
            table_query = '''CREATE TABLE IF NOT EXISTS patient_info (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    first_name TEXT,
                                    middle_name TEXT,
                                    last_name TEXT,
                                    preferred_name TEXT,
                                    gender TEXT,
                                    birthday INT,
                                    postal_code TEXT
                                )'''
            conn.execute(table_query)



            data_insert_que = '''INSERT INTO patient_info (first_name, middle_name, last_name, preferred_name, gender, birthday,postal_code)
                                     VALUES (?, ?, ?, ?, ?, ?,?)'''
            data_insert_tup = (first_n, middle_n, last_n, preffered_n, gender_n, birth_n,postal_n)

            cursor = conn.cursor()
            cursor.execute(data_insert_que, data_insert_tup)
            conn.commit()
            conn.close()


class Page2(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text= "Clinic Form 2")


        label.pack(padx=10,pady=10)
        d_columns = ["Contact Information",]
        healthcard_label = tk.Label(self, text="Health Card Number (enter 10 digits)", anchor='w')
        healthcard_label.pack(fill='x')

        healthcard_entry = tk.Entry(self)
        healthcard_entry.pack(anchor='w', padx=10)

        for column in d_columns:
            if column=="Health Card Number":
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')

                healthcard_entry = tk.Entry(self)
                healthcard_entry.pack(anchor='w', padx=10)


            if column == "Contact Information": #phone, home, work,,email
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')

                Cell_label = tk.Label(self, text="Phone #")
                Cell_label.pack(anchor='w', padx=10)
                Cell_entry = tk.Entry(self)
                Cell_entry.pack(anchor='w', padx=10)

                home_label = tk.Label(self, text="Home #")
                home_label.pack(anchor='w', padx=10)
                home_entry = tk.Entry(self)
                home_entry.pack(anchor='w', padx=10)

                work_label = tk.Label(self, text="Work #")
                work_label.pack(anchor='w', padx=10)
                work_entry = tk.Entry(self)
                work_entry.pack(anchor='w', padx=10)

                email_label = tk.Label(self, text="Email")
                email_label.pack(anchor='w', padx=10)
                email_entry = tk.Entry(self)
                email_entry.pack(anchor='w', padx=10)

                #emergency contact label and entry form
                emergencycon_label = tk.Label(self, text="Emergency Contact:")
                emergencycon_label.pack(anchor="w", padx=10)
                firstn_label = tk.Label(self, text="First Name")
                firstn_label.pack(anchor='w', padx=10)
                firstn_entry = tk.Entry(self)
                firstn_entry.pack(anchor='w', padx=10)

                middlen_label = tk.Label(self, text="Middle Name")
                middlen_label.pack(anchor='w', padx=10)
                middlen_entry = tk.Entry(self)
                middlen_entry.pack(anchor='w', padx=10)

                lastn_label = tk.Label(self, text="Last Name")
                lastn_label.pack(anchor='w', padx=10)
                lastn_entry = tk.Entry(self)
                lastn_entry.pack(anchor='w', padx=10)

                Cellr_label = tk.Label(self, text="Phone #")
                Cellr_label.pack(anchor='w', padx=10)
                Cellr_entry = tk.Entry(self)
                Cellr_entry.pack(anchor='w', padx=10)

                Relationship_label = tk.Label(self, text="Relationship with Patient:")
                Relationship_label.pack(anchor='w', padx=10)
                Relationship_entry = tk.Entry(self)
                Relationship_entry.pack(anchor='w', padx=10)

                pg_label = tk.Label(self, text="Parent/Guardian:")
                pg_label.pack(anchor="w", padx=10)
                firstn_label = tk.Label(self, text="First Name")
                firstn_label.pack(anchor='w', padx=10)
                firstn_entry = tk.Entry(self)
                firstn_entry.pack(anchor='w', padx=10)

                middlen_label = tk.Label(self, text="Middle Name")
                middlen_label.pack(anchor='w', padx=10)
                middlen_entry = tk.Entry(self)
                middlen_entry.pack(anchor='w', padx=10)


            else:
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')

                tk.Label(self, text="", height=1).pack()

            def entries_pt2():
                health_card = healthcard_entry.get()
                cell_phone = Cell_entry.get()
                email = email_entry.get()
                emergency_contact_phone = Cellr_entry.get()

                print("Health Card:", health_card)
                print("Phone #:", cell_phone)
                print("Email:", email)
                print("Emergency Contact #:", emergency_contact_phone)

                conn = sqlite3.connect("clinicform.db")
                cursor = conn.cursor()

                cursor.execute('''CREATE TABLE IF NOT EXISTS contact_info (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        health_card_number TEXT,
                                        cell_phone TEXT,
                                        email TEXT,
                                        emergency_contact_phone TEXT
                                    )''')
                conn.commit()

                data_insert_que = '''INSERT INTO contact_info (
                                        health_card_number, cell_phone, email, emergency_contact_phone
                                    ) VALUES (?, ?, ?, ?)'''
                data_insert_tup = (health_card, cell_phone, email, emergency_contact_phone)

                cursor.execute(data_insert_que, data_insert_tup)
                conn.commit()
                conn.close()


        button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_frame(Page1))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 3", command=lambda: controller.show_frame(Page3))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_frame(Page4))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 5", command=lambda: controller.show_frame(Page5))
        button.pack(side="left", padx=5, pady=5)
        submit_button = tk.Button(self, text="Submit", width=10, command=entries_pt2)
        submit_button.pack()

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "Clinic Form 3")
        label.pack(padx=10, pady=10)
        d_columns = [ "Occupation", "Employer", "Martial Status"]

        pg_label = tk.Label(self, text="Parent/Guardian Information Continued:")
        pg_label.pack(anchor="w", padx=10)
        lastn_label = tk.Label(self, text="Last Name")
        lastn_label.pack(anchor='w', padx=10)
        lastn_entry = tk.Entry(self)
        lastn_entry.pack(anchor='w', padx=10)
        Cellr_label = tk.Label(self, text="Phone #")
        Cellr_label.pack(anchor='w', padx=10)
        Cellr_entry = tk.Entry(self)
        Cellr_entry.pack(anchor='w', padx=10)

        email_label = tk.Label(self, text="Email")
        email_label.pack(anchor='w', padx=10)
        email_entry = tk.Entry(self)
        email_entry.pack(anchor='w', padx=10)

        Relationship_label = tk.Label(self, text="Relationship with Patient:")
        Relationship_label.pack(anchor='w', padx=10)
        Relationship_entry = tk.Entry(self)
        Relationship_entry.pack(anchor='w', padx=10)

        patientjob_label = tk.Label(self, text="Patient Occupation Status:")
        patientjob_label.pack(anchor="w", padx=10)

        for column in d_columns:

            if column == "Occupation":
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')
                occu_entry = tk.Entry(self)
                occu_entry.pack(anchor='w', padx=10)

            elif column=="Employer":
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')
                emp_entry = tk.Entry(self)
                emp_entry.pack(anchor='w', padx=10)

            elif column=="Martial Status":
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')

                self.marital_status = tk.StringVar()
                marital_status_combobox = ttk.Combobox(self, textvariable=self.marital_status, values=["Select", "Single", "Married", "Divorced", "Widowed"])
                marital_status_combobox.pack(anchor='w', padx=10)
                marital_status_combobox.current(0)

                self.spouse_frame = tk.Frame(self)
                self.spouse_frame.pack(anchor='w', padx=10)

                self.spouse_name_label = tk.Label(self.spouse_frame, text="Spouse Name:")
                self.spouse_name_label.pack()

                self.spouse_first_name_label = tk.Label(self.spouse_frame, text="First:")
                self.spouse_first_name_label.pack()
                self.spouse_first_name_entry = tk.Entry(self.spouse_frame)
                self.spouse_first_name_entry.pack()

                self.spouse_middle_name_label = tk.Label(self.spouse_frame, text="Middle:")
                self.spouse_middle_name_label.pack()
                self.spouse_middle_name_entry = tk.Entry(self.spouse_frame)
                self.spouse_middle_name_entry.pack()

                self.spouse_last_name_label = tk.Label(self.spouse_frame, text="Last:")
                self.spouse_last_name_label.pack()
                self.spouse_last_name_entry = tk.Entry(self.spouse_frame)
                self.spouse_last_name_entry.pack()
                self.spouse_frame.pack_forget()
                self.marital_status.trace("w", self.show_hide_spouse)

        button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_frame(Page1))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_frame(Page4))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 5", command=lambda: controller.show_frame(Page5))
        button.pack(side="left", padx=5, pady=5)

    def show_hide_spouse(self, *args):
        self.spouse_frame.pack_forget()
        if self.marital_status.get() == "Married":
            self.spouse_frame.pack()
            #this allows to only  show spouse information if married is selected from marital status section



class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "Clinic Form 4")
        label.pack(padx=10, pady=10)
        d_columns = [  "Medical Details", "Insurance Information"]


        for column in d_columns:

            if column == "Medical Details":
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')

                medicaldetails_label = tk.Label(self, text="Height:")
                medicaldetails_label.pack(anchor="w", padx=10)

                medicaldetails_entry = tk.Entry(self, width=10,)
                medicaldetails_entry.pack(anchor="w", padx=10)

                medicaldetails_label = tk.Label(self, text="Weight:")
                medicaldetails_label.pack(anchor="w", padx=10)
                medicaldetails_entry = tk.Entry(self, width=10,)
                medicaldetails_entry.pack(anchor="w", padx=10)

                medicaldetails_label = tk.Label(self, text="Current Medications (seperate by , if more than one):")
                medicaldetails_label.pack(anchor="w", padx=10)
                medicaldetails_entry = tk.Entry(self)
                medicaldetails_entry.pack(anchor="w", padx=10)

                medicaldetails_label = tk.Label(self, text="Allergies:medical/general (seperate by , if more than one):")
                medicaldetails_label.pack(anchor="w", padx=10)
                medicaldetails_entry = tk.Entry(self)
                medicaldetails_entry.pack(anchor="w", padx=10)


                medicaldetails_label = tk.Label(self, text="Relevant Medical History (seperate by , if more than one):")
                medicaldetails_label.pack(anchor="w", padx=10)
                medicaldetails_entry = tk.Entry(self)
                medicaldetails_entry.pack(anchor="w", padx=10)

                # labels for insurance information
                insuranceinfo_label = tk.Label(self, text="Insurance Information:")
                insuranceinfo_label.pack(anchor="w", padx=10)

                primaryins_label=tk.Label(self, text="Primary Insurance:")
                primaryins_label.pack(anchor="w", padx=10)
                primaryins_entry = tk.Entry(self)
                primaryins_entry.pack(anchor="w", padx=10)

                subpol_label = tk.Label(self, text="The patient is a Subscriber/Policy Holder")
                subpol_label.pack(anchor="w", padx=10)

                self.subscriber_policy_holder_var = tk.StringVar()
                self.subscriber_policy_holder_var.set("None")
                subscriber_policy_holder_yes_checkbutton= tk.Radiobutton(self, text="Yes", variable=self.subscriber_policy_holder_var, value="Yes")
                subscriber_policy_holder_yes_checkbutton.pack(anchor="w", padx=10)
                subscriber_policy_holder_no_checkbutton= tk.Radiobutton(self, text="No", variable=self.subscriber_policy_holder_var, value="No")
                subscriber_policy_holder_no_checkbutton.pack(anchor="w", padx=10)

                secondaryins_label=tk.Label(self, text="Secondary Insurance:")
                secondaryins_label.pack(anchor="w", padx=10)
                secondaryins_entry = tk.Entry(self)
                secondaryins_entry.pack(anchor="w", padx=10)

                subpol_label = tk.Label(self, text="The patient is a Subscriber/Policy Holder")
                subpol_label.pack(anchor="w", padx=10)

                self.subscriber_policy_holder_var = tk.StringVar()
                self.subscriber_policy_holder_var.set("None")
                subscriber_policy_holder_yes_checkbutton= tk.Radiobutton(self, text="Yes", variable=self.subscriber_policy_holder_var, value="Yes")
                subscriber_policy_holder_yes_checkbutton.pack(anchor="w", padx=10)
                subscriber_policy_holder_no_checkbutton= tk.Radiobutton(self, text="No", variable=self.subscriber_policy_holder_var, value="No")
                subscriber_policy_holder_no_checkbutton.pack(anchor="w", padx=10)

                ifotherinsurance_label = tk.Label(self, text="Insurance Information (if other than patient)")
                ifotherinsurance_label.pack(anchor="w", padx=10)
                subs_label=tk.Label(self, text="Subscriber/Policy Holder")
                subs_label.pack(anchor="w", padx=10)
                subs_entry = tk.Entry(self)
                subs_entry.pack(anchor="w", padx=10)

                relation_label=tk.Label(self, text="Relatonship with Patient")
                relation_label.pack(anchor="w", padx=10)
                relation_entry = tk.Entry(self)
                relation_entry.pack(anchor="w", padx=10)

        button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_frame(Page1))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 3", command=lambda: controller.show_frame(Page3))
        button.pack(side="left", padx=5, pady=5)
        button = tk.Button(self, text="Go to Page 5", command=lambda: controller.show_frame(Page5))
        button.pack(side="left", padx=5, pady=5)


class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "Clinic Form 5")
        label.pack(padx=10, pady=10)
        d_columns = [ "Billing Information"]


        for column in d_columns:
            if column == "Billing Information":
                billing_label = tk.Label(self, text="Billing Information:")
                billing_label.pack(anchor="w", padx=10)
                self.billing_toggle_var = tk.IntVar(value=0)
                billing_toggle_checkbox = tk.Checkbutton(self, text="Same as Address in Page 1",variable=self.billing_toggle_var)
                billing_toggle_checkbox.pack(anchor='w', padx=10)

                country_label = tk.Label(self, text="Country")
                country_label.pack(anchor='w', padx=10)
                country_entry = tk.Entry(self)
                country_entry.pack(anchor='w', padx=10)

                Postcode_label = tk.Label(self, text="Postal Code")
                Postcode_label.pack(anchor='w', padx=10)
                Postcode_entry = tk.Entry(self)
                Postcode_entry.pack(anchor='w', padx=10)

                button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_frame(Page1))
                button.pack(side="left", padx=5, pady=5)
                button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
                button.pack(side="left", padx=5, pady=5)
                button = tk.Button(self, text="Go to Page 3", command=lambda: controller.show_frame(Page3))
                button.pack(side="left", padx=5, pady=5)
                button = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_frame(Page4))
                button.pack(side="left", padx=5, pady=5)



tk = Clinic_Forum()
tk.mainloop()


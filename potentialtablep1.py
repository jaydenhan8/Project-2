# note:this python file is only for page 1 and linking it to sql database, speifically for patient INFORMATION
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


        button = tk.Button(self, text="Submit", width=10, command=lambda: entries(Page1))
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



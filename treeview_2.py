from tkinter import ttk
import tkinter as tk

class Clinic_Forum(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("640x480")

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
        button.pack(side="bottom")

        button = tk.Button(self, text="Go to Page 3", command=lambda: controller.show_frame(Page3))
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_frame(Page4))
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 5", command=lambda: controller.show_frame(Page5))
        button.pack(side="bottom")

        #tree.insert(parent="", 0, text="Title", values=())


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

        button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_frame(Page1))
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 3", command=lambda: controller.show_frame(Page3))
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_frame(Page4))
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 5", command=lambda: controller.show_frame(Page5))
        button.pack(side="bottom")

class Page3(tk.Frame): #
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "Clinic Form 3")
        label.pack(padx=10, pady=10)
        d_columns = [ "Occupation", "Employer", "Martial Status"] #still have to do these


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

        button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_frame(Page1))
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 4", command=lambda: controller.show_frame(Page4))
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 5", command=lambda: controller.show_frame(Page5))
        button.pack(side="bottom")



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

                #medical details with larger entry box
                medicaldetails_label = tk.Label(self, text="Height:")
                medicaldetails_label.pack(anchor="w", padx=10)

                medicaldetails_entry = tk.Entry(self, width=10,)
                medicaldetails_entry.pack(anchor="w", padx=10)

                medicaldetails_label = tk.Label(self, text="Weight:")
                medicaldetails_label.pack(anchor="w", padx=10)
                medicaldetails_entry = tk.Entry(self, width=10,)
                medicaldetails_entry.pack(anchor="w", padx=10)

                medicaldetails_label = tk.Label(self, text="Current Medications:")
                medicaldetails_label.pack(anchor="w", padx=10)
                medicaldetails_entry = tk.Entry(self)
                medicaldetails_entry.pack(anchor="w", padx=10)
                medicaldetails_entry = tk.Entry(self)
                medicaldetails_entry.pack(anchor="w", padx=10)



                medicaldetails_label = tk.Label(self, text="Allergies (medical/general):")
                medicaldetails_label.pack(anchor="w", padx=10)
                medicaldetails_entry = tk.Entry(self)
                medicaldetails_entry.pack(anchor="w", padx=10)
                medicaldetails_entry = tk.Entry(self)
                medicaldetails_entry.pack(anchor="w", padx=10)

                medicaldetails_label = tk.Label(self, text="Relevant Medical History:")
                medicaldetails_label.pack(anchor="w", padx=10)
                medicaldetails_entry = tk.Entry(self)
                medicaldetails_entry.pack(anchor="w", padx=10)

                # labels for insurance information
                # Primary Insurance: The patient is a Subscriber/Policy Holder:
                # Y/N Secondary Insurance: The patient is a Subscriber/Policy Holder: Y/N
                insuranceinfo_label = tk.Label(self, text="Insurance Information:")
                insuranceinfo_label.pack(anchor="w", padx=10)

                secondaryins_label=tk.Label(self, text="Secondary Insurance:")
                secondaryins_label.pack(anchor="w", padx=10)
                secondaryins_entry = tk.Entry(self)
                secondaryins_entry.pack(anchor="w", padx=10)

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
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 3", command=lambda: controller.show_frame(Page3))
        button.pack(side="bottom")
        button = tk.Button(self, text="Go to Page 5", command=lambda: controller.show_frame(Page5))
        button.pack(side="bottom")


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
                billing_toggle_checkbox = tk.Checkbutton(self, text="Same as Address in Page 1",
                                                         variable=self.billing_toggle_var)
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
                button.pack(side="bottom")
                button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
                button.pack(side="bottom")
                button = tk.Button(self, text="Go to Page 3", command=lambda: controller.show_frame(Page3))
                button.pack(side="bottom")


tk = Clinic_Forum()
tk.mainloop()

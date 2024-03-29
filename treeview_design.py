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

        for F in (Page1, Page2):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(Page1)


    def show_frame(self,cont):

        frame = self.frames[cont]

        frame.tkraise()

class Page1(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Clinic Form 1")
        label.pack(pady=10,padx=10)

        c_columns = ["Patient Information", "Billing Information", "Insurance Information", "Insured Information (if other than patient"]
            #for loop for iterating all of the columns
        #creating specific for loops for each section of the form
        for column in c_columns:
            if column == "Patient Information":
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')

                #creating label for "name" section
                name_label = tk.Label(self, text="Name:")
                name_label.pack(anchor='w', padx=10)

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

                #create entries for adress section here:

            elif column == "Billing Information":
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')

                #add labels + entries for billing info here

            else:
                label = tk.Label(self, text=column, anchor='w')
                label.pack(fill='x')

                tk.Label(self, text="", height=1).pack()  # adding space between the labels/columns for design purposes/organization

        button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
        button.pack(side="bottom") #changed position of the button

        #tree.insert(parent="", 0, text="Title", values=())


class Page2(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text= "Clinic Form 2")

        label.pack(padx=10,pady=10)
        d_columns = ["Emergency Contact", "Parent/Guardian", "Medical Details"]

        for column in d_columns:
            label = tk.Label(self, text=column, anchor='w')
            label.pack(fill='x')

            tk.Label(self, text="", height=1).pack()

        button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_frame(Page1))
        button.pack(side="bottom")



tk = Clinic_Forum()
tk.mainloop()


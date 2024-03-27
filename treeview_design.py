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

        tree = ttk.Treeview(self, selectmode="browse", columns=c_columns)

        tree.pack(fill="x")

        for i in c_columns:
            #for loop for iterating all of the columns

            tree.heading(column=f'{i}',text=f'{i}',anchor='w')
            tree.column(column=f'{i}', width=150, minwidth=50)

        #tree.insert(parent="", 0, text="Title", values=())








        button = tk.Button(self, text = "Go to Page 2", command = lambda: controller.show_frame(Page2))
        button.pack()



class Page2(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text= "Clinic Form 2")

        label.pack(padx=10,pady=10)
        d_columns = ["Emergency Contact", "Parent/Guardian", "Medical Details"]

        tree = ttk.Treeview(self, selectmode="browse", columns=d_columns)

        tree.pack(fill="x")


        for i in d_columns:
            tree.heading(column=f'{i}', text=f'{i}', anchor='w')
            tree.column(column=f'{i}', width=150, minwidth=50)

        button = tk.Button(self, text = "Go to Page 1", command = lambda: controller.show_frame(Page1))
        button.pack()






tk = Clinic_Forum()
tk.mainloop()


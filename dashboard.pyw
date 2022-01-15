from tkinter import *

from oop.spanisch import Vokabeltrainer


class Dashboard:
    woerterbuch = Vokabeltrainer()

    def __init__(self):
        self.fenster = Tk()
        self.ausgabe = Label(self.fenster, width=20, height=2)

        self.lbl_spanisch = Label(self.fenster, text="Spanisch:")
        self.lbl_deutsch = Label(self.fenster, text="Deutsch:")
        self.spanisch = Entry(self.fenster)
        self.deutsch = Entry(self.fenster)



        # Buttons
        self.select_data = Button(self.fenster, text='Select', command=self.sel)
        self.insert_data = Button(self.fenster, text='Insert Into', command=self.ins)
        self.update_data = Button(self.fenster, text='Update', command=self.upd)
        self.delete_data = Button(self.fenster, text='Delete', command=self.dele)

        self.lbl_spanisch.pack()
        self.spanisch.pack(padx=10, pady=10)

        self.lbl_deutsch.pack()
        self.deutsch.pack(pady=10)

        self.select_data.pack(pady=10)
        self.insert_data.pack(pady=10)
        self.update_data.pack(pady=10)
        self.delete_data.pack(pady=10)


        self.ausgabe.pack()
        self.fenster.mainloop()

    def sel(self):
        self.woerterbuch.select_data() # Note: prints it out on the console
        # ToDo: Tabelle in der GUI implementieren für Ausgabe
    def ins(self):
        self.woerterbuch.insert_data() #Note: needs parameter
        #ToDo: retrieve textbox values and  hand them over to the function as parameters
    def upd(self):
        self.woerterbuch.update_data() #Missing input parameters
    def dele(self):
        self.woerterbuch.delete_data() #Missing input parameters
gui = Dashboard()
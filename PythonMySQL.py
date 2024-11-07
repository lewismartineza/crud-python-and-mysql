# CRUD file creation and use of functions to interact with the database.

# Imports.
import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Clients import *
from Connection import *


class FormClient:

  # Global variables.
  global base
  base = None

  global textBoxId
  textBoxId = None

  global textBoxName
  textBoxName = None

  global textBoxLastName
  textBoxLastName = None

  global combo
  combo = None

  global groupBox
  groupBox = None

  global tree
  tree = None

# Function of the CRUD parts.
def Form():
    global base
    global textBoxId
    global textBoxName
    global textBoxLastName
    global combo
    global groupBox
    global tree

    try:
        base = Tk()
        base.geometry("1200x300")
        base.title("Form Python")

        # Group for fields to enter customer information and buttons to add, update and delete.
        groupBox = LabelFrame(base,text="Data Client", padx=5, pady=5)
        groupBox.grid(row=0,column=0,padx=10,pady=10)

        labelId = Label(groupBox,text="Id:",width=13,font=("arial",8)).grid(row=0,column=0)
        textBoxId = Entry(groupBox)
        textBoxId.grid(row=0,column=1)

        labelName = Label(groupBox,text="Name:",width=13,font=("arial",8)).grid(row=1,column=0)
        textBoxName = Entry(groupBox)
        textBoxName.grid(row=1,column=1)

        labelLastName = Label(groupBox,text="LastName:",width=13,font=("arial",8)).grid(row=2,column=0)
        textBoxLastName = Entry(groupBox)
        textBoxLastName.grid(row=2,column=1)

        labelGender = Label(groupBox,text="Gender:",width=13,font=("arial",8)).grid(row=3,column=0)
        select = tk.StringVar()
        combo = ttk.Combobox(groupBox,values=["Male","Female"],textvariable=select)
        combo.grid(row=3,column=1)
        select.set("Male")

        # CRUD buttons.
        
        # Button and function call to update user information in the database.
        Button(groupBox,text="Edit",width=10,command=updateRecords).grid(row=4,column=1)

        # Button and function call to delete user information from the database.
        Button(groupBox,text="Delete",width=10,command=deleteRecords).grid(row=4,column=2)

        # Button and function call to save new users in the database.
        Button(groupBox,text="Save",width=10,command=saveRecords).grid(row=4,column=0)

        # Group that allows visibility of current customers in the database with immediate updates.
        groupBox = LabelFrame(base,text="Client List",padx=5,pady=5,)
        groupBox.grid(row=0,column=1,padx=5,pady=5)

        tree = ttk.Treeview(groupBox,columns=("Id","Name","LastName","Gender"),show="headings",height=5)
        tree.column("#1",anchor=CENTER)
        tree.heading('# 1', text="Id")

        tree.column("#2",anchor=CENTER)
        tree.heading('# 2', text="Name")

        tree.column("#3",anchor=CENTER)
        tree.heading('# 3', text="LastName")

        tree.column("#4",anchor=CENTER)
        tree.heading('# 4', text="Gender")

        for row in CClients.showClients():
            tree.insert("","end",values=row)


        tree.bind("<<TreeviewSelect>>", selectRecord)

        tree.pack()


        base.mainloop()
    # Shows in console if there is an error when executing the function.
    except ValueError as error:
        print("Error to watch the interfaz, error: {}".format(error))

# Function that allows to save customers in the database from the CRUD.
def saveRecords():

    global textBoxName,textBoxLastName,combo,groupBox

    try:
        # Cycle that validates if the global variables were initialized.
        if textBoxName is None or textBoxLastName is None or combo is None:
            print("The widgets it isn't initialized")
            return

        # Declaration and initialization of the variables that will store the new customer information and send it to the database.
        firstname = textBoxName.get()
        lastname = textBoxLastName.get()
        gender = combo.get()

        # Send to the function that will be in charge of storing the information of the new client entered in the database.
        CClients.enterClients(firstname,lastname,gender)
        messagebox.showinfo("Information","STORED DATA")

        # Call to the function that updates the customer table in the CRUD immediately.
        UpdateTreeView()

        # Cleaning of the information fields.
        textBoxName.delete(0,END)
        textBoxLastName.delete(0,END)

    # Shows in console if there is an error when executing the function.
    except ValueError as error:
        print("Error to save the records, error: {}".format(error))

# Function that updates the CRUD table when a customer is saved, updated or deleted.
def UpdateTreeView():
    global tree

    try:
        tree.delete(*tree.get_children())

        data = CClients.showClients()

        for row in data:
            tree.insert("","end",values=row)

    # Shows in console if there is an error when executing the function.
    except ValueError as error:
        print("Error to update table, error: {}".format(error))

# Function that is in charge of selecting in the CRUD table the customer that you want to update or delete from the database.
def selectRecord(event):

    try:
        itemSelected = tree.focus()

        if itemSelected:
            values = tree.item(itemSelected)['values']

            textBoxId.delete(0, END)
            textBoxId.insert(0, values[0])

            textBoxName.delete(0, END)
            textBoxName.insert(0, values[1])

            textBoxLastName.delete(0, END)
            textBoxLastName.insert(0, values[2])

            combo.set(values[3])

    # Shows in console if there is an error when executing the function.
    except ValueError as error:
        print("Error to select record, error: {}".format(error))

# Function that allows updating customer information in the database from the CRUD.
def updateRecords():

    global textBoxId,textBoxName,textBoxLastName,combo,groupBox

    try:
        # Cycle that validates if the global variables were initialized.
        if textBoxId is None or textBoxName is None or textBoxLastName is None or combo is None:
            print("The widgets it isn't initialized")
            return

        # Declaration and initialization of the variables that will update the client's information and send it to the database.
        idUser = textBoxId.get()
        firstname = textBoxName.get()
        lastname = textBoxLastName.get()
        gender = combo.get()

        # Send to the function that will be responsible for updating the customer information in the database.
        CClients.updateClients(idUser,firstname,lastname,gender)
        messagebox.showinfo("Information","UPDATE DATA")

        # Call to the function that updates the customer table in the CRUD immediately.
        UpdateTreeView()

        # Cleaning of the information fields.
        textBoxId.delete(0,END)
        textBoxName.delete(0,END)
        textBoxLastName.delete(0,END)

    # Shows in console if there is an error when executing the function.
    except ValueError as error:
        print("Error to update records, error: {}".format(error))

# Function that allows to remove clients from the database from the CRUD.
def deleteRecords():

    global textBoxId,textBoxName,textBoxLastName

    try:
        # Cycle that validates if the global variables were initialized.
        if textBoxId is None:
            print("The widget it isn't initialized")
            return

        # Declaration and initialization of the variable that will delete the customer using the customer ID and delete it from the CRUD table and the database.
        idUser = textBoxId.get()

        # Send to the function that will remove the customer's information from the database.
        CClients.deleteClients(idUser)
        messagebox.showinfo("Information","DELETE DATA")

        # Call to the function that updates the customer table in the CRUD immediately.
        UpdateTreeView()

        # Cleaning of the information fields.
        textBoxId.delete(0,END)
        textBoxName.delete(0,END)
        textBoxLastName.delete(0,END)

    # Shows in console if there is an error when executing the function.
    except ValueError as error:
        print("Error to delete records, error: {}".format(error))


Form()
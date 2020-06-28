# user_interface.py
# basic menus and decision-making around what user wants to do
import tkinter
from tkinter import Toplevel
from app.update_files import update_etp
from app.update_files import update_asset
from app.update_files import update_liability
from app.update_files import delete_etp
from app.update_files import delete_liability
from app.update_files import delete_asset
import os
from tkinter.ttk import *
import pandas as pd 

from app import etp_update

#asset_class = "Equity"
#identifier = "GOOG"
#units = 10
#purchase_price = 100#

##update_ETP(asset_class, identifier, units, purchase_price)#

#delete_etp(identifier)

asset_class = "Real Estate"
identifier = "Hamptons"
purchase_price = 600000
current_value = 850000

#update_asset(asset_class, identifier, current_value)
#delete_asset(identifier)


#THIS CODE WORKS TO DISPLAY TABLE!
#etp_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
#df = pd.read_csv(etp_filepath)
#
#
#from tkinter import * 
#
#
#
#root = Tk() 
#
#t1 = Text(root) 
#t1.pack() 
#
#class PrintToT1(object): 
# def write(self, s): 
#     t1.insert(END, s) 
#
#sys.stdout = PrintToT1() 
#
#print ('Hello, world!') 
#print (df)
icon_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "16-168200_dollar-sign-image-money-clip-art-black-small.gif")
#clipart sourced from http://clipart-library.com/clipart/dollar-cliparts_9.htm

def update_button_click():
    x = 1

def open_new_window(window_name):
    new_window =Toplevel(master)
    new_window.title("Edit Data")

    # sets the geometry of toplevel
    #newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    #Label(newWindow,text="This is a new window").pack()
    tkinter.Label(new_window, text="Which portfolio do you want to edit?", width=30, height=10).pack()

    update_radio_label = tkinter.Label(new_window,text="Please select one of the following options:")


    update_radio_value = tkinter.StringVar()
    my_radio_x = tkinter.Radiobutton(new_window,
        text="Exchange Traded Products", value="X", variable=update_radio_value)
    my_radio_y = tkinter.Radiobutton(new_window,
        text="Other Assets", value="Y", variable=update_radio_value)
    my_radio_z = tkinter.Radiobutton(new_window,
        text="Liabilities", value="Z", variable=update_radio_value)
    
    update_button = tkinter.Button(new_window, text="OK", command=update_button_click)

    update_radio_label.pack()
    my_radio_x.pack()
    my_radio_y.pack()
    my_radio_z.pack()
    update_button.pack(side="bottom")

# iniitalise GUI
master = tkinter.Tk()
icon = tkinter.PhotoImage(file=icon_filepath)
label = Label(master, image=icon, width=20)
master.title("Main Menu")
my_message = tkinter.Message(text='''Portfolio Performance & Reporting System v1.0 \n
                Copyright Justin Davda 2020 \n''', width=1000)


# ENTRY (TEXT INPUT) WITH LABEL

#my_label = tkinter.Label(text="Input something here:")
#entry_value = tkinter.StringVar()
#my_entry = tkinter.Entry(textvariable=entry_value)

# RADIO BUTTONS

my_radio_label = tkinter.Label(
    text="Please select one of the following options:")
my_radio_value = tkinter.StringVar()
my_radio_a = tkinter.Radiobutton(
    text="View Asset Allocation & New Worth", value="A", variable=my_radio_value)
my_radio_b = tkinter.Radiobutton(
    text="Refresh Market Prices", value="B", variable=my_radio_value)
my_radio_c = tkinter.Radiobutton(
    text="Update Assets & Liabilities", value="C", variable=my_radio_value)
#my_radio_d = tkinter.Radiobutton(
#       text="Exit Program", value="D", variable=my_radio_value)
# CHECKBUTTONS

#my_checkbox_group_label = tkinter.Label(
#    text="Please check one or more of the following boxes:")
#my_checkbox_a_val = tkinter.StringVar()
#my_checkbox_a = tkinter.Checkbutton(text="Box A", variable=my_checkbox_a_val)
#my_checkbox_b_val = tkinter.StringVar()
#my_checkbox_b = tkinter.Checkbutton(text="Box B", variable=my_checkbox_b_val)
#my_checkbox_c_val = tkinter.StringVar()
#my_checkbox_c = tkinter.Checkbutton(text="Box C", variable=my_checkbox_c_val)
#
## LISTBOX (DROPDOWN SELECT)
#
#my_select_label = tkinter.Label(
#    text="Please select an item from the dropdown:")
#my_select = tkinter.Listbox()
#my_select.insert(1, "First Item")
#my_select.insert(2, "Second Item")
#my_select.insert(3, "Third Item")
#my_select.insert(4, "Fourth Item")
#my_select.insert(5, "Fifth Item")
#my_select.insert(6, "Sixth Item")

# BUTTON


def handle_button_click():
    #print("------------------------------")
    #print("NICE. YOU CLICKED THE BUTTON")
    ##print("THE ENTRY'S INPUT VALUE IS:", my_entry.get())
    #print("THE SELECTED RADIO BUTTON'S VALUE IS:", my_radio_value.get())
    if my_radio_value.get() == "A":
        etp_update()
        

    elif my_radio_value.get() == "B":
        x = 1
    elif my_radio_value.get() == "C":
        window_name = "C"
        open_new_window(window_name)
    #print("THE CHECKBOX ON/OFF VALUES FOR A, B, C, RESPECTIVELY, ARE:",
    #      [my_checkbox_a_val.get(), my_checkbox_b_val.get(), my_checkbox_c_val.get()])
    #print("THE SELECTED DROPDOWN ITEM IS:",
    #      my_select.get(my_select.curselection()))
    
def exit_button_click():
    exit()

my_button = tkinter.Button(text="OK", command=handle_button_click)
exit_button = tkinter.Button(text="Exit", command=exit_button_click)
#
# BIND THE INDIVIDUAL COMPONENTS TO THE GUI WINDOW (PACK)
# ... THEN LAUNCH THE GUI WINDOW (MAINLOOP)
#

my_message.pack()
label.pack(pady = 10)
#my_label.pack()
#my_entry.pack()

my_radio_label.pack()
my_radio_a.pack()
my_radio_b.pack()
my_radio_c.pack()

#my_checkbox_group_label.pack()
#my_checkbox_a.pack()
#my_checkbox_b.pack()
#my_checkbox_c.pack()
#
#my_select_label.pack()
#my_select.pack()
#
exit_button.pack(side="bottom")
my_button.pack(side="bottom")

#
master.mainloop()

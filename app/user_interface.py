# user_interface.py
# basic menus and decision-making around what user wants to do

import tkinter
from app.update_files import update_etp
from app.update_files import update_asset
from app.update_files import update_liability
from app.update_files import delete_etp
from app.update_files import delete_liability
from app.update_files import delete_asset
import os
import tkinter

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


# iniitalise GUI
window = tkinter.Tk()

my_message = tkinter.Message(text="Hi. Welcome to my Example GUI Application!", width=1000)
my_message = tkinter.Message(text="Hi. Welcome to my Example GUI Application!", width=1000)


# ENTRY (TEXT INPUT) WITH LABEL

my_label = tkinter.Label(text="Input something here:")
entry_value = tkinter.StringVar()
my_entry = tkinter.Entry(textvariable=entry_value)

# RADIO BUTTONS

my_radio_label = tkinter.Label(
    text="Please selection one of the following options:")
my_radio_value = tkinter.StringVar()
my_radio_a = tkinter.Radiobutton(
    text="Option A", value="A", variable=my_radio_value)
my_radio_b = tkinter.Radiobutton(
    text="Option B", value="B", variable=my_radio_value)
my_radio_c = tkinter.Radiobutton(
    text="Option C", value="C", variable=my_radio_value)

# CHECKBUTTONS

my_checkbox_group_label = tkinter.Label(
    text="Please check one or more of the following boxes:")
my_checkbox_a_val = tkinter.StringVar()
my_checkbox_a = tkinter.Checkbutton(text="Box A", variable=my_checkbox_a_val)
my_checkbox_b_val = tkinter.StringVar()
my_checkbox_b = tkinter.Checkbutton(text="Box B", variable=my_checkbox_b_val)
my_checkbox_c_val = tkinter.StringVar()
my_checkbox_c = tkinter.Checkbutton(text="Box C", variable=my_checkbox_c_val)

# LISTBOX (DROPDOWN SELECT)

my_select_label = tkinter.Label(
    text="Please select an item from the dropdown:")
my_select = tkinter.Listbox()
my_select.insert(1, "First Item")
my_select.insert(2, "Second Item")
my_select.insert(3, "Third Item")
my_select.insert(4, "Fourth Item")
my_select.insert(5, "Fifth Item")
my_select.insert(6, "Sixth Item")

# BUTTON


def handle_button_click():
    print("------------------------------")
    print("NICE. YOU CLICKED THE BUTTON")
    print("THE ENTRY'S INPUT VALUE IS:", my_entry.get())
    print("THE SELECTED RADIO BUTTON'S VALUE IS:", my_radio_value.get())
    print("THE CHECKBOX ON/OFF VALUES FOR A, B, C, RESPECTIVELY, ARE:",
          [my_checkbox_a_val.get(), my_checkbox_b_val.get(), my_checkbox_c_val.get()])
    print("THE SELECTED DROPDOWN ITEM IS:",
          my_select.get(my_select.curselection()))


my_button = tkinter.Button(text="Click Me", command=handle_button_click)

#
# BIND THE INDIVIDUAL COMPONENTS TO THE GUI WINDOW (PACK)
# ... THEN LAUNCH THE GUI WINDOW (MAINLOOP)
#

my_message.pack()

my_label.pack()
my_entry.pack()

my_radio_label.pack()
my_radio_a.pack()
my_radio_b.pack()
my_radio_b.pack()

my_checkbox_group_label.pack()
my_checkbox_a.pack()
my_checkbox_b.pack()
my_checkbox_c.pack()

my_select_label.pack()
my_select.pack()

my_button.pack()

window.mainloop()

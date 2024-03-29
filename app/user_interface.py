# user_interface.py
# basic menus and decision-making around what user wants to do
import tkinter
from tkinter import *
from tkinter import messagebox
from app.update_files import update_etp
from app.update_files import update_asset
from app.update_files import update_liability
from app.update_files import delete_etp
from app.update_files import delete_liability
from app.update_files import delete_asset
import os
from tkinter.ttk import *
import pandas as pd 

from app.etp_update import update_etps
from app.create_report import report_create

icon_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "16-168200_dollar-sign-image-money-clip-art-black-small.gif")

#clipart sourced from http://clipart-library.com/clipart/dollar-cliparts_9.htm
#help with df printing in tkinter from https://stackoverflow.com/questions/26629695/how-to-display-content-of-pandas-data-frame-in-tkinter-gui-window
# other tkinter assistance (passing information from forms to functions) from: https://github.com/th679/Recipe-lookup/blob/master/app/recipe-search.py

#window for editing etps
def open_etp_window():

    def update_etp_df():
        etp_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
        df = pd.read_csv(etp_filepath)
        print (df)

    etp_window =Toplevel(master)
    etp_window.title("Exchange Traded Products")
    etp_message = tkinter.Message(etp_window, text='''                                                                               Add, edit or delete records:\n
    Enter all fields and a NEW identifier to ADD a new record.  Enter all fields and an EXISTING identifier in order to AMEND a row,
                                                                                    or just the identifier to DELETE \n''', width=700)
    etp_message.pack(side="top")
    
    #get user input  #asset_class,identifier,units,purchase_price
    
    #asset class
    asset_label = tkinter.Label(etp_window, text="Asset Class:")
    asset_entry_value = tkinter.StringVar()
    asset_entry = tkinter.Entry(etp_window, textvariable=asset_entry_value)
    asset_label.pack()
    asset_entry.pack()
    
    #identifier
    id_label = tkinter.Label(etp_window, text="Identifier:")
    id_entry_value = tkinter.StringVar()
    id_entry = tkinter.Entry(etp_window, textvariable=id_entry_value)
    id_label.pack()
    id_entry.pack()

    #units
    units_label = tkinter.Label(etp_window, text="Units:")
    units_entry_value = tkinter.StringVar()
    units_entry = tkinter.Entry(etp_window, textvariable=units_entry_value)
    units_label.pack()
    units_entry.pack()

    #purchase price
    purchase_label = tkinter.Label(etp_window, text="Purchase Price:")
    purchase_entry_value = tkinter.StringVar()
    purchase_entry = tkinter.Entry(etp_window, textvariable=purchase_entry_value)
    purchase_label.pack()
    purchase_entry.pack()

    def add_etp_button_click():
        asset_input = asset_entry.get()
        id_input = id_entry.get()
        units_input = units_entry.get()
        purchase_input = purchase_entry.get()
        update_etp(asset_input, id_input, units_input, purchase_input)
        update_etp_df()

    add_etp_button = tkinter.Button(etp_window,text="Add/Amend", command=add_etp_button_click)
    add_etp_button.pack()

    def del_etp_button_click():
        id_input = id_entry.get()
        delete_etp(id_input)
        update_etp_df()   

    del_button = tkinter.Button(etp_window,text="Delete", command=del_etp_button_click)
    del_button.pack()

    def exit_etp_button_click():
        etp_window.destroy()  

    exit_etp_button = tkinter.Button(etp_window,text="Close", command=exit_etp_button_click)
    exit_etp_button.pack()

    #show current file
    tkinter.Label(etp_window, text="\n Exchange Traded Product Holdings").pack()
    etp_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "exchange_traded_products.csv")
    df = pd.read_csv(etp_filepath)
    
    t1 = Text(etp_window) 
    t1.pack() 
    
    class PrintToT1(object): 
     def write(self, s): 
         t1.insert(END, s) 
    sys.stdout = PrintToT1()
    print (df)




#window for editing other assets
def open_asset_window():

    def update_asset_df():
        asset_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "other_assets.csv")
        df = pd.read_csv(asset_filepath)
        print(df)

    asset_window = Toplevel(master)
    asset_window.title("Other Assets")
    asset_message = tkinter.Message(asset_window, text='''                                                                               Add, edit or delete records:\n
    Enter all fields and a NEW identifier to ADD a new record.  Enter all fields and an EXISTING identifier in order to AMEND a row,
                                                                                    or just the identifier to DELETE \n''', width=700)
    asset_message.pack(side="top")

    #get user input  #asset_class,identifier,current_value

    #asset class
    asset_label = tkinter.Label(asset_window, text="Asset Class:")
    asset_entry_value = tkinter.StringVar()
    asset_entry = tkinter.Entry(asset_window, textvariable=asset_entry_value)
    asset_label.pack()
    asset_entry.pack()

    #identifier
    id_label = tkinter.Label(asset_window, text="Identifier:")
    id_entry_value = tkinter.StringVar()
    id_entry = tkinter.Entry(asset_window, textvariable=id_entry_value)
    id_label.pack()
    id_entry.pack()

    #current value
    value_label = tkinter.Label(asset_window, text="Current Value:")
    value_entry_value = tkinter.StringVar()
    value_entry = tkinter.Entry(asset_window, textvariable=value_entry_value)
    value_label.pack()
    value_entry.pack()

    def add_asset_button_click():
        value_input = value_entry.get()
        id_input = id_entry.get()
        asset_input = asset_entry.get()
        
        update_asset(asset_input, id_input, value_input)
        update_asset_df()

    add_asset_button = tkinter.Button(asset_window, text="Add/Amend", command=add_asset_button_click)
    add_asset_button.pack()

    def del_asset_button_click():
        id_input = id_entry.get()
        delete_asset(id_input)
        update_asset_df()

    del_button = tkinter.Button(asset_window, text="Delete", command=del_asset_button_click)
    del_button.pack()

    def exit_asset_button_click():
        asset_window.destroy()

    exit_asset_button = tkinter.Button(asset_window, text="Close", command=exit_asset_button_click)
    exit_asset_button.pack()

    #show current file
    
    tkinter.Label(asset_window, text="\n Other Assets").pack()
    asset_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "other_assets.csv")
    df = pd.read_csv(asset_filepath)
    t1 = Text(asset_window)
    t1.pack()
    class PrintToT1(object):
     def write(self, s):
         t1.insert(END, s)
    sys.stdout = PrintToT1()
    print(df)


#window for editing liabilities 
def open_liab_window():

    def update_liab_df():
        liab_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "liabilities.csv")
        df = pd.read_csv(liab_filepath)
        print(df)

    liab_window = Toplevel(master)
    liab_window.title("Liabilities")
    liab_message = tkinter.Message(liab_window, text='''                                                                                       Add, edit or delete records:\n
    Enter all fields and a NEW identifier to ADD a new record.  Enter all fields and an EXISTING identifier in order to AMEND a row,
                                                                                   or just the identifier to DELETE \n''', width=700)
    liab_message.pack(side="top")

    #get user input  #asset_class, identifier, current_value

    #asset class
    asset_label = tkinter.Label(liab_window, text="Asset Class:")
    asset_entry_value = tkinter.StringVar()
    asset_entry = tkinter.Entry(liab_window, textvariable=asset_entry_value)
    asset_label.pack()
    asset_entry.pack()

    #identifier
    id_label = tkinter.Label(liab_window, text="Identifier:")
    id_entry_value = tkinter.StringVar()
    id_entry = tkinter.Entry(liab_window, textvariable=id_entry_value)
    id_label.pack()
    id_entry.pack()

    #current value
    value_label = tkinter.Label(liab_window, text="Current Value:")
    value_entry_value = tkinter.StringVar()
    value_entry = tkinter.Entry(liab_window, textvariable=value_entry_value)
    value_label.pack()
    value_entry.pack()

    def add_liab_button_click():
        asset_input = asset_entry.get()
        id_input = id_entry.get()
        value_input = value_entry.get()

        update_liability(asset_input, id_input, value_input)
        update_liab_df()

    add_liab_button = tkinter.Button(liab_window, text="Add/Amend", command=add_liab_button_click)
    add_liab_button.pack()

    def del_liab_button_click():
        id_input = id_entry.get()
        delete_liability(id_input)
        update_liab_df()

    del_button = tkinter.Button(liab_window, text="Delete", command=del_liab_button_click)
    del_button.pack()

    def exit_liab_button_click():
        liab_window.destroy()

    exit_liab_button = tkinter.Button(liab_window, text="Close", command=exit_liab_button_click)
    exit_liab_button.pack()

    #show current file
    tkinter.Label(liab_window, text="\n Liabilities").pack()
    liab_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "liabilities.csv")
    df = pd.read_csv(liab_filepath)

    t1 = Text(liab_window)
    t1.pack()

    class PrintToT1(object):
     def write(self, s):
         t1.insert(END, s)
    sys.stdout = PrintToT1()
    print(df)




#window for selecting what to edit
def open_new_window():
    new_window =Toplevel(master)
    new_window.title("Data Management")
    icon = tkinter.PhotoImage(file=icon_filepath)
    new_label = Label(new_window, image=icon, width=20)

    #select options + open new windows

    tkinter.Label(new_window, text="Which portfolio do you want to review?").pack()
    new_label.pack(pady=10,side="top")
    update_radio_label = tkinter.Label(new_window,text="Please select one of the following options:")
    update_radio_value = tkinter.StringVar(new_window)
    my_radio_x = tkinter.Radiobutton(new_window,
        text="Exchange Traded Products", value="X", variable=update_radio_value)
    my_radio_y = tkinter.Radiobutton(new_window,
        text="Other Assets", value="Y", variable=update_radio_value)
    my_radio_z = tkinter.Radiobutton(new_window,
        text="Liabilities", value="Z", variable=update_radio_value)
        
    def update_button_click():
        
        if update_radio_value.get() == "X":
            open_etp_window()
    
        elif update_radio_value.get() == "Y":
            open_asset_window()
  
        elif update_radio_value.get() == "Z":
            open_liab_window()

    update_button = tkinter.Button(new_window, text="OK", command=update_button_click)
    
    update_radio_label.pack()
    my_radio_x.pack()
    my_radio_y.pack()
    my_radio_z.pack()
    update_button.pack()
    
    def exit_edit_button_click():
        new_window.destroy()  

    exit_edit_button = tkinter.Button(new_window,text="Exit", command=exit_edit_button_click)
    exit_edit_button.pack()



# Main Window

master = tkinter.Tk()
icon = tkinter.PhotoImage(file=icon_filepath)
label = Label(master, image=icon, width=20)
master.title("Main Menu")

my_message = tkinter.Message(text='''Financial Health Toolkit v1.0''', width=1000, font='bold')
my_message_2 = tkinter.Message(text='''Copyright Justin Davda 2020 \n \n''', width = 1000)

# RADIO BUTTON SELECTION
my_radio_label = tkinter.Label(
    text='''Please select one of the following options: \n''', font='underline')
my_radio_value = tkinter.StringVar()
my_radio_a = tkinter.Radiobutton(
    text="Data Visualisation:   View Asset Allocation + Net Worth", value="A", variable=my_radio_value)
my_radio_b = tkinter.Radiobutton(
    text="Market Monitoring:   Screen Portfolio for Unusual Price Moves  ", value="B", variable=my_radio_value)
my_radio_c = tkinter.Radiobutton(
    text='''Data Management: View + Edit Portfolio''', value="C", variable=my_radio_value)

# BUTTONS
def handle_button_click():
    if my_radio_value.get() == "A":
        messagebox.showinfo("Please check your browser", "Two charts will be displayed: please close the first browser window to see the second one!")
        report_create()
              

    elif my_radio_value.get() == "B":
        messagebox.showinfo("Please Be Patient", "This step may take a while:  Tickers refresh at a rate of 5per minute - please be patient if you have a long list to process!")
        update_etps()
        messagebox.showinfo("Prices Refreshed + Market Moves Analysed", "Please check your email for details of any alerts triggered!")
        

    elif my_radio_value.get() == "C":
        window_name = "C"
        open_new_window()
    
    
def exit_button_click():
    exit()

my_button = tkinter.Button(text="OK", command=handle_button_click)
exit_button = tkinter.Button(text="Exit", command=exit_button_click)

#pack main window

my_message.pack()
my_message_2.pack()
label.pack(pady = 10)

my_radio_label.pack()
my_radio_a.pack()
my_radio_b.pack()
my_radio_c.pack()

exit_button.pack(side="bottom")
my_button.pack(side="bottom")

# launch infinite loop for main window
master.mainloop()

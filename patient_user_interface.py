import sqlite3
from tkinter import *


global password, username, age, date_of_birth, aadhar_card_number, last_name


def sign_up():

    def submit():
        global password, username, age, date_of_birth, aadhar_card_number, last_name

        first_name = first_name_entry_box.get()
        last_name = last_name_entry_box.get()
        date_of_birth = date_of_birth_entry_box.get()
        age = age_entry_box.get()
        aadhar_card_number = aadhar_card_number_entry_box.get()

        conn = sqlite3.connect("Patient.db")

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO Patient VALUES (:first_name, :last_name, :date_of_birth, :age, :aadhar_card_number)",
            {"first_name": first_name, "last_name": last_name, "date_of_birth": date_of_birth, "age": age,
             "aadhar_card_number": aadhar_card_number})

        conn.commit()

        conn.close()

    root = Toplevel()
    root.attributes("-fullscreen", True)

    # First Name
    first_name_label = Label(root, text="First Name")
    first_name_label.place(relx=0.15, rely=0.2)

    first_name_entry_box = Entry(root)
    first_name_entry_box.place(relx=0.25, rely=0.2)

    # Last Name
    last_name_label = Label(root, text="Last Name")
    last_name_label.place(relx=0.65, rely=0.2)

    last_name_entry_box = Entry(root)
    last_name_entry_box.place(relx=0.75, rely=0.2)

    # Date of Birth
    date_of_birth_label = Label(root, text="Date of Birth")
    date_of_birth_label.place(relx=0.15, rely=0.4)

    date_of_birth_entry_box = Entry(root)
    date_of_birth_entry_box.place(relx=0.25, rely=0.4)

    # Age
    age_label = Label(root, text="Age")
    age_label.place(relx=0.65, rely=0.4)

    age_entry_box = Entry(root)
    age_entry_box.place(relx=0.75, rely=0.4)

    # Aadhar Card Number
    aadhar_card_number_label = Label(root, text="Aadhar-Card Number")
    aadhar_card_number_label.place(relx=0.15, rely=0.6)

    aadhar_card_number_entry_box = Entry(root)
    aadhar_card_number_entry_box.place(relx=0.25, rely=0.6)

    # Submit Button
    submit_button = Button(root, text="Submit", command=lambda: [submit(), root.destroy()])
    submit_button.place(relx=0.5, rely=0.8)

    root.mainloop()


def login():
    win = Tk()
    win.attributes("-fullscreen", True)

    id_label = Label(win, text="ID")
    id_label.place(relx=0.4, rely=0.4)

    id_entry_box = Entry(win)
    id_entry_box.place(relx=0.5, rely=0.4)

    password_label = Label(win, text="Password")
    password_label.place(relx=0.4, rely=0.6)

    password_entry_box = Entry(win)
    password_entry_box.place(relx=0.5, rely=0.6)

    win.mainloop()


window = Tk()
window.attributes("-fullscreen", True)

login_button = Button(window, text="Login", font=("Agency FB", 26), command=lambda: [login()])
login_button.place(relx=0.4, rely=0.5)

sign_up_button = Button(window, text="Sign Up", font=("Agency FB", 26), command=lambda: [sign_up()])
sign_up_button.place(rely=0.5, relx=0.5)

quit_button = Button(window, text="Quit", font=("Agency FB", 26), command=quit)
quit_button.place(relx=0.5, rely=0.7)

window.mainloop()

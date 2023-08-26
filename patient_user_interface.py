import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

global password, username, age, date_of_birth, aadhar_card_number, last_name, first_name


# [('U', 'S', '12/08/2022', 1, 102938475638, '123')]


def sign_up():
    def submit():
        global password, username, age, date_of_birth, aadhar_card_number, last_name, first_name

        first_name = first_name_entry_box.get()
        last_name = last_name_entry_box.get()
        date_of_birth = date_of_birth_entry_box.get()
        age = age_entry_box.get()
        aadhar_card_number = aadhar_card_number_entry_box.get()
        password = password_entry_box.get()

        conn = sqlite3.connect("Patient.db")

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO Patient VALUES (:first_name, :last_name, :date_of_birth, :age, :aadhar_card_number, :password)",
            {"first_name": first_name, "last_name": last_name, "date_of_birth": date_of_birth, "age": age,
             "aadhar_card_number": aadhar_card_number, "password": password})

        cursor.execute("SELECT * FROM Patient")

        print(cursor.fetchall())

        conn.commit()

        conn.close()

        messagebox.showwarning("oyee", "hiiii")
        root.destroy()

    root = Toplevel()
    root.attributes("-fullscreen", True)
    root.config(bg="light green")

    # First Name
    first_name_label = Label(root, text="First Name",font="Cambria 24 bold",bg="light green")
    first_name_label.place(relx=0.14, rely=0.2)

    first_name_entry_box = Entry(root)
    first_name_entry_box.place(relx=0.27, rely=0.22)

    # Last Name
    last_name_label = Label(root, text="Last Name",font="Cambria 24 bold",bg="light green")
    last_name_label.place(relx=0.65, rely=0.2)

    last_name_entry_box = Entry(root)
    last_name_entry_box.place(relx=0.79, rely=0.22)

    # Date of Birth
    date_of_birth_label = Label(root, text="Date of Birth",font="Cambria 24 bold",bg="light green")
    date_of_birth_label.place(relx=0.12, rely=0.4)

    date_of_birth_entry_box = Entry(root)
    date_of_birth_entry_box.place(relx=0.3, rely=0.41)

    # Age
    age_label = Label(root, text="Age",font="Cambria 24 bold",bg="light green")
    age_label.place(relx=0.65, rely=0.4)

    age_entry_box = Entry(root)
    age_entry_box.place(relx=0.72, rely=0.42)

    # Aadhar Card Number
    aadhar_card_number_label = Label(root, text="Aadhar-Card Number",font="Cambria 24 bold",bg="light green")
    aadhar_card_number_label.place(relx=0.15, rely=0.6)

    aadhar_card_number_entry_box = Entry(root)
    aadhar_card_number_entry_box.place(relx=0.19, rely=0.66)

    # Password
    password_label = Label(root, text="Password",font="Cambria 24 bold",bg="light green")
    password_label.place(relx=0.65, rely=0.6)

    password_entry_box = Entry(root, show='*')
    password_entry_box.place(relx=0.69, rely=0.66)

    # Submit Button
    submit_button = Button(root, text="Submit",font="Cambria 17 bold", command=lambda: [submit(), root.destroy()])
    submit_button.place(relx=0.46, rely=0.8)

    root.mainloop()


def dashboard():
    global first_name, last_name, age, aadhar_card_number, password, date_of_birth

    win = Tk()
    win.config(bg="#111111")
    win.attributes("-fullscreen", True)

    profile_first_name_label = Label(win, text=f"First name: {first_name}")
    profile_first_name_label.place(relx=0.4, rely=0.2)

    profile_last_name_label = Label(win, text=f"Last name: {last_name}")
    profile_last_name_label.place(relx=0.4, rely=0.2)

    profile_date_of_birth_label = Label(win, text=f"Date of Birth: {date_of_birth}")
    profile_date_of_birth_label.place(relx=0.4, rely=0.4)

    profile_age_label = Label(win, text=f"Age: {age}")
    profile_age_label.place(relx=0.6, rely=0.4)

    profile_aadhar_card_number_label = Label(win, text=f"Aadhar Card Number: {aadhar_card_number}")
    profile_aadhar_card_number_label.place(relx=0.4, rely=0.6)

    profile_password_label = Label(win, text=f"Password: {password}")
    profile_password_label.place(relx=0.6, rely=0.6)

    book_appointment_button = Button(win, text='Book Appointment')
    book_appointment_button.place(relx=0.4, rely=0.8)  ## KRISH

    history_button = Button(win, text="Medical History")
    history_button.place(relx=0.6, rely=0.8)  ## KRISH

    win.mainloop()


def login():
    def enter():
        conn = sqlite3.connect("Patient.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT password FROM Patient WHERE aadhar_card_number = '{id_entry_box.get()}'")

        if cursor.fetchall() == []:
            messagebox.showwarning("WARNING", "Your username or password is wong")
        else:
            dashboard()

    win = Tk()
    win.attributes("-fullscreen", True)

    id_label = Label(win, text="ID",font="Cambria 14 bold")
    id_label.place(relx=0.4, rely=0.4)

    id_entry_box = Entry(win)
    id_entry_box.place(relx=0.5, rely=0.4)

    password_label = Label(win, text="Password",font="Cambria 17 bold")
    password_label.place(relx=0.4, rely=0.6)

    password_entry_box = Entry(win)
    password_entry_box.place(relx=0.5, rely=0.6)

    enter_button = Button(win, text="Enter", command=enter,font="Cambria 15 bold")
    enter_button.place(relx=0.5, rely=0.8)

    win.mainloop()


window = Tk()
img = PhotoImage(file="doctor.png")
label = Label(window,image=img)
label.place(x=0, y=0)
window.attributes("-fullscreen", True)

login_button = Button(window, text="Login", font=("Agency FB", 26), command=lambda: [login()])
login_button.place(relx=0.7, rely=0.33)

sign_up_button = Button(window, text="Sign Up", font=("Agency FB", 26), command=lambda: [sign_up()])
sign_up_button.place(rely=0.49, relx=0.7)

quit_button = Button(window, text="Quit", font=("Agency FB", 26), command=quit)
quit_button.place(relx=0.7, rely=0.69)


window.mainloop()

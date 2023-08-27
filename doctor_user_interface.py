from tkinter import *
import sqlite3
import csv
import datetime


def gettime():
    return datetime.datetime.now()


def prog():
    pr1 = prescription.get(1.0, END)
    print(pr1)
    with open("prescription.txt", "a") as op:
        op.write(str([str(gettime())]) + ": " + pr1 + "\n")
    print("successfully written")


conn = sqlite3.connect("Patient.db")
cursor = conn.cursor()
cursor.execute("SELECT aadhar_card_number FROM Patient")
id = cursor.fetchone()
cursor.execute(f"SELECT * FROM Patient WHERE aadhar_card_number = '{id[0]}'")
database_input = cursor.fetchone()
# cursor.execute(f"DELETE FROM Patient WHERE aadhar_card_number = '{id[0]}'")
conn.commit()
conn.close()

conn2 = sqlite3.connect("Symptoms.db")
cursor2 = conn2.cursor()
cursor2.execute(f"SELECT symptoms FROM Symptoms WHERE userid = '{id[0]}'")
data = cursor2.fetchall()
conn2.commit()
conn2.close()

print(data)
filename = open("Patient_histroy.csv", "w")
w = csv.writer(filename)
w.writerow(database_input)

window = Tk()

name_label = Label(window, text="Name: " + str(database_input[0]) + " " + str(database_input[1]))
name_label.pack()

user_id_label = Label(window, text="User ID: " + str(database_input[4]))
user_id_label.pack()

symptoms_label = Label(window, text='Symptoms: ' + str(data))
symptoms_label.pack()

prescription = Text(window)
prescription.pack(side=BOTTOM)

sub_but = Button(window, text="SUBMIT", font="broadway 12 bold", command=prog)
sub_but.place(relx=0.42, rely=0.87)

window.mainloop()

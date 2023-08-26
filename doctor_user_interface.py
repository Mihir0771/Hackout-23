from tkinter import *
import sqlite3
import csv


conn = sqlite3.connect("Patient.db")
cursor = conn.cursor()
cursor.execute("SELECT aadhar_card_number FROM Patient")
id = cursor.fetchone()
cursor.execute(f"SELECT * FROM Patient WHERE aadhar_card_number = '{id[0]}'")
database_input = cursor.fetchone()
cursor.execute(f"DELETE FROM Patient WHERE aadhar_card_number = '{id[0]}'")
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



window.mainloop()
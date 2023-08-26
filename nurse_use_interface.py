from tkinter import *
import sqlite3
# [(102938475638, "5'11", '58.2', '120-80', '27', 'Cold')]

def send():
    conn = sqlite3.connect("Symptoms.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO Symptoms VALUES (:userid, :height, :weight, :blood_pressure, :temp, :symptoms)",
                   {"userid": userid_entry_box.get(), "height": height_entry_box.get(),
                    "weight": weight_entry_box.get(),
                    "blood_pressure": blood_pressure_entry_box.get(), "temp": temp_entry_box.get(),
                    "symptoms": symptoms_entry_box.get(),
                    "send_button": symptoms_entry_box.get()})

    cursor.execute("SELECT * FROM Symptoms")

    print(cursor.fetchall())

    conn.commit()

    conn.close()


nroot = Tk()
nroot.attributes("-fullscreen", True)
nroot.config(bg="#111111")

userid_label = Label(nroot, text="User ID",font="Verdana 17")
userid_label.place(relx=0.2, rely=0.2)

userid_entry_box = Entry(nroot,font="Verdana 11")
userid_entry_box.place(relx=0.28, rely=0.21)

height = Label(nroot, text="Height",font="Verdana 17")
height.place(relx=0.57, rely=0.19)

height_entry_box = Entry(nroot,font="Verdana 11")
height_entry_box.place(relx=0.64, rely=0.2)

weight = Label(nroot, text="Weight",font="Verdana 17")
weight.place(relx=0.21, rely=0.4)

weight_entry_box = Entry(nroot,font="Verdana 11")
weight_entry_box.place(relx=0.29, rely=0.41)

blood_pressure = Label(nroot, text="Blood pressure",font="Verdana 17")
blood_pressure.place(relx=0.54, rely=0.4)

blood_pressure_entry_box = Entry(nroot,font="Verdana 11")
blood_pressure_entry_box.place(relx=0.69, rely=0.41)

temp = Label(nroot, text="Temperature",font="Verdana 17")
temp.place(relx=0.19, rely=0.6)

temp_entry_box = Entry(nroot,font="Verdana 11")
temp_entry_box.place(relx=0.32, rely=0.61)

symptoms = Label(nroot, text="Symptoms",font="Verdana 17")
symptoms.place(relx=0.58, rely=0.6)

symptoms_entry_box = Entry(nroot,font="Verdana 11")
symptoms_entry_box.place(relx=0.69, rely=0.61)

send_button = Button(nroot, text="Send to the doctor",font="Verdana 14 bold", command=lambda: [send(), nroot.destroy()])
send_button.place(relx=0.37, rely=0.84)

quit_button = Button(nroot, text="Quit",font="Verdana 14 bold", command=quit)
quit_button.place(relx=0.59, rely=0.84)

nroot.mainloop()

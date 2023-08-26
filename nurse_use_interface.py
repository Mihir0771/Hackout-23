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

userid_label = Label(nroot, text="User ID")
userid_label.place(relx=0.3, rely=0.2)

userid_entry_box = Entry(nroot)
userid_entry_box.place(relx=0.4, rely=0.2)

height = Label(nroot, text="Height")
height.place(relx=0.6, rely=0.2)

height_entry_box = Entry(nroot)
height_entry_box.place(relx=0.7, rely=0.2)

weight = Label(nroot, text="Weight")
weight.place(relx=0.3, rely=0.4)

weight_entry_box = Entry(nroot)
weight_entry_box.place(relx=0.4, rely=0.4)

blood_pressure = Label(nroot, text="Blood pressure")
blood_pressure.place(relx=0.6, rely=0.4)

blood_pressure_entry_box = Entry(nroot)
blood_pressure_entry_box.place(relx=0.7, rely=0.4)

temp = Label(nroot, text="Temperature")
temp.place(relx=0.3, rely=0.6)

temp_entry_box = Entry(nroot)
temp_entry_box.place(relx=0.4, rely=0.6)

symptoms = Label(nroot, text="Symptoms")
symptoms.place(relx=0.6, rely=0.6)

symptoms_entry_box = Entry(nroot)
symptoms_entry_box.place(relx=0.7, rely=0.6)

send_button = Button(nroot, text="Send to the doctor", command=lambda: [send(), nroot.destroy()])
send_button.place(relx=0.4, rely=0.9)

quit_button = Button(nroot, text="Quit", command=quit)
quit_button.place(relx=0.6, rely=0.9)

nroot.mainloop()

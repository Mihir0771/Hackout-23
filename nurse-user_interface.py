from tkinter import *


def send():
    print("ok")


def can():
    print("kyuu?")
    nroot.destroy()



nroot = Tk()
nroot.attributes("-fullscreen", True)
nroot.config(bg="#111111")

height = Label(nroot,text="Height of the Patient", font="Roboto 20")
height.place(x=130,y=200)

heightE = Entry(nroot)
heightE.place(x=130,y=200)

weight = Label(nroot,text="Weight of the Patient" ,font="Roboto 20")
weight.place(x=890,y=200)

weightE = Entry(nroot)
weightE.place(x=890,y=200)

bp = Label(nroot,text="Blood pressure of the Patient",font="Roboto 20")
bp.place(x=170,y=350)

bpE = Entry(nroot)
bpE.place(x=170,y=350)

tp = Label(nroot,text="Tempature of the Patient",font="Roboto 20")
tp.place(x=770,y=350)

tpE = Entry(nroot)
tpE.place(x=770,y=350)

sy = Label(nroot,text="Basis Symtomps of the Patient",font="Roboto 20")
sy.place(x=110,y=500)

syE = Text(nroot)
syE.place(x=100,y=550)

mh = Label(nroot,text="Medicial History of the Patient",font="Roboto 20")
mh.place(x=790,y=500)

mhE = Text(nroot)
mhE.place(x=700,y=550)

sd = Button(nroot,text="Send to the doctor",command= send)
sd.place(x=1400,y=40)

cd = Button(nroot,text="CANCEL",command= can)
cd.place(x=10,y=40)

nroot.mainloop()

def bloodpressure():
    distole=int(input("What is your distole?"))
    sistole=int(input("What is your systole?"))
    if(distole<80 and sistole<120):
        print("Low blood pressure")
        print("Maintain or adapt a healthy lifestyle")
    if(distole<80 and sistole<120 or sistole<129):
        print("Elevated blood pressure")
    if (distole<80 or distole<89 and sistole<130 or sistole<139):
        print("Stage1 high blood pressure (hypertension)")
    if (distole>90 and sistole>140):
        print("Stage2 high blood pressure (hypertension)")
bloodpressure()


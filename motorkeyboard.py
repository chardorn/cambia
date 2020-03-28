from tkinter import *

import PiMotor

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3) 
ar = PiMotor.Arrow(4)




    
class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.go = False
        self.bind('<Left>', self.A2_On)
        self.bind('<KeyRelease-Left>', self.A2_Off)
        self.pack(expand=YES, fill=BOTH)
        self.focus_force()
    def showJudgments(self, event=None):
        if self.go == False:
            self.go = True
            self.showJudgmentsA()
        else: 
            self.keepShowing()
            
    def Start(check):
        print (check)
        print("check")
    
    
    def M1Start():
        speed = float(w1.get())
        print ("Motor1 Start Running")
        print("-->Speed @ %s" % speed)
        if var1.get() == 1:
            m1.forward((speed))
        elif var1.get() == 2:
            m1.reverse(speed)
        else:
            print("M1 - Error")
            m1.stop()

    def M1Stop():
        print ("Motor1 Stop")
        m1.stop()

    def M2Start():
        speed = float(w2.get())
        print ("Motor2 Start Running")
        print("-->Speed @ %s" % speed)
        if var2.get() == 1:
            m2.forward((speed))
        elif var2.get() == 2:
            m2.reverse(speed)
        else:
            print("M2 - Error")
            m2.stop()

    def M2Stop():
        print ("Motor2 Stop")
        m2.stop()

    def M3Start():
        speed = float(w3.get())
        print ("Motor3 Start Running")
        print("-->Speed @ %s" % speed)
        if var3.get() == 1:
            m3.forward((speed))
        elif var3.get() == 2:
            m3.reverse(speed)
        else:
            print("M3 - Error")
            m3.stop()
    
    def M3Stop():
        print ("Motor3 Stop")
        m3.stop()

    def M4Start():
        speed = float(w4.get())
        print ("Motor4 Start Running")
        print("-->Speed @ %s" % speed)
        if var4.get() == 1:
            m4.forward((speed))
        elif var4.get() == 2:
            m4.reverse(speed)
        else:
            print("M4 - Error")
            m4.stop()

    def M4Stop():
        print ("Motor4 Stop")
        m4.stop()

    def A1_On():
        print ("Arrow-F ON")
        m1.stop()
        m2.stop()
        af.on()
        m1.forward(100)
        m2.forward(100)
    
    def A1_Off():
        print ("Arrow-F OFF")
        af.off()
        m1.stop()
        m2.stop()

    def A2_On():
        print ("Arrow-L ON")
        m1.stop()
        m2.stop()
        al.on()
        m1.reverse(100)
        m2.forward(100)
    
    def A2_Off():
        print ("Arrow-L OFF")
        al.off()
        m1.stop()
        m2.stop()


    def A3_On():
        print ("Arrow-R ON")
        m1.stop()

    def keepShowing(self):
        print (" key being pressed")
    def showJudgmentsA(self):
        print ("key-press started")
    def makeChoice(self, event=None):
        print ("choice made")
        self.go = False
mainw = Tk()
mainw.f = MyFrame(mainw)
mainw.f.grid()
mainw.mainloop()

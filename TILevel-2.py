# Level-2

from tkinter import *
import random
boot=Tk()
boot.geometry("1000x1000")

def restart():
    l100=Label(boot,text="")

def wrong():
    k9=Label(boot,text="The option you chose is wrong. Game over.").place(x=380,y=250)
    c11=Button(boot,text="Exit",command=boot.destroy,padx=25).place(x=400,y=275)
    c12=Button(boot,text="Restart",command=restart,padx=25).place(x=500,y=275)

def pick():
    k12=Label(boot,text=s1).place(x=380,y=330)
    c11=Button(boot,text="Exit",command=boot.destroy,padx=25).place(x=400,y=360)
    c12=Button(boot,text="Play again",command=restart,padx=25).place(x=500,y=360)
    

def correct():
    k10=Label(boot,text="Now there are three swords , first one coloured Gold , second one coloured Silver , third one coloured Platinum.").place(x=225,y=250)
    k11=Label(boot,text="The original Excalibur is only one of these. Which one do you want to choose. ").place(x=300,y=275)
    c13=Button(boot,text="Gold",padx=25,command=pick).place(x=350,y=300)
    c14=Button(boot,text="Platinum",padx=25,command=pick).place(x=450,y=300)
    c15=Button(boot,text="Silver",padx=25,command=pick).place(x=575,y=300)

def enter():
    k7=Label(boot,text="There is a huge door guarding the sword. You have to solve a math equation to unlock the door.").place(x=250,y=175)
    k8=Label(boot,text="The equation is : 20+2[5*(6-2*4)-13]").place(x=385,y=200)
    c7=Button(boot,text="143",padx=25,command=wrong).place(x=300,y=225)
    c8=Button(boot,text="183",padx=25,command=wrong).place(x=400,y=225)
    c9=Button(boot,text="153",padx=25,command=correct).place(x=500,y=225)
    c10=Button(boot,text="123",padx=25,command=wrong).place(x=600,y=225)


def leave():
    k6=Label(boot,text="You've decided to leave the cave. Game over.").place(x=380,y=175)
    c5=Button(boot,text="Exit",command=boot.destroy,padx=25).place(x=400,y=200)
    c6=Button(boot,text="Restart",command=restart,padx=25).place(x=500,y=200)

def hide():
    k5=Label(boot,text="You've reached a cave. This cave may or may not have the Excalibur. Do You want to go inside?").place(x=250,y=125)
    c3=Button(boot,text="Enter",command=enter,padx=25).place(x=400,y=150)
    c4=Button(boot,text="Leave",command=leave,padx=25).place(x=500,y=150)




def fight():
    def gold():
        if s3=="You've picked the empty door. Game over":
            k18=Label(boot,text="You've picked the wrong door. You loose!").place(x=380,y=210)
            c11=Button(boot,text="Exit",command=boot.destroy,padx=25).place(x=400,y=235)
            c12=Button(boot,text="Play again",command=restart,padx=25).place(x=500,y=235)

            
        elif s3=="You've picked the right door. You win!!!":
            k19=Label(boot,text="You've picked the right door. You win!!!").place(x=380,y=210)
            c11=Button(boot,text="Exit",command=boot.destroy,padx=25).place(x=400,y=235)
            c12=Button(boot,text="Play again",command=restart,padx=25).place(x=500,y=235)
    
    if s2=="You've lost with the demon":
        k15=Label(boot,text="You've lost with the demon. Game over").place(x=390,y=135)
        c16=Button(boot,text="Exit",padx=25,command=boot.destroy).place(x=400,y=160)
        c17=Button(boot,text="Play again",padx=25,command=restart).place(x=500,y=160)
        
    elif s2=="You've won with the Demon!!!":
        k16=Label(boot,text="You've won against the Demon!!! Now you've arrived at an alternate cave with a key and a map.").place(x=250,y=135)
        k17=Label(boot,text=" There are two doors with colours Gold and Silver. Which one do you choose?").place(x=290,y=160)
        c18=Button(boot,text="Gold",padx=25,command=gold).place(x=400,y=185)
        c19=Button(boot,text="Silver",padx=25,command=gold).place(x=500,y=185)
        
        



s1=random.choice(["You've picked the correct Excalibur!!! You win!!!","You've picked the wrong Excalibur. You loose!"])
s2=random.choice(["You've won with the Demon!!!","You've lost with the demon"])
s3=random.choice(["You've picked the empty door. Game over","You've picked the right door. You win!!!"])

k1=Label(boot,text='"Quest For Excalibur"',font="50",fg="red").pack()
k2=Label(boot,text="In this level you need to find the legendary sword Excalibur.").pack()
k3=Label(boot,text="You've walked forward and found a Demon.").pack()
k4=Label(boot,text="Do you want to fight against or hide.").pack()
c1=Button(boot,text="Hide",padx=25,command=hide).place(x=400,y=100)
c2=Button(boot,text="Fight",padx=25,command=fight).place(x=500,y=100)

boot.mainloop()

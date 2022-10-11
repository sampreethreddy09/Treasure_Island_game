import random
from tkinter import *
global main



def level2():
    
    boot=Tk()
    boot.geometry("1000x1000")
    boot.configure(bg="black")


    def wrong():
        k9=Label(boot,text="The option you chose is wrong. Game over.",fg="white",bg="black").place(x=380,y=250)
        c11=Button(boot,text="Exit",command=boot.destroy,padx=25,fg="white",bg="black").place(x=400,y=275)
        c12=Button(boot,text="Restart",command=restart,padx=25,fg="white",bg="black").place(x=500,y=275)

    def pick():
        k12=Label(boot,text=s1,fg="white",bg="black").place(x=380,y=330)
        c11=Button(boot,text="Exit",command=boot.destroy,padx=25,fg="white",bg="black").place(x=400,y=360)
        c12=Button(boot,text="Play again",command=restart,padx=25,fg="white",bg="black").place(x=500,y=360)
    
    def correct():
        k10=Label(boot,text="Now there are three swords , first one coloured Gold , second one coloured Silver , third one coloured Platinum.",fg="white",bg="black").place(x=225,y=250)
        k11=Label(boot,text="The original Excalibur is only one of these. Which one do you want to choose. ",fg="white",bg="black").place(x=300,y=275)
        c13=Button(boot,text="Gold",padx=25,command=pick,fg="white",bg="black").place(x=350,y=300)
        c14=Button(boot,text="Platinum",padx=25,command=pick,fg="white",bg="black").place(x=450,y=300)
        c15=Button(boot,text="Silver",padx=25,command=pick,fg="white",bg="black").place(x=575,y=300)

    def enter():
        k7=Label(boot,text="There is a huge door guarding the sword. You have to solve a math equation to unlock the door.",fg="white",bg="black").place(x=250,y=175)
        k8=Label(boot,text="The equation is : 20+2[5*(6-2*4)-13]",fg="white",bg="black").place(x=385,y=200)
        c7=Button(boot,text="-16",padx=25,command=wrong,fg="white",bg="black").place(x=300,y=225)
        c8=Button(boot,text="-14",padx=25,command=wrong,fg="white",bg="black").place(x=400,y=225)
        c9=Button(boot,text="-26",padx=25,command=correct,fg="white",bg="black").place(x=500,y=225)
        c10=Button(boot,text="-36",padx=25,command=wrong,fg="white",bg="black").place(x=600,y=225)

    def leave():
        k6=Label(boot,text="You've decided to leave the cave. Game over.",fg="white",bg="black").place(x=380,y=175)
        c5=Button(boot,text="Exit",command=boot.destroy,padx=25,fg="white",bg="black").place(x=400,y=200)
        c6=Button(boot,text="Restart",command=restart,padx=25,fg="white",bg="black").place(x=500,y=200)

    def hide():
        k5=Label(boot,text="You've reached a cave. This cave may or may not have the Excalibur. Do You want to go inside?",fg="white",bg="black").place(x=250,y=125)
        c3=Button(boot,text="Enter",command=enter,padx=25,fg="white",bg="black").place(x=400,y=150)
        c4=Button(boot,text="Leave",command=leave,padx=25,fg="white",bg="black").place(x=500,y=150)

    def fight():
        def gold():
            if s3=="You've picked the empty door. Game over":
                k18=Label(boot,text="You've picked the wrong door. You loose!",fg="white",bg="black").place(x=380,y=210)
                c11=Button(boot,text="Exit",command=boot.destroy,padx=25,fg="white",bg="black").place(x=400,y=235)
                c12=Button(boot,text="Play again",command=restart,padx=25,fg="white",bg="black").place(x=500,y=235)

            
            elif s3=="You've picked the right door. You win!!!":
                k19=Label(boot,text="You've picked the right door. You win!!!",fg="white",bg="black").place(x=380,y=210)
                c11=Button(boot,text="Exit",command=boot.destroy,padx=25,fg="white",bg="black").place(x=400,y=235)
                c12=Button(boot,text="Play again",command=restart,padx=25,fg="white",bg="black").place(x=500,y=235)
    
        if s2=="You've lost with the demon":
            k15=Label(boot,text="You've lost with the demon. Game over",fg="white",bg="black").place(x=390,y=135)
            c16=Button(boot,text="Exit",padx=25,command=boot.destroy,fg="white",bg="black").place(x=400,y=160)
            c17=Button(boot,text="Play again",padx=25,command=restart,fg="white",bg="black").place(x=500,y=160)
        
        elif s2=="You've won with the Demon!!!":
            k16=Label(boot,text="You've won against the Demon!!! Now you've arrived at an alternate cave with a key and a map.",fg="white",bg="black").place(x=250,y=135)
            k17=Label(boot,text=" There are two doors with colours Gold and Silver. Which one do you choose?",fg="white",bg="black").place(x=290,y=160)
            c18=Button(boot,text="Gold",padx=25,command=gold,fg="white",bg="black").place(x=400,y=185)
            c19=Button(boot,text="Silver",padx=25,command=gold,fg="white",bg="black").place(x=500,y=185)
            
    s1=random.choice(["You've picked the correct Excalibur!!! You win!!!","You've picked the wrong Excalibur. You loose!"])
    s2=random.choice(["You've won with the Demon!!!","You've lost with the demon"])
    s3=random.choice(["You've picked the empty door. Game over","You've picked the right door. You win!!!"])

    k1=Label(boot,text='"Quest For Excalibur"',font="50",fg="red",bg="black").pack()
    k2=Label(boot,text="In this level you need to find the legendary sword Excalibur.",fg="white",bg="black").pack()
    k3=Label(boot,text="You've walked forward and found a Demon.",fg="white",bg="black").pack()
    k4=Label(boot,text="Do you want to fight against or hide.",fg="white",bg="black").pack()
    c1=Button(boot,text="Hide",padx=25,command=hide,fg="white",bg="black").place(x=400,y=100)
    c2=Button(boot,text="Fight",padx=25,command=fight,fg="white",bg="black").place(x=500,y=100)

    boot.mainloop()

def main():

    root = Tk()

    def restart():
        global main
        root.destroy()
        main()
    def red():
        l8=Label(root,text=r1,fg="white",bg="black").place(x=415,y=245)
        if r1=="You found the treasure! You Win!":
            b16=Button(root,text="Play Level-2",padx=25,command=level2,fg="white",bg="black").place(x=600,y=275)
        b9=Button(root,text="Exit",command=root.destroy,padx=25,fg="white",bg="black").place(x=400,y=275)
        b14=Button(root,text="Restart",command=restart,padx=25,fg="white",bg="black").place(x=500,y=275)
    def yellow():
        l9=Label(root,text=r1,fg="white",bg="black").place(x=415,y=245)
        if r1=="You found the treasure! You Win!":
            b16=Button(root,text="Play Level-2",command=level2,padx=25,fg="white",bg="black").place(x=600,y=275)
        b10=Button(root,text="Exit",command=root.destroy,padx=25,fg="white",bg="black").place(x=400,y=275)
        b13=Button(root,text="Restart",command=restart,padx=25,fg="white",bg="black").place(x=500,y=275)
    def blue():
        l10=Label(root,text=r1,fg="white",bg="black").place(x=390,y=245)
        if r1=="You found the treasure! You Win!":
            b16=Button(root,text="Play Level-2",command=level2,padx=25,fg="white",bg="black").place(x=600,y=275)
        b11=Button(root,text="Exit",command=root.destroy,padx=25,fg="white",bg="black").place(x=400,y=275)
        b15=Button(root,text="Restart",command=restart,padx=25,fg="white",bg="black").place(x=500,y=275)

    def swim():
        l6=Label(root,text="You get attacked by an angry trout. Game Over.",fg="white",bg="black").place(x=350,y=190)
        b5=Button(root,text="Exit",command=root.destroy,padx=25,fg="white",bg="black").place(x=400,y=215)
        b12=Button(root,text="Restart",command=restart,padx=25,fg="white",bg="black").place(x=500,y=215)
    def wait():
        l7=Label(root,text="You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?",fg="white",bg="black").place(x=215,y=190)
        b6=Button(root,text="red",command=red,padx=25,fg="white",bg="black").place(x=350,y=215)
        b7=Button(root,text="Yellow",command=yellow,padx=20,fg="white",bg="black").place(x=450,y=215)
        b8=Button(root,text="Blue",command=blue,padx=25,fg="white",bg="black").place(x=550,y=215)

    def gold():
        l17=Label(root,text=r2,fg="white",bg="black").place(x=400,y=380)
        if r2=="You found the treasure! You Win!":
            b29=Button(root,text="Play Level-2",padx=25,command=level2,fg="white",bg="black").place(x=600,y=405)
        b30=Button(root,text="Exit",command=root.destroy,padx=25,fg="white",bg="black").place(x=400,y=405)
        b31=Button(root,text="Restart",command=restart,padx=25,fg="white",bg="black").place(x=500,y=405)
            
            
    def ordinary():
        l16=Label(root,text=r2,fg="white",bg="black").place(x=400,y=380)
        if r2=="You found the treasure! You Win!":
            b32=Button(root,text="Play Level-2",padx=25,command=level2,fg="white",bg="black").place(x=600,y=405)
        b33=Button(root,text="Exit",command=root.destroy,padx=25,fg="white",bg="black").place(x=400,y=405)
        b34=Button(root,text="Restart",command=restart,padx=25,fg="white",bg="black").place(x=500,y=405)

    def silence():
        l13=Label(root,text="Very Good. Now You've found two boxes in the safe.",fg="white",bg="black").place(x=390,y=285)
        l15=Label(root,text="One of the box is gold-plated and the other box is just an ordinary box.  Which one do you choose?",fg="white",bg="black").place(x=250,y=315)
        b27=Button(root,text="Gold box",command=gold,padx=25,fg="white",bg="black").place(x=400,y=345)
        b28=Button(root,text="Ordinary box",command=ordinary,padx=25,fg="white",bg="black").place(x=525,y=345)

    def ego():
        l14=Label(root,text="Wrong guess. Game Over",fg="white",bg="black").place(x=450,y=285)
        b25=Button(root,text="Exit",command=root.destroy,padx=25,fg="white",bg="black").place(x=400,y=315)
        b26=Button(root,text="Restart",command=restart,padx=25,fg="white",bg="black").place(x=500,y=315)

    def bomb():
        l10=Label(root,text="The Bomb has self-detonated. Game Over",fg="white",bg="black").place(x=375,y=190)
        b19=Button(root,text="Exit",command=root.destroy,padx=25,fg="white",bg="black").place(x=400,y=215)
        b20=Button(root,text="Restart",command=restart,padx=25,fg="white",bg="black").place(x=500,y=215)

    def sword():
        l11=Label(root,text="There's an old man near safe. Only he knows the correct pin. If you answer his riddle he'll tell you the pin ",fg="white",bg="black").place(x=250,y=190)
        l12=Label(root,text="The Riddle is :   It's so fragile that it's name can break it. What is it?",fg="white",bg="black").place(x=350,y=215)
        b21=Button(root,text="Ego",command=ego,padx=25,fg="white",bg="black").place(x=300,y=245)
        b22=Button(root,text="Silence",command=silence,padx=25,fg="white",bg="black").place(x=400,y=245)
        b23=Button(root,text="Steel",command=ego,padx=25,fg="white",bg="black").place(x=500,y=245)
        b24=Button(root,text="Francium",command=ego,padx=25,fg="white",bg="black").place(x=600,y=245)
        

    def direction():    
        if r3=="a":
            l5=Label(root,text="You've come to a lake. There is an island in the middle of the lake. Do you wanna wait for a boat or swim across the lake",fg="white",bg="black").place(x=225,y=135)
            b3=Button(root,text="Wait",command=wait,padx=25,fg="white",bg="black").place(x=400,y=160)
            b4=Button(root,text="Swim",command=swim,padx=25,fg="white",bg="black").place(x=500,y=160)

        elif r3=="b":
            l6=Label(root,text="You've found two weapons.What do you want to choose?",fg="white",bg="black").place(x=350,y=135)
            b17=Button(root,text="Bomb",command=bomb,padx=25,fg="white",bg="black").place(x=400,y=160)
            b18=Button(root,text="Sword",command=sword,padx=25,fg="white",bg="black").place(x=500,y=160)
         
    r1=random.choice(["You found the treasure! You Win!","It's a room full of fire. Game Over.","You enter a room of beasts. Game Over."])
    r2=random.choice(["You found the treasure! You Win!","It's an empty box. Game Over"])
    r3=random.choice(["a","b"])
    root.geometry('1000x1000')
    root.configure(bg="black")
    l1=Label(root,text='"Treasure Island"',font="50",fg="yellow",bg="black").pack()
    l2=Label(root,text="Welcome to Treasure Island.",fg="white",bg="black").pack()
    l3=Label(root,text="Your mission is to find the treasure.",fg="white",bg="black").pack()
    l4=Label(root,text="You're at a cross road. Where do you want to go?",fg="white",bg="black").pack()
    b1=Button(root,text="left",command=direction,padx=25,fg="white",bg="black").place(x=500,y=100)
    b2=Button(root,text="Right",command=direction,padx=25,fg="white",bg="black").place(x=400,y=100)

    root.mainloop()

main()

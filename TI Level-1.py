import random
from tkinter import *
root=Tk()

def restart():
    l100=Label(root,text="Game restarted").place(x=475,y=300)
def level2():
    l111=Label(root,text="You're playing level-2").place(x=450,y=300)

def red():
    l8=Label(root,text=r1).place(x=415,y=245)
    if r1=="You found the treasure! You Win!":
        b16=Button(root,text="Play Level-2",padx=25,command=level2).place(x=600,y=275)
    b9=Button(root,text="Exit",command=root.destroy,padx=25).place(x=400,y=275)
    b14=Button(root,text="Restart",command=restart,padx=25).place(x=500,y=275)
def yellow():
    l9=Label(root,text=r1).place(x=415,y=245)
    if r1=="You found the treasure! You Win!":
        b16=Button(root,text="Play Level-2",command=level2).place(x=600,y=275)
    b10=Button(root,text="Exit",command=root.destroy,padx=25).place(x=400,y=275)
    b13=Button(root,text="Restart",command=restart,padx=25).place(x=500,y=275)
def blue():
    l10=Label(root,text=r1).place(x=390,y=245)
    if r1=="You found the treasure! You Win!":
        b16=Button(root,text="Play Level-2",command=level2).place(x=600,y=275)
    b11=Button(root,text="Exit",command=root.destroy,padx=25).place(x=400,y=275)
    b15=Button(root,text="Restart",command=restart,padx=25).place(x=500,y=275)

def swim():
    l6=Label(root,text="You get attacked by an angry trout. Game Over.").place(x=350,y=190)
    b5=Button(root,text="Exit",command=root.destroy,padx=25).place(x=400,y=215)
    b12=Button(root,text="Restart",command=restart,padx=25).place(x=500,y=215)
def wait():
    l7=Label(root,text="You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").place(x=215,y=190)
    b6=Button(root,text="red",command=red,padx=20).place(x=400,y=215)
    b7=Button(root,text="Yellow",command=yellow,padx=20).place(x=500,y=215)
    b8=Button(root,text="Blue",command=blue,padx=20).place(x=600,y=215)


def gold():
    l17=Label(root,text=r2).place(x=400,y=380)
    if r2=="You found the treasure! You Win!":
        b29=Button(root,text="Play Level-2",padx=25,command=level2).place(x=600,y=405)
    b30=Button(root,text="Exit",command=root.destroy,padx=25).place(x=400,y=405)
    b31=Button(root,text="Restart",command=restart,padx=25).place(x=500,y=405)
        
        
def ordinary():
    l16=Label(root,text=r2).place(x=400,y=380)
    if r2=="You found the treasure! You Win!":
        b32=Button(root,text="Play Level-2",padx=25,command=level2).place(x=600,y=405)
    b33=Button(root,text="Exit",command=root.destroy,padx=25).place(x=400,y=405)
    b34=Button(root,text="Restart",command=restart,padx=25).place(x=500,y=405)

def silence():
    l13=Label(root,text="Very Good. Now You've found two boxes in the safe.").place(x=390,y=285)
    l15=Label(root,text="One of the box is gold-plated and the other box is just an ordinary box.  Which one do you choose?").place(x=250,y=315)
    b27=Button(root,text="Gold box",command=gold,padx=25).place(x=400,y=345)
    b28=Button(root,text="Ordinary box",command=ordinary,padx=25).place(x=525,y=345)

def ego():
    l14=Label(root,text="Wrong guess. Game Over").place(x=450,y=285)
    b25=Button(root,text="Exit",command=root.destroy,padx=25).place(x=400,y=315)
    b26=Button(root,text="Restart",command=restart,padx=25).place(x=500,y=315)

def bomb():
    l10=Label(root,text="The Bomb has self-detonated. Game Over").place(x=375,y=190)
    b19=Button(root,text="Exit",command=root.destroy,padx=25).place(x=400,y=215)
    b20=Button(root,text="Restart",command=restart,padx=25).place(x=500,y=215)

def sword():
    l11=Label(root,text="There's an old man near safe. Only he knows the correct pin. If you answer his riddle he'll tell you the pin ").place(x=250,y=190)
    l12=Label(root,text="The Riddle is :   It's so fragile that it's name can break it. What is it?").place(x=350,y=215)
    b21=Button(root,text="Ego",command=ego,padx=25).place(x=300,y=245)
    b22=Button(root,text="Silence",command=silence,padx=25).place(x=400,y=245)
    b23=Button(root,text="Steel",command=ego,padx=25).place(x=500,y=245)
    b24=Button(root,text="Francium",command=ego,padx=25).place(x=600,y=245)
    


def direction():    
    if r3=="a":
        l5=Label(root,text="You've come to a lake. There is an island in the middle of the lake. Do you wanna wait for a boat or swim across the lake").place(x=225,y=135)
        b3=Button(root,text="Wait",command=wait,padx=25).place(x=400,y=160)
        b4=Button(root,text="Swim",command=swim,padx=25).place(x=500,y=160)

    elif r3=="b":
        l6=Label(root,text="You've found two weapons.What do you want to choose?").place(x=350,y=135)
        b17=Button(root,text="Bomb",command=bomb,padx=25).place(x=400,y=160)
        b18=Button(root,text="Sword",command=sword,padx=25).place(x=500,y=160)
    

r1=random.choice(["You found the treasure! You Win!","It's a room full of fire. Game Over.","You enter a room of beasts. Game Over."])
r2=random.choice(["You found the treasure! You Win!","It's an empty box. Game Over"])
r3=random.choice(["a","b"])
root.geometry('1000x1000')
l1=Label(root,text="Treasure Island",font="50",fg="blue").pack()
l2=Label(root,text="Welcome to Treasure Island.",fg="black").pack()
l3=Label(root,text="Your mission is to find the treasure.",fg="black").pack()
l4=Label(root,text="You're at a cross road. Where do you want to go?",fg="black").pack()
b1=Button(root,text="left",command=direction,padx=25).place(x=400,y=100)
b2=Button(root,text="Right",command=direction,padx=25).place(x=500,y=100)

root.mainloop()

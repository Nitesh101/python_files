from Tkinter import *
import tkMessageBox
import Tkinter

top = Tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=20, \
                 width = 250)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=20, \
                 width = 250)
def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "submmited succsfully")

B = Tkinter.Button(top, text ="Submit", command = helloCallBack)

C1.pack()
C2.pack()
B.pack()
top.mainloop()

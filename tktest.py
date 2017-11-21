from tkinter import *

top = Tk()

def main():
    global lab, chk, chkvar, ent, txt
    Button(top, text="Here is a button", command=shit).pack()
    lab = Label(top, text="I am a Label", width=20)
    lab.pack()
    chkvar = IntVar()
    chk = Checkbutton(top, text='This is a Checkbutton', variable=chkvar)
    chk.pack()
    ent = Entry(top, width=25)
    ent.pack()
    txt = Text(top, width=25, height=25)
    txt.pack()
    mainloop()

def shit():
    print('Woop!')
main()

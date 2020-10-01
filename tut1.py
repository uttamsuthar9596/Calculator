# calculator using Tkinter

from tkinter import *

# create GUI window
root = Tk()
root.geometry("336x376")
root.title("Calculator")
root.minsize(336, 376)
root.maxsize(336, 376)
root.wm_iconbitmap('1.ico')

# expression variable
expr = ""

# important functions
def num_input(num):
    global expr
    expr = expr + str(num)
    scrvalue.set(expr)


def equalpress(equal):
    global expr

    try:

        global expr

        total = str(eval(expr))
        scrvalue.set(total)
        f1 = open("history.txt", "a")
        f1.write(expr)
        f1.write("=")
        f1.write(total)
        f1.write("\n")
        f1.close()
        expr = ""

    except:
        scrvalue.set("error")
        expr = ""


def clear_scr():
    global expr

    text.delete(0, END)
    expr = ""


def clear():
    global expr

    text.delete(len(scrvalue.get())-1)
    expr = text.get()


def openfile():
    f1 = open("history.txt", "r")
    print(f1.read())


def clearfile():
    f1 = open("history.txt", "r+")
    f1.truncate()
    f1.close()

# Text entry field


scrvalue = StringVar()
scrvalue.set("")
text = Entry(root, textvariable=scrvalue, font="lucida 30 ")
text.pack(fill=X, ipadx=10)

# Buttons
clear_button = Button(root, text="C", font="lucida 25", fg="green", bg="light grey", activebackground="grey", width=4, bd=1, relief=FLAT, command=clear_scr).pack(side=LEFT, anchor="nw")
divide_oper_button = Button(root, text="/", font="lucida 25", width=4, bg="light grey", activebackground="grey",bd=1, relief=FLAT, command=lambda: num_input("/")).pack(side=LEFT, anchor="nw")
multi_oper_button = Button(root, text="*", font="lucida 25", width=4, bg="light grey", activebackground="grey", bd=1, relief=FLAT, command=lambda: num_input("*")).pack(side=LEFT, anchor="nw")
back_button = Button(root, text="X", font="lucida 25", bg="light grey", activebackground="grey", width=4, bd=1, relief=FLAT, command=clear).pack(side=LEFT, anchor="nw")


button_7 = Button(root, text="7", font="lucida 25", width=4, bd=1, activebackground="light grey", relief=FLAT, command=lambda: num_input("7")).place(x=1, y=114)
button_8 = Button(root, text="8", font="lucida 25", width=4, bd=1, activebackground="light grey", relief=FLAT, command=lambda: num_input("8")).place(x=84, y=114)
button_9 = Button(root, text="9", font="lucida 25", width=4, bd=1, activebackground="light grey", relief=FLAT, command=lambda: num_input("9")).place(x=168, y=114)
add_oper_button = Button(root, text="+", font="lucida 25", bg="light grey", activebackground="grey", width=4, bd=1, relief=FLAT, command=lambda: num_input("+")).place(x=252, y=114)


button_4 = Button(root, text="4", font="lucida 25", width=4, bd=1, activebackground="light grey", relief=FLAT, command=lambda: num_input("4")).place(x=1, y=179)
button_5 = Button(root, text="5", font="lucida 25", width=4, bd=1, activebackground="light grey", relief=FLAT, command=lambda: num_input("5")).place(x=84, y=179)
button_6 = Button(root, text="6", font="lucida 25", width=4, bd=1, activebackground="light grey", relief=FLAT, command=lambda: num_input("6")).place(x=168, y=179)
sbt_button = Button(root, text="-", font="lucida 25", width=4, bg="light grey", activebackground="grey", bd=1, relief=FLAT, command=lambda: num_input("-")).place(x=252, y=179)


button_1 = Button(root, text="1", font="lucida 25", width=4, activebackground="light grey", bd=1, relief=FLAT, command=lambda: num_input("1")).place(x=1, y=244)
button_2 = Button(root, text="2", font="lucida 25", width=4, activebackground="light grey", bd=1, relief=FLAT, command=lambda: num_input("2")).place(x=84, y=244)
button_3 = Button(root, text="3", font="lucida 25", width=4, activebackground="light grey", bd=1, relief=FLAT, command=lambda: num_input("3")).place(x=168, y=244)


button_0 = Button(root, text="0", font="lucida 25", width=4, bd=1, relief=FLAT, activebackground="light grey", command=lambda: num_input("0")).place(x=1, y=310)
button_00 = Button(root, text="00", font="lucida 25", width=4, bd=1, relief=FLAT, activebackground="light grey", command=lambda: num_input("00")).place(x=84, y=310)
point_button = Button(root, text=".", font="lucida 25", width=4, bd=1, relief=FLAT, activebackground="light grey", command=lambda: num_input(".")).place(x=168, y=310)
equal_button = Button(root, text="=", font="lucida 25", width=4, height=3, bg="light grey", activebackground="grey", bd=1, relief=FLAT, command=lambda: equalpress("=")).place(x=252, y=244)

# Menu
filemenu = Menu(root)
m1 = Menu(filemenu, tearoff=0)
m1.add_command(label="open", command=openfile)
m1.add_command(label="clear history", command=clearfile)
root.config(menu=filemenu)
filemenu.add_cascade(label="History", menu=m1)

root.mainloop()

from tkinter import *
from tkinter import messagebox
from userdata import *
from HMM_score import *

kor = 0
elso = "X"
masodik = "O"

def valtas():
    global elso
    global masodik
    v = elso
    elso = masodik
    masodik = v
    kezd.config(text="Kezdő: " + elso)

# egymás utá különböző karaktert rakjon
def gomb(gomb):
    global kor
    if kor % 2 == 0:
        gomb.config(text=elso)
    else:
        gomb.config(text=masodik)
    kor += 1
    wincheck()

def wincheck():
    if gomb1.cget("text") == gomb2.cget("text") and gomb1.cget("text") == gomb3.cget("text"):
            messagebox.showinfo("Játék vége", gomb1.cget("text") + " Nyert")
            if gomb1.cget("text") == "X":
                score(user1.cget("text"), user2.cget("text"))
            else:
                score(user2.cget("text"), user1.cget("text"))
    elif gomb1.cget("text") == gomb4.cget("text") and gomb1.cget("text") == gomb7.cget("text"):
            messagebox.showinfo("Játék vége", gomb1.cget("text") + " Nyert")
            if gomb1.cget("text") == "X":
                score(user1.cget("text"), user2.cget("text"))
            else:
                score(user2.cget("text"), user1.cget("text"))
    elif gomb1.cget("text") == gomb5.cget("text") and gomb1.cget("text") == gomb9.cget("text"):
            messagebox.showinfo("Játék vége", gomb1.cget("text") + " Nyert")
            if gomb1.cget("text") == "X":
                score(user1.cget("text"), user2.cget("text"))
            else:
                score(user2.cget("text"), user1.cget("text"))
    elif gomb5.cget("text") == gomb2.cget("text") and gomb5.cget("text") == gomb8.cget("text"):
            messagebox.showinfo("Játék vége", gomb5.cget("text") + " Nyert")
            if gomb5.cget("text") == "X":
                score(user1.cget("text"), user2.cget("text"))
            else:
                score(user2.cget("text"), user1.cget("text"))
    elif gomb5.cget("text") == gomb2.cget("text") and gomb5.cget("text") == gomb6.cget("text"):
            messagebox.showinfo("Játék vége", gomb5.cget("text") + " Nyert")
            if gomb5.cget("text") == "X":
                score(user1.cget("text"), user2.cget("text"))
            else:
                score(user2.cget("text"), user1.cget("text"))
    elif gomb5.cget("text") == gomb7.cget("text") and gomb5.cget("text") == gomb3.cget("text"):
            messagebox.showinfo("Játék vége", gomb5.cget("text") + " Nyert")
            if gomb5.cget("text") == "X":
                score(user1.cget("text"), user2.cget("text"))
            else:
                score(user2.cget("text"), user1.cget("text"))
    elif gomb9.cget("text") == gomb6.cget("text") and gomb9.cget("text") == gomb3.cget("text"):
            messagebox.showinfo("Játék vége", gomb9.cget("text") + " Nyert")
            if gomb5.cget("text") == "X":
                score(user1.cget("text"), user2.cget("text"))
            else:
                score(user2.cget("text"), user1.cget("text"))
    elif gomb9.cget("text") == gomb8.cget("text") and gomb9.cget("text") == gomb7.cget("text"):
            messagebox.showinfo("Játék vége", gomb9.cget("text") + " Nyert")
            if gomb5.cget("text") == "X":
                score(user1.cget("text"), user2.cget("text"))
            else:
                score(user2.cget("text"), user1.cget("text"))

def reset():
        gomb1.config(text="1")
        gomb2.config(text="2")
        gomb3.config(text="3")
        gomb4.config(text="4")
        gomb5.config(text="5")
        gomb6.config(text="6")
        gomb7.config(text="7")
        gomb8.config(text="8")
        gomb9.config(text="9")
        global kor
        kor = 0


    #def mentes():

def ScoreBoard():

    def gombscore():
        user = HMM_scorecount(userName.get())
        name.config(text=f"Name: {user.name}\nWins: {user.win}\nLosses: {user.loss}")

    scoreWindow = Toplevel(root)
    scoreWindow.title("ScoreBoard")
    scoreWindow.geometry("700x400")

    userName = StringVar()
    userName.set("")
    userNameEntry = Entry(scoreWindow, textvariable=userName, width=40)
    userNameEntry.grid(row=0, column=1)

    ok = Button(scoreWindow, text="ok", width=10, command=gombscore)
    ok.grid(row=2, column=1)

    name = Label(scoreWindow, text="name")
    name.grid(row=3, column=1)

def register():

    def gombOk():
        if userName.get() == "" or userPassword.get() == "":
            messagebox.showinfo("Hiba", "a név vagy jelszó üres")
        else:
            mentes(userName.get(), userPassword.get())
            RegWindow.destroy()

    RegWindow = Toplevel(root)
    RegWindow.title("regisztráció")
    ok = Button(RegWindow, text="ok", width=10, command=gombOk)
    ok.grid(row=2, column=1)
    name = Label(RegWindow, text="név:", width=10, height=5, font=("Arial", 10))
    name.grid(row=0, column=0)

    userName = StringVar()
    userName.set("")
    userNameEntry = Entry(RegWindow, textvariable=userName, width=40)
    userNameEntry.grid(row=0, column=1)

    userPassword = StringVar()
    userPassword.set("")
    userPasswordEntry = Entry(RegWindow, textvariable=userPassword, width=40)
    userPasswordEntry.grid(row=1, column=1)

    password = Label(RegWindow, text="jelszó:", width=10, height=5, font=("Arial", 10))
    password.grid(row=1, column=0)

def login(user):
    def gombLogin():
        userdata = log()
        if userName.get() == "" or userPassword.get() == "" or userName.get() not in userdata and userPassword.get() not in userdata:
            messagebox.showinfo("Hiba", "a név vagy jelszó helytelen")
        elif userName.get() in userdata and userPassword.get() in userdata:
            user.config(text=userName.get())
            LoginWindow.destroy()

    LoginWindow = Toplevel(root)
    LoginWindow.title("belépés")
    ok = Button(LoginWindow, text="ok", width=10, command=gombLogin)
    ok.grid(row=2, column=1)
    name = Label(LoginWindow, text="név:", width=10, height=5, font=("Arial", 10))
    name.grid(row=0, column=0)

    userName = StringVar()
    userName.set("")
    userNameEntry = Entry(LoginWindow, textvariable=userName, width=40)
    userNameEntry.grid(row=0, column=1)

    userPassword = StringVar()
    userPassword.set("")
    userPasswordEntry = Entry(LoginWindow, textvariable=userPassword, width=40)
    userPasswordEntry.grid(row=1, column=1)

    password = Label(LoginWindow, text="jelszó:", width=10, height=5, font=("Arial", 10))
    password.grid(row=1, column=0)


#window

root = Tk()
root.title("app")
root.geometry("700x400")

menu = Menu(root)

lehetosegek = Menu(menu)
lehetosegek.add_command(label="reset", command=reset)
lehetosegek.add_command(label="regisztráció", command=register)
lehetosegek.add_command(label="scoreboard", command=ScoreBoard)
menu.add_cascade(label="lehetőségek", menu=lehetosegek)


Amoba = Label(root, text="AMŐBA", width=10, height=5, font=("Arial", 10))
Amoba.grid(row=0, column=0)

kezd = Label(root, text="Kezdő: X")
kezd.grid(row=0, column=1)

valt = Button(root, text="Váltás", width=10, command=valtas)
valt.grid(row=0, column=2)

gomb1 = Button(root, text="1", width=10, height=5, command=lambda: gomb(gomb1))
gomb1.grid(row=1, column=1, pady=10, padx=10)
gomb2 = Button(root, text="2", width=10, height=5, command=lambda: gomb(gomb2))
gomb2.grid(row=1, column=2, pady=10, padx=10)
gomb3 = Button(root, text="3", width=10, height=5, command=lambda: gomb(gomb3))
gomb3.grid(row=1, column=3, pady=10, padx=10)
gomb4 = Button(root, text="4", width=10, height=5, command=lambda: gomb(gomb4))
gomb4.grid(row=2, column=1, pady=10, padx=10)
gomb5 = Button(root, text="5", width=10, height=5, command=lambda: gomb(gomb5))
gomb5.grid(row=2, column=2, pady=10, padx=10)
gomb6 = Button(root, text="6", width=10, height=5, command=lambda: gomb(gomb6))
gomb6.grid(row=2, column=3, pady=10, padx=10)
gomb7 = Button(root, text="7", width=10, height=5, command=lambda: gomb(gomb7))
gomb7.grid(row=3, column=1, pady=10, padx=10)
gomb8 = Button(root, text="8", width=10, height=5, command=lambda: gomb(gomb8))
gomb8.grid(row=3, column=2, pady=10, padx=10)
gomb9 = Button(root, text="9",width=10, height=5, command=lambda: gomb(gomb9))
gomb9.grid(row=3, column=3, pady=10, padx=10)

felhasznalok = Label(root, text="felhasználók:",width=10)
felhasznalok.grid(row=0, column=5, pady=10, padx=10)

login1 = Button(root, text="belépés",width=10, command=lambda: login(user1))
login1.grid(row=1, column=4, pady=10, padx=10)

user1 = Label(root, text="guest",width=10)
user1.grid(row=1, column=5, pady=10, padx=10)

X = Label(root, text="X",width=10)
X.grid(row=1, column=6, pady=10, padx=10)

login2 = Button(root, text="belépés",width=10, command=lambda: login(user2))
login2.grid(row=2, column=4, pady=10, padx=10)

user2 = Label(root, text="guest",width=10)
user2.grid(row=2, column=5, pady=10, padx=10)

O = Label(root, text="O",width=10)
O.grid(row=2, column=6, pady=10, padx=10)

root.config(menu=menu)
root.mainloop()
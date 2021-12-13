from tkinter import *
import sqlite3
import os
from tkinter import messagebox
from tkinter.font import BOLD, Font

root = Tk()
root.title("Sign In")
root.iconbitmap('resources/img/folder-icon.ico')
width = 440
height = 487
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


def Database():
    global conn, cursor
    conn = sqlite3.connect("cache/LoginCache.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS dbmembr (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM dbmembr WHERE username = 'admin' AND password ='123'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO dbmembr (username, password) VALUES('admin', '123')")
        conn.commit()

def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="" , fg="#1df700")
    else:
        cursor.execute("SELECT * FROM dbmembr WHERE username = ? AND password = ?",(USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            root.withdraw()
            os.system('py grading-system/main.py')
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="The password you\'ve entered is incorrect", fg="#5c5b96")
            USERNAME.set("")
            PASSWORD.set("")
            cursor.close()
            conn.close()


def click(event):
    username.config(state=NORMAL)
    username.delete(0, END)
def click1(event):
    password.config(state=NORMAL,show="*")
    password.delete(0, END)

def on_enter(event):
    login_tuplok.config(image=login2)
def on_leave(enter):
    login_tuplok.config(image=login)
#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
ustpLogo = PhotoImage(file='resources/img/ustp-logo.png')
login = PhotoImage(file='resources/img/login-button.png')
login2 = PhotoImage(file='resources/img/login-button-hover.png')
usernameEntryImage = PhotoImage(file='resources/img/username.png')
passwordEntryImage = PhotoImage(file='resources/img/password.png')
headerFont= Font(family="Noto Sans",size=36,weight=BOLD)

#==============================FRAMES=========================================
Form = Frame(root)
Form.pack(side=TOP, pady=80)
#==============================LABELS=========================================
signIn = Label(root,image=ustpLogo,bd=0,fg="#ffc20a",bg="#f1f1f1",font=headerFont)
signIn.place(x=80,y=30)

lbl_title = Label(root, text="Sign In",bd=0,fg="#ffc20a",bg="#f1f1f1",font=headerFont)
lbl_title.place(x=80,y=120)

lbl_text = Label(root,bg='#f1f1f1',bd=0,fg="#ffc20a",font="Arial 10")
lbl_text.place(x=99,y=315)

#==============================ENTRY WIDGETS==================================
usernameEntry = Label(root,image=usernameEntryImage,bd=0,fg="#ffc20a",bg="#f1f1f1",font=headerFont)
usernameEntry.place(x=80,y=210)

username = Entry(root, textvariable=USERNAME,font='Inter 13',fg='#505050',bg='#ffffff',width=16,bd=0)
username.insert(8,"USERNAME")
username.bind("<Button-1>",click)
username.place(x=122,y=220)

passwordEntry = Label(root,image=passwordEntryImage,bd=0,fg="#ffc20a",bg="#f1f1f1",font=headerFont)
passwordEntry.place(x=80,y=270)

password = Entry(root, textvariable=PASSWORD,font='Inter 13',fg='#505050',bg='#ffffff',width=16,bd=0)
password.insert(8,"PASSWORD")
password.bind("<Button-1>",click1)
password.place(x=122,y=280)
    
#==============================BUTTON WIDGETS=================================
login_tuplok = Button(root,image=login,command=Login,borderwidth=0,fg='#050505',bg='#f1f1f1',border=0,activebackground='#f1f1f1',cursor='hand2')
login_tuplok.place(x=80,y=338)
login_tuplok.bind("<Enter>", on_enter)
login_tuplok.bind ("<Leave>", on_leave)
login_tuplok.bind(Login)
lbl_forget = Label(root,text="Forgot password?",bd=0,fg="#ffc20a",bg="#f1f1f1",font="Arial 12")
lbl_forget.place(x=222,y=398)
root.config(bg='#f1f1f1')
Form.config(bg='#f1f1f1')
root.mainloop()


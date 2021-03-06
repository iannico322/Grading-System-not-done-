from tkinter import *
from tkinter import messagebox
import os
import math
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
def logout():
    
    root.withdraw()
    os.system('login.py')
    
def on_enter(event):
    logout_button.config(image=logout_button_photo2)
    
def on_leave(enter):
    logout_button.config(image=logout_button_photo)

def on_enter1(event):
    calculate_button.config(image=cal_button2)
def on_leave1(enter):
    calculate_button.config(image=cal_button)
def calculate():
    pop = Tk()
    pop.title('Result')
    pop.iconbitmap('resources/img/folder-icon.ico')
    width = 572
    height = 405
    screen_width = pop.winfo_screenwidth()
    screen_height = pop.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    pop.geometry("%dx%d+%d+%d" % (width, height, x, y))
    pop.resizable(False, False)


    #calculation
    attendanceGrade = ((ATTENDANCE1.get() + ATTENDANCE1.get() + ATTENDANCE3.get() )/3)*100


    quizOne = (QUIZ1.get() / 20) * 100
    quizTwo = (QUIZ2.get() / 10) * 100
    quizThree = (QUIZ3.get() / 20) * 100

    quizGrade = (quizOne + quizTwo + quizThree) / 3

    classpationGrade = (PARTICIPATION.get() / 3) * 100
    
    assignmentOne = (ASS1.get() / 40) * 100
    assignmentTwo = (ASS2.get() / 20) * 100
    assignmentThree = (ASS3.get() / 50) * 100

    assignmentGrade = (assignmentOne + assignmentTwo + assignmentThree) / 3
    
    projectOne = (PROJECT1.get()/ 60) * 100
    projectTwo = (PROJECT2.get() / 40) * 100
    projectThree = (PROJECT3.get()/ 50) * 100
    projectGrade = (projectOne + projectTwo + projectThree) / 3
    
    handsOnOne = (HANDSON1.get()/ 100) * 100
    handsOnTwo = (HANDSON2.get()/ 100) * 100
    handsOnGrade = (handsOnOne + handsOnTwo) / 2
    
    majorExamGrade = (MAJOREXAM.get() / 80) * 100
    participationGrade = ((classpationGrade + assignmentGrade + projectGrade) /3 )
    finalGrade = ((attendanceGrade * .15) + (quizGrade * .15) + (participationGrade * .15)+(handsOnGrade * .20)+(majorExamGrade* .35))
	
    finalGrade = math.trunc(finalGrade)
   
    if(finalGrade > 95):
        finalGrade = 1.0
    elif (finalGrade == 94):
        finalGrade = 1.1
    elif(finalGrade == 93):
        finalGrade = 1.2
    elif(finalGrade == 92):
        finalGrade = 1.3
    elif (finalGrade == 91):
        finalGrade = 1.4
    elif (finalGrade == 90):
        finalGrade = 1.5
    elif (finalGrade == 89):
        finalGrade = 1.6
    elif (finalGrade == 88):
        finalGrade = 1.7
    elif (finalGrade == 87):
        finalGrade = 1.8
    elif (finalGrade == 86):
        finalGrade = 1.9
    elif (finalGrade == 85):
        finalGrade = 2.0
    elif (finalGrade == 84):
        finalGrade = 2.1
    elif (finalGrade == 83):
        finalGrade = 2.2
    elif (finalGrade == 82):
        finalGrade = 2.3
    elif (finalGrade == 81):
        finalGrade = 2.4
    elif (finalGrade == 80):
        finalGrade = 2.5
    elif (finalGrade == 79):
        finalGrade = 2.6
    elif (finalGrade == 78):
        finalGrade = 2.7
    elif (finalGrade == 77):
        finalGrade = 2.8
    elif (finalGrade == 76):
        finalGrade = 2.9
    elif (finalGrade == 75):
        finalGrade = 3.0
    elif (finalGrade <= 74):
        finalGrade = 5.0
		

    if(finalGrade == 5.0):
        remarks = "Failed"
    else:
        remarks = "Passed"
		
#     ID Number:
# Name of the Student:
# Course and Year:
# Attendance Grade:
# Quizzes Grade:
# Class Participation Grade:
# Assignment Grade:
# Project Grade:
# Hands - on Grade:
# Major Exam Grade:
# Final Grade:
# Remarks: (Passed or Failed)
    Label(pop,text=f"ID Number: {ID.get()}").grid(row=0,column = 1)
    Label(pop,text=f"Name of the Student: {NAME.get()}").grid(row=1,column = 1)
    Label(pop,text=f"Course and Year: {COURSEANDSECTION.get()}").grid(row=2,column = 1)
    Label(pop,text=f"Attendance Grade: {attendanceGrade}").grid(row=3,column = 1)
    Label(pop,text=f"Quizzes Grade: {quizGrade}").grid(row=4,column = 1)
    Label(pop,text=f"Class Participation Grade: {classpationGrade}").grid(row=5,column = 1)
    Label(pop,text=f"Assignment Grade: {assignmentGrade}").grid(row=6,column = 1)
    Label(pop,text=f"Project Grade: {projectGrade}").grid(row=7,column = 1)
    Label(pop,text=f"Hands-on Grade: {handsOnGrade}").grid(row=8,column = 1)
    Label(pop,text=f"Major Exam Grade: {majorExamGrade}").grid(row=9,column = 1)
    
    Label(pop,text=f"Final Grade: {finalGrade}").grid(row=10,column = 1)
    Label(pop,text=f"Remarks: {remarks}").grid(row=11,column = 1)
    Button(pop,text='Save to Database', fg='orange',background='white',font='Inter 14').grid(row=12,column = 1)

    pop.mainloop()

def limitSizeForAssignment(*args):

    value = str(ASS1.get())
    if len(value) > 2: ASS1.set(value[:2])
    value1 = str(ASS2.get())
    if len(value1) > 2: ASS2.set(value1[:2])
    value2 = str(ASS3.get())
    if len(value2) > 2: ASS3.set(value2[:2])

def limitSizeForHandsOn(*args):

    value = str(HANDSON1.get())
    if len(value) > 3: HANDSON1.set(value[:3])
    value1 = str(HANDSON2.get())
    if len(value1) > 3: HANDSON2.set(value1[:3])

def limitSizeForMajorExam(*args):
    
    value = str(MAJOREXAM.get())
    if len(value) > 2: MAJOREXAM.set(value[:2])

def limitSizeForQuizzes(*args):

    value = str(QUIZ1.get())
    if len(value) > 2: QUIZ1.set(value[:2])
    value1 = str(QUIZ2.get())
    if len(value1) > 2: QUIZ2.set(value1[:2])
    value2 = str(QUIZ3.get())
    if len(value2) > 2: QUIZ3.set(value2[:2])
def limitSizeForProjects(*args):
    
    value = str(PROJECT1.get())
    if len(value) > 2: PROJECT1.set(value[:2])
    value1 = str(PROJECT2.get())
    if len(value1) > 2: PROJECT2.set(value1[:2])
    value2 = str(PROJECT3.get())
    if len(value2) > 2: PROJECT3.set(value2[:2])

#/functions=========================================
root = Tk()
root.title('E-GRADING')
root.iconbitmap('resources/img/folder-icon.ico')
width = 1072
height = 645
screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, False)

#Images=========================================


cal_button = PhotoImage(file='resources/img/calculate-button.png')
cal_button2 = PhotoImage(file='resources/img/calculate-button-active.png')

set_grade_photo = PhotoImage(file='resources/img/setgrade-button.png')

main = PhotoImage(file='resources/img/main.png')


logout_button_photo = PhotoImage(file='resources/img/logout-inactive.png')
logout_button_photo2 = PhotoImage(file='resources/img/logout-active.png')
#/Images=========================================
#Variables=========================================
ID = StringVar()
NAME = StringVar()
COURSEANDSECTION = StringVar()


ATTENDANCE1  = IntVar()
ATTENDANCE2 = IntVar()
ATTENDANCE3 = IntVar()

MAJOREXAM = IntVar()
MAJOREXAM.trace('w', limitSizeForMajorExam)
PARTICIPATION = IntVar()

HANDSON1 = IntVar()
HANDSON2 = IntVar()
HANDSON1.trace('w', limitSizeForHandsOn)
HANDSON2.trace('w', limitSizeForHandsOn)

QUIZ1 = IntVar()
QUIZ2 = IntVar()
QUIZ3 = IntVar()
QUIZ1.trace('w', limitSizeForQuizzes)
QUIZ2.trace('w', limitSizeForQuizzes)
QUIZ3.trace('w', limitSizeForQuizzes)

ASS1 = IntVar()
ASS2 = IntVar()
ASS3 = IntVar()
ASS1.trace('w', limitSizeForAssignment)
ASS2.trace('w', limitSizeForAssignment)
ASS3.trace('w', limitSizeForAssignment)

PROJECT1 = IntVar()
PROJECT2 = IntVar()
PROJECT3 = IntVar()
PROJECT1.trace('w', limitSizeForProjects)
PROJECT2.trace('w', limitSizeForProjects)
PROJECT3.trace('w', limitSizeForProjects)

main_bg = Label(root,image=main,bd=0)
main_bg.place(x=0,y=0)

id_number = Entry(root, textvariable=ID,font='Inter 14',fg='orange',bg='white',width=13,bd=0)
id_number.place(x=449,y=52)

course_and_section = Entry(root, textvariable=COURSEANDSECTION,font='Inter 14',fg='orange',bg='white',width=13,bd=0)
course_and_section.place(x=650,y=52)

name = Entry(root, textvariable=NAME,font='Inter 15',fg='orange',bg='white',width=19,bd=0)
name.place(x=449,y=134)

attendance1 = Checkbutton (fg='orange', variable=ATTENDANCE1,bg='white',bd=0,activebackground='white',cursor='hand2',activeforeground='white',onvalue=1,offvalue=0) 
attendance1.place(x=910,y=101)

attendance2 = Checkbutton (fg='orange', variable=ATTENDANCE2,bg='white',bd=0,activebackground='white',cursor='hand2',activeforeground='white',onvalue=1,offvalue=0) 
attendance2.place(x=964,y=101)

attendance3 = Checkbutton (fg='orange', variable=ATTENDANCE3,bg='white',bd=0,activebackground='white',cursor='hand2',activeforeground='white',onvalue=1,offvalue=0) 
attendance3.place(x=1018,y=101)

style = ttk.Style()
style.theme_create('combostyle', parent='alt',
                   settings={'TCombobox':
                             {'configure':
                              {'selectbackground': 'white','selectforeground': 'orange',
                               'fieldbackground': 'white',
                               'foreground': '#1df700',
                               'background': 'white',
                               'bd': 0,
                               'relief': GROOVE,
                               'width': 10,
                               }}}
                   )
style.theme_use('combostyle')
participation = ttk.Combobox(root,font='Inter 19',width=3,foreground='orange',textvariable=PARTICIPATION)
participation.config(values=[
0,1,
2,
3])
participation.place(x=507,y=284)

hands_on1 = Entry(root, textvariable=HANDSON1,font='Inter 14',fg='orange',bg='white',width=3,bd=0)
hands_on1.place(x=673,y=286)
hands_on2 = Entry(root, textvariable=HANDSON2,font='Inter 14',fg='orange',bg='white',width=3,bd=0)
hands_on2.place(x=826,y=286)


quiz1 = Entry(root, textvariable=QUIZ1,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
quiz1.place(x=514,y=383)
quiz2 = Entry(root, textvariable=QUIZ2,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
quiz2.place(x=514,y=434)
quiz3 = Entry(root, textvariable=QUIZ3,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
quiz3.place(x=514,y=486)


assignment1 = Entry(root, textvariable=ASS1,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
assignment1.place(x=680,y=383)
assignment2 = Entry(root, textvariable=ASS2,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
assignment2.place(x=680,y=434)
assignment3 = Entry(root, textvariable=ASS3,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
assignment3.place(x=680,y=486)


project1 = Entry(root, textvariable=PROJECT1,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
project1.place(x=852,y=383)
project2 = Entry(root, textvariable=PROJECT2,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
project2.place(x=852,y=434)
project3 = Entry(root, textvariable=PROJECT3,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
project3.place(x=852,y=486)

majorexam = Entry(root, textvariable=MAJOREXAM,font='Inter 19',fg='orange',bg='white',width=2,bd=0)
majorexam.place(x=975,y=290)

calculate_button = Button(root,image=cal_button,command=calculate,borderwidth=0,fg='#050505',bg='#f1f1f1',border=0,activebackground='#f1f1f1',cursor='hand2')
calculate_button.place(x=464,y=541)
calculate_button.bind("<Enter>", on_enter1)
calculate_button.bind ("<Leave>", on_leave1)
root.config(bg='#17161b')

setgrade_button = Button(root,image=set_grade_photo,command=logout,borderwidth=0,fg='#050505',bg='#a0a0a0',border=0,activebackground='#a0a0a0',cursor='hand2')
setgrade_button.place(x=206,y=240)

logout_button = Button(root,image=logout_button_photo,command=logout,borderwidth=0,fg='#050505',bg='#a0a0a0',border=0,activebackground='#a0a0a0',cursor='hand2')
logout_button.place(x=229,y=376)
logout_button.bind("<Enter>", on_enter)
logout_button.bind ("<Leave>", on_leave)



root.mainloop()


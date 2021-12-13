from tkinter import *
from tkinter import messagebox
import os
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image

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
	
    finalGrade = round(finalGrade, 2)
   
    if(finalGrade > 50):
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
        finalGrade = 0.0
		

    if(finalGrade == 0.0):
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

    value = ASS1.get()
    if len(value) > 2: ASS1.set(value[:2])
    value1 = ASS2.get()
    if len(value1) > 2: ASS2.set(value1[:'2'])
    value2 = ASS3.get()
    if len(value2) > 2: ASS3.set(value2[:'2'])

def limitSizeForHandsOn(*args):

    value = HANDSON1.get()
    if len(value) > 3: HANDSON1.set(value[:3])
    value1 = HANDSON2.get()
    if len(value1) > 3: HANDSON2.set(value1[:3])

def limitSizeForMajorExam(*args):
    
    value = MAJOREXAM.get()
    if len(value) > 2: MAJOREXAM.set(value[:2])

def limitSizeForQuizzes(*args):

    value = QUIZ1.get()
    if len(value) > 2: QUIZ1.set(value[:2])
    value1 = QUIZ2.get()
    if len(value1) > 2: QUIZ2.set(value1[:2])
    value2 = QUIZ3.get()
    if len(value2) > 2: QUIZ3.set(value2[:2])
def limitSizeForProjects(*args):
    
    value = PROJECT1.get()
    if len(value) > 2: PROJECT1.set(value[:2])
    value1 = PROJECT2.get()
    if len(value1) > 2: PROJECT2.set(value1[:2])
    value2 = PROJECT3.get()
    if len(value2) > 2: PROJECT3.set(value2[:2])

#/functions=========================================
root = Tk()
root.title('E-GRADING')
root.iconbitmap('resources/img/folder-icon.ico')
width = 1072
height = 605
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, False)

#Images=========================================
main = Image.open('resources/img/mainbig.png')
cal_button = PhotoImage(file='resources/img/calculate-button.png')


resized = main.resize((1072,605 ), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
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

main_bg = Label(root,image=new_pic,bd=0)
main_bg.place(x=0,y=0)

id_number = Entry(root, textvariable=ID,font='Inter 14',fg='orange',bg='white',width=13,bd=0)
id_number.place(x=449,y=48)

course_and_section = Entry(root, textvariable=COURSEANDSECTION,font='Inter 14',fg='orange',bg='white',width=13,bd=0)
course_and_section.place(x=650,y=48)

name = Entry(root, textvariable=NAME,font='Inter 15',fg='orange',bg='white',width=19,bd=0)
name.place(x=449,y=125)

attendance1 = Checkbutton (fg='orange', variable=ATTENDANCE1,bg='white',bd=0,activebackground='white',cursor='hand2',activeforeground='white',onvalue=1,offvalue=0) 
attendance1.place(x=910,y=95)

attendance2 = Checkbutton (fg='orange', variable=ATTENDANCE2,bg='white',bd=0,activebackground='white',cursor='hand2',activeforeground='white',onvalue=1,offvalue=0) 
attendance2.place(x=964,y=95)

attendance3 = Checkbutton (fg='orange', variable=ATTENDANCE3,bg='white',bd=0,activebackground='white',cursor='hand2',activeforeground='white',onvalue=1,offvalue=0) 
attendance3.place(x=1018,y=95)


participation = ttk.Combobox(root,font='Inter 19',width=2,foreground='orange',textvariable=PARTICIPATION)
participation.config(values=[
0,1,
2,
3])
participation.place(x=515,y=266)

hands_on1 = Entry(root, textvariable=HANDSON1,font='Inter 14',fg='orange',bg='white',width=3,bd=0)
hands_on1.place(x=673,y=271)
hands_on2 = Entry(root, textvariable=HANDSON2,font='Inter 14',fg='orange',bg='white',width=3,bd=0)
hands_on2.place(x=826,y=271)

majorexam = Entry(root, textvariable=MAJOREXAM,font='Inter 18',fg='orange',bg='white',width=2,bd=0)
majorexam.place(x=975,y=271)


quiz1 = Entry(root, textvariable=QUIZ1,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
quiz1.place(x=512,y=361)
quiz2 = Entry(root, textvariable=QUIZ2,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
quiz2.place(x=512,y=408)
quiz3 = Entry(root, textvariable=QUIZ3,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
quiz3.place(x=512,y=457)


assignment1 = Entry(root, textvariable=ASS1,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
assignment1.place(x=680,y=361)
assignment2 = Entry(root, textvariable=ASS2,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
assignment2.place(x=680,y=408)
assignment3 = Entry(root, textvariable=ASS3,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
assignment3.place(x=680,y=457)


project1 = Entry(root, textvariable=PROJECT1,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
project1.place(x=852,y=361)
project2 = Entry(root, textvariable=PROJECT2,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
project2.place(x=852,y=408)
project3 = Entry(root, textvariable=PROJECT3,font='Inter 16',fg='orange',bg='white',width=2,bd=0)
project3.place(x=852,y=457)

submit_button = Button(root,image=cal_button,command=calculate,borderwidth=0,fg='#050505',bg='#f1f1f1',border=0,activebackground='#f1f1f1',cursor='hand2')
submit_button.place(x=464,y=511)
root.config(bg='#17161b')



root.mainloop()


from tkinter import *
from tkinter import messagebox
import os
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
import sqlite3


def logout():
    root.withdraw()
    os.system("login.py")


def on_enter(event):
    logout_button.config(image=logout_button_photo2)


def on_leave(enter):
    logout_button.config(image=logout_button_photo)


def on_enter1(event):
    calculate_button.config(image=cal_button2)


def on_leave1(enter):
    calculate_button.config(image=cal_button)


# Save student_info to database.
def save_to_database(student_info):
    con = sqlite3.connect("student_database.db")
    cur = con.cursor()

    # Create table if it does not exist.
    CREATE = """CREATE TABLE IF NOT EXISTS student_grades (
        id INTEGER,
        student_name TEXT,
        course_and_year TEXT,
        grade_attendance DOUBLE,
        grade_quiz DOUBLE,
        grade_participation DOUBLE,
        grade_assignment DOUBLE,
        grade_project DOUBLE,
        grade_hands_on DOUBLE,
        grade_major_exam DOUBLE,
        final_grade DOUBLE,
        remarks TEXT
    )"""

    cur.execute(CREATE)

    # Insert student_info to student_grades.
    INSERT = "INSERT INTO student_grades VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    cur.execute(
        INSERT,
        (
            student_info[0],
            student_info[1],
            student_info[2],
            student_info[3],
            student_info[4],
            student_info[5],
            student_info[6],
            student_info[7],
            student_info[8],
            student_info[9],
            student_info[10],
            student_info[11],
        ),
    )

    # Display table contents.
    cur.execute("SELECT * FROM student_grades")

    print(cur.fetchall())


# CALCULATE
def calculate():
    pop = Tk()
    pop.title("Result")
    # pop.iconbitmap('resources/img/folder-icon.ico')
    width = 572
    height = 405
    screen_width = pop.winfo_screenwidth()
    screen_height = pop.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    pop.geometry("%dx%d+%d+%d" % (width, height, x, y))
    pop.resizable(False, False)

    # Calculate grades.
    attendanceGrade = (
        (ATTENDANCE1.get() + ATTENDANCE2.get() + ATTENDANCE3.get()) / 3
    ) * 100

    quizGrade = (
        ((QUIZ1.get() / 20) * 100)
        + ((QUIZ2.get() / 10) * 100)
        + ((QUIZ3.get() / 20) * 100)
    ) / 3

    classpationGrade = (PARTICIPATION.get() / 3) * 100

    assignmentGrade = (
        ((ASS1.get() / 40) * 100)
        + ((ASS2.get() / 20) * 100)
        + ((ASS3.get() / 50) * 100)
    ) / 3

    projectGrade = (
        ((PROJECT1.get() / 60) * 100)
        + ((PROJECT2.get() / 40) * 100)
        + ((PROJECT3.get() / 50) * 100)
    ) / 3

    handsOnGrade = (((HANDSON1.get() / 100) * 100) + ((HANDSON2.get() / 100) * 100)) / 2

    majorExamGrade = (MAJOREXAM.get() / 80) * 100

    participationGrade = (classpationGrade + assignmentGrade + projectGrade) / 3

    # Calculate final grade.

    finalGrade = int(
        (attendanceGrade * 0.15)
        + (quizGrade * 0.15)
        + (participationGrade * 0.15)
        + (handsOnGrade * 0.20)
        + (majorExamGrade * 0.35)
    )

    # Use dictionary instead of if-else for efficiency.
    grading_system = {
        94: 1.1, 93: 1.2, 92: 1.3, 91: 1.4, 90: 1.5, 89: 1.6, 87: 1.7, 86: 1.8,
        85: 1.9, 84: 2.0, 83: 2.1, 82: 2.2, 81: 2.3, 80: 2.4, 79: 2.5, 78: 2.6,
        77: 2.7, 76: 2.8, 75: 2.9,
    }

    if grading_system.get(finalGrade):
        remarks = "Passed"
        finalGrade = grading_system.get(finalGrade)
    else:
        remarks = "Passed" if finalGrade >= 95 else "Failed"
        finalGrade = 1.0 if finalGrade >= 95 else 5.0

    student_info = [
        ID.get(),
        NAME.get(),
        COURSEANDSECTION.get(),
        attendanceGrade,
        quizGrade,
        classpationGrade,
        assignmentGrade,
        projectGrade,
        handsOnGrade,
        majorExamGrade,
        finalGrade,
        remarks,
    ]

    # ID Number:
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
    Label(pop, text=f"ID Number: {ID.get()}").grid(row=0, column=1)
    Label(pop, text=f"Name of the Student: {NAME.get()}").grid(row=1, column=1)
    Label(pop, text=f"Course and Year: {COURSEANDSECTION.get()}").grid(row=2, column=1)
    Label(pop, text=f"Attendance Grade: {attendanceGrade}").grid(row=3, column=1)
    Label(pop, text=f"Quizzes Grade: {quizGrade}").grid(row=4, column=1)
    Label(pop, text=f"Class Participation Grade: {classpationGrade}").grid(
        row=5, column=1
    )
    Label(pop, text=f"Assignment Grade: {assignmentGrade}").grid(row=6, column=1)
    Label(pop, text=f"Project Grade: {projectGrade}").grid(row=7, column=1)
    Label(pop, text=f"Hands-on Grade: {handsOnGrade}").grid(row=8, column=1)
    Label(pop, text=f"Major Exam Grade: {majorExamGrade}").grid(row=9, column=1)

    Label(pop, text=f"Final Grade: {finalGrade}").grid(row=10, column=1)
    Label(pop, text=f"Remarks: {remarks}").grid(row=11, column=1)

    Button(
        pop,
        text="Save to Database",
        fg="orange",
        background="white",
        font="Inter 14",
        command=lambda: save_to_database(student_info),
    ).grid(row=12, column=1)

    pop.mainloop()


def limitSizeForAssignment(*args):
    value = str(ASS1.get())
    if len(value) > 2:
        ASS1.set(value[:2])
    value1 = str(ASS2.get())
    if len(value1) > 2:
        ASS2.set(value1[:2])
    value2 = str(ASS3.get())
    if len(value2) > 2:
        ASS3.set(value2[:2])


def limitSizeForHandsOn(*args):
    value = str(HANDSON1.get())
    if len(value) > 3:
        HANDSON1.set(value[:3])
    value1 = str(HANDSON2.get())
    if len(value1) > 3:
        HANDSON2.set(value1[:3])


def limitSizeForMajorExam(*args):
    value = str(MAJOREXAM.get())
    if len(value) > 2:
        MAJOREXAM.set(value[:2])


def limitSizeForQuizzes(*args):
    value = str(QUIZ1.get())
    if len(value) > 2:
        QUIZ1.set(value[:2])
    value1 = str(QUIZ2.get())
    if len(value1) > 2:
        QUIZ2.set(value1[:2])
    value2 = str(QUIZ3.get())
    if len(value2) > 2:
        QUIZ3.set(value2[:2])


def limitSizeForProjects(*args):
    value = str(PROJECT1.get())
    if len(value) > 2:
        PROJECT1.set(value[:2])
    value1 = str(PROJECT2.get())
    if len(value1) > 2:
        PROJECT2.set(value1[:2])
    value2 = str(PROJECT3.get())
    if len(value2) > 2:
        PROJECT3.set(value2[:2])


# /functions=========================================


root = Tk()
root.title("E-GRADING")
# root.iconbitmap('resources/img/folder-icon.ico')
width = 1072
height = 645
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, False)


# Images=========================================
main = Image.open("../resources/img/main.png")

cal_button = PhotoImage(file="../resources/img/calculate-button.png")
cal_button2 = PhotoImage(file="../resources/img/calculate-button-active.png")

set_grade_photo = PhotoImage(file="../resources/img/setgrade-button.png")
resized = main.resize((1072, 605), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)


logout_button_photo = PhotoImage(file="../resources/img/logout-inactive.png")
logout_button_photo2 = PhotoImage(file="../resources/img/logout-active.png")
# /Images=========================================


# Variables=========================================
ID = StringVar()
NAME = StringVar()
COURSEANDSECTION = StringVar()


ATTENDANCE1 = IntVar()
ATTENDANCE2 = IntVar()
ATTENDANCE3 = IntVar()

MAJOREXAM = IntVar()
MAJOREXAM.trace("w", limitSizeForMajorExam)
PARTICIPATION = IntVar()

HANDSON1 = IntVar()
HANDSON2 = IntVar()
HANDSON1.trace("w", limitSizeForHandsOn)
HANDSON2.trace("w", limitSizeForHandsOn)

QUIZ1 = IntVar()
QUIZ2 = IntVar()
QUIZ3 = IntVar()
QUIZ1.trace("w", limitSizeForQuizzes)
QUIZ2.trace("w", limitSizeForQuizzes)
QUIZ3.trace("w", limitSizeForQuizzes)

ASS1 = IntVar()
ASS2 = IntVar()
ASS3 = IntVar()
ASS1.trace("w", limitSizeForAssignment)
ASS2.trace("w", limitSizeForAssignment)
ASS3.trace("w", limitSizeForAssignment)

PROJECT1 = IntVar()
PROJECT2 = IntVar()
PROJECT3 = IntVar()
PROJECT1.trace("w", limitSizeForProjects)
PROJECT2.trace("w", limitSizeForProjects)
PROJECT3.trace("w", limitSizeForProjects)

main_bg = Label(root, image=new_pic, bd=0)
main_bg.place(x=0, y=0)

id_number = Entry(
    root, textvariable=ID, font="Inter 14", fg="orange", bg="white", width=13, bd=0
)
id_number.place(x=449, y=48)

course_and_section = Entry(
    root,
    textvariable=COURSEANDSECTION,
    font="Inter 14",
    fg="orange",
    bg="white",
    width=13,
    bd=0,
)
course_and_section.place(x=650, y=48)

name = Entry(
    root, textvariable=NAME, font="Inter 15", fg="orange", bg="white", width=19, bd=0
)
name.place(x=449, y=125)

attendance1 = Checkbutton(
    fg="orange",
    variable=ATTENDANCE1,
    bg="white",
    bd=0,
    activebackground="white",
    cursor="hand2",
    activeforeground="white",
    onvalue=1,
    offvalue=0,
)
attendance1.place(x=910, y=95)

attendance2 = Checkbutton(
    fg="orange",
    variable=ATTENDANCE2,
    bg="white",
    bd=0,
    activebackground="white",
    cursor="hand2",
    activeforeground="white",
    onvalue=1,
    offvalue=0,
)
attendance2.place(x=964, y=95)

attendance3 = Checkbutton(
    fg="orange",
    variable=ATTENDANCE3,
    bg="white",
    bd=0,
    activebackground="white",
    cursor="hand2",
    activeforeground="white",
    onvalue=1,
    offvalue=0,
)
attendance3.place(x=1018, y=95)


participation = ttk.Combobox(
    root, font="Inter 19", width=2, foreground="orange", textvariable=PARTICIPATION
)
participation.config(values=[0, 1, 2, 3])
participation.place(x=515, y=266)

hands_on1 = Entry(
    root, textvariable=HANDSON1, font="Inter 14", fg="orange", bg="white", width=3, bd=0
)
hands_on1.place(x=673, y=271)
hands_on2 = Entry(
    root, textvariable=HANDSON2, font="Inter 14", fg="orange", bg="white", width=3, bd=0
)
hands_on2.place(x=826, y=271)

majorexam = Entry(
    root,
    textvariable=MAJOREXAM,
    font="Inter 18",
    fg="orange",
    bg="white",
    width=2,
    bd=0,
)
majorexam.place(x=975, y=271)


quiz1 = Entry(
    root, textvariable=QUIZ1, font="Inter 16", fg="orange", bg="white", width=2, bd=0
)
quiz1.place(x=512, y=361)
quiz2 = Entry(
    root, textvariable=QUIZ2, font="Inter 16", fg="orange", bg="white", width=2, bd=0
)
quiz2.place(x=512, y=408)
quiz3 = Entry(
    root, textvariable=QUIZ3, font="Inter 16", fg="orange", bg="white", width=2, bd=0
)
quiz3.place(x=512, y=457)


assignment1 = Entry(
    root, textvariable=ASS1, font="Inter 16", fg="orange", bg="white", width=2, bd=0
)
assignment1.place(x=680, y=361)
assignment2 = Entry(
    root, textvariable=ASS2, font="Inter 16", fg="orange", bg="white", width=2, bd=0
)
assignment2.place(x=680, y=408)
assignment3 = Entry(
    root, textvariable=ASS3, font="Inter 16", fg="orange", bg="white", width=2, bd=0
)
assignment3.place(x=680, y=457)


project1 = Entry(
    root, textvariable=PROJECT1, font="Inter 16", fg="orange", bg="white", width=2, bd=0
)
project1.place(x=852, y=361)
project2 = Entry(
    root, textvariable=PROJECT2, font="Inter 16", fg="orange", bg="white", width=2, bd=0
)
project2.place(x=852, y=408)
project3 = Entry(
    root, textvariable=PROJECT3, font="Inter 16", fg="orange", bg="white", width=2, bd=0
)
project3.place(x=852, y=457)

calculate_button = Button(
    root,
    image=cal_button,
    command=calculate,
    borderwidth=0,
    fg="#050505",
    bg="#f1f1f1",
    border=0,
    activebackground="#f1f1f1",
    cursor="hand2",
)
calculate_button.place(x=464, y=511)
calculate_button.bind("<Enter>", on_enter1)
calculate_button.bind("<Leave>", on_leave1)
root.config(bg="#17161b")

setgrade_button = Button(
    root,
    image=set_grade_photo,
    command=logout,
    borderwidth=0,
    fg="#050505",
    bg="#a0a0a0",
    border=0,
    activebackground="#a0a0a0",
    cursor="hand2",
)
setgrade_button.place(x=206, y=204)

logout_button = Button(
    root,
    image=logout_button_photo,
    command=logout,
    borderwidth=0,
    fg="#050505",
    bg="#a0a0a0",
    border=0,
    activebackground="#a0a0a0",
    cursor="hand2",
)
logout_button.place(x=229, y=370)
logout_button.bind("<Enter>", on_enter)
logout_button.bind("<Leave>", on_leave)


root.mainloop()

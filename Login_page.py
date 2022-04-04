from tkinter import *

def Login_page():
    global root
    root=Tk()
    root.geometry("800x600")
    root.geometry("+275+70")
    root.configure(bg='light blue')
    root.title("Student Database")
    root.resizable(False, False)
    main()
    root.mainloop()

def addstudent():
    root.destroy()
    import add_student
    add_student.add_student()

def viewstudent():
    root.destroy()
    import Show_student
    Show_student.show_student()

def deletestudent():
    import delete_record
    delete_record.delete_record()

def addmarks():
    root.destroy()
    import Add_marks
    Add_marks.add_marks()

def gradesheet():
    root.destroy()
    import Gradesheet
    Gradesheet.gradesheet()

def modify():
    root.destroy()
    import modify
    modify.modify()

def p():
    b1=  Button(root, text="Add Student",width=35,font=("Times New Roman",15),command=addstudent)
    b2 = Button(root, text="View Detail of Student",width=35,font=("Times New Roman",15),command=viewstudent)
    b3 = Button(root, text="Remove Student",width=35,font=("Times New Roman",15),command=deletestudent)
    b4 = Button(root, text="Add Marks Of Student",width=35,font=("Times New Roman",15),command=addmarks)
    b5 = Button(root, text="Grade Sheet Of Student",width=35,font=("Times New Roman",15),command=gradesheet)
    b6 = Button(root, text="Modify the Record Of Student",width=35,font=("Times New Roman",15),command=modify)

    l = Label(root, text="Student Database App",font=("Times New Roman",40),bg="light blue",fg="#008000")
    l.place(relx=0.5,rely=0.09,anchor=CENTER)

    d=Label(root,text="Developed by: Roshan Ojha",font=("Times New Roman",12),bg="Light blue")
    d.place(relx=0,rely=1,anchor=SW)

    b1.place(relx=0.5,rely=0.24,anchor=CENTER)
    b2.place(relx=0.5,rely=0.31,anchor=CENTER)
    b3.place(relx=0.5,rely=0.38,anchor=CENTER)
    b4.place(relx=0.5,rely=0.45,anchor=CENTER)
    b5.place(relx=0.5,rely=0.52,anchor=CENTER)
    b6.place(relx=0.5,rely=0.59,anchor=CENTER)

def main():
    l1=Label(root,text="Welcome to Student Database",font=("Times New Roman",35),bg="light blue",fg="Lime")
    l1.grid(padx=120,pady=275)
    root.after(2000,lambda:(l1.destroy(),p()))
Login_page()


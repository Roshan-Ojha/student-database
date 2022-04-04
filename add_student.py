from tkinter import *
import tkinter.messagebox
import sqlite3
def add_student():
    global top,r
    top=Tk()
    top.geometry("800x600")
    top.geometry("+275+70")
    top .configure(bg="#7CFC00")
    top.title("Add Student")
    main()

    top.resizable(False, False)
    top.mainloop()
def back():
    top.destroy()
    import Login_page
    Login_page.Login_page()

def check():
    global g
    if r.get()==1:
        g="Male"
    elif r.get()==2:
        g="Female"
    elif r.get()==3:
        g="Other"

def submit():
    check()
    ans=tkinter.messagebox.askquestion("Student Database","Are you sure you want to add this record to database?")
    if ans == "yes":
        conn=sqlite3.connect('Add.db')
        c=conn.cursor()
        c.execute("INSERT INTO addstudent VALUES(:a,:b,:c,:d,:e,:f,:g,:h,:i)",
              {
                  'a': e1.get(),
                  'b': g,
                  'c': e3.get(),
                  'd': e4.get(),
                  'e': e5.get(),
                  'f': e6.get(),
                  'g': e7.get(),
                  'h': e8.get(),
                  'i': e9.get()
              }
              )

        conn.commit()
        conn.close()

        e1.delete(0, END)
        r.set("1")
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)

    else:
        e1.delete(0, END)
        r.set("1")
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)

def main():

    global e1,e2,e3,e4,e5,e6,e7,e8,e9,r

    r = IntVar()
    r.set("1")

    l1=Label(top,text="Name :",font=("Calibri (Body)",15),bg="#7CFC00")
    l2=Label(top,text="Gender :",font=("Calibri (Body)",15),bg="#7CFC00")
    l3=Label(top,text="Class :",font=("Calibri (Body)",15),bg="#7CFC00")
    l4=Label(top,text="Section :",font=("Calibri (Body)",15),bg="#7CFC00")
    l5=Label(top,text="Roll No :",font=("Calibri (Body)",15),bg="#7CFC00")
    l6=Label(top,text="Address :",font=("Calibri (Body)",15),bg="#7CFC00")
    l7=Label(top,text="Contact No :",font=("Calibri (Body)",15),bg="#7CFC00")
    l8=Label(top,text="Father's Name :",font=("Calibri (Body)",15),bg="#7CFC00")
    l9=Label(top,text="Mother's Name :",font=("Calibri (Body)",15),bg="#7CFC00")

    e1=Entry(top,width=30,font=("Calibri (Body)",15))
    e2=Radiobutton(top,text="Male",variable=r,value=1,bg="#7CFC00",activebackground="#7CFC00",font=("Calibri (Body)",13),command=lambda:check())
    e21=Radiobutton(top,text="Female",variable=r,value=2,bg="#7CFC00",activebackground="#7CFC00",font=("Calibri (Body)",13),command=lambda:check())
    e22=Radiobutton(top,text="Other",variable=r,value=3,bg="#7CFC00",activebackground="#7CFC00",font=("Calibri (Body)",13),command=lambda:check())
    e3=Entry(top,width=30,font=("Calibri (Body)",15))
    e4=Entry(top,width=30,font=("Calibri (Body)",15))
    e5=Entry(top,width=30,font=("Calibri (Body)",15))
    e6=Entry(top,width=30,font=("Calibri (Body)",15))
    e7=Entry(top,width=30,font=("Calibri (Body)",15))
    e8=Entry(top,width=30,font=("Calibri (Body)",15))
    e9=Entry(top,width=30,font=("Calibri (Body)",15))

    l1.place(relx=0.04,rely=0.24,anchor=W)
    e1.place(relx=0.44,rely=0.24,anchor=CENTER)
    l2.place(relx=0.04,rely=0.29,anchor=W)
    e2.place(relx=0.3,rely=0.29,anchor=CENTER)
    e21.place(relx=0.44,rely=0.29,anchor=CENTER)
    e22.place(relx=0.6,rely=0.29,anchor=CENTER)
    l3.place(relx=0.04,rely=0.34,anchor=W)
    e3.place(relx=0.44,rely=0.34,anchor=CENTER)
    l4.place(relx=0.04,rely=0.39,anchor=W)
    e4.place(relx=0.44,rely=0.39,anchor=CENTER)
    l5.place(relx=0.04,rely=0.44,anchor=W)
    e5.place(relx=0.44,rely=0.44,anchor=CENTER)
    l6.place(relx=0.04,rely=0.49,anchor=W)
    e6.place(relx=0.44,rely=0.49,anchor=CENTER)
    l7.place(relx=0.04,rely=0.54,anchor=W)
    e7.place(relx=0.44,rely=0.54,anchor=CENTER)
    l8.place(relx=0.04,rely=0.59,anchor=W)
    e8.place(relx=0.44,rely=0.59,anchor=CENTER)
    l9.place(relx=0.04,rely=0.64,anchor=W)
    e9.place(relx=0.44,rely=0.64,anchor=CENTER)

    b1=Button(top,text="Submit",width=20,font=("Times New Roman",20),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=submit)
    b1.place(relx=0.24,rely=0.75,anchor=CENTER)

    b2=Button(top,text="Back",width=20,font=("Times New Roman",20),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=lambda:back())
    b2.place(relx=0.74,rely=0.75,anchor=CENTER)

    l = Label(top, text="Student Database App",font=("Times New Roman",40),bg="#7CFC00",fg="#008000")
    l.place(relx=0.5,rely=0.09,anchor=CENTER)



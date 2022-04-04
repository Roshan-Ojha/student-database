from tkinter import *
import sqlite3
import tkinter.messagebox
def show_student():
    global root
    root=Tk()
    root.geometry("800x600")
    root.geometry("+275+70")
    root.configure(bg="#7CFC00")
    root.title("Detail of Student")
    main()
    root.resizable(False, False)
    root.mainloop()

def original():
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    l6.destroy()
    l7.destroy()
    l8.destroy()
    l9.destroy()
    l11.destroy()
    l22.destroy()
    l33.destroy()
    l44.destroy()
    l55.destroy()
    l66.destroy()
    l77.destroy()
    l88.destroy()
    l99.destroy()
    b21.destroy()
    main()

def view():

    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l11,l22,l33,l44,l55,l66,l77,l88,l99,b21

    conn=sqlite3.connect('Add.db')
    c=conn.cursor()
    c.execute("SELECT * FROM addstudent WHERE class=:a AND roll=:b",
              {
                  'a': e1.get(),
                  'b': e2.get()
              })
    data=c.fetchall()

    conn.commit()
    conn.close()

    if data==[]:
        tkinter.messagebox.showerror("Record Not Found","Sorry no such record in the database.")
        e1.delete(0,END)
        e2.delete(0,END)
    else:
        l111.destroy()
        l222.destroy()
        e1.destroy()
        e2.destroy()
        b1.destroy()
        b2.destroy()
        da=data[0]
        l1 = Label(root, text="Name :", font=("Calibri (Body)", 15), bg="#7CFC00",)
        l2 = Label(root, text="Gender :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l3 = Label(root, text="Class :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l4 = Label(root, text="Section :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l5 = Label(root, text="Roll No :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l6 = Label(root, text="Address :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l7 = Label(root, text="Contact No :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l8 = Label(root, text="Father's Name :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l9 = Label(root, text="Mother's Name :", font=("Calibri (Body)", 15), bg="#7CFC00")

        l11 = Label(root, text=da[0], width=30,font=("Calibri (Body)", 15), bg="#7CFC00",relief="sunken")
        l22 = Label(root, text=da[1], width=30,font=("Calibri (Body)", 15), bg="#7CFC00",relief="sunken")
        l33 = Label(root, text=da[2], width=30,font=("Calibri (Body)", 15), bg="#7CFC00",relief="sunken")
        l44 = Label(root, text=da[3], width=30,font=("Calibri (Body)", 15), bg="#7CFC00",relief="sunken")
        l55 = Label(root, text=da[4], width=30,font=("Calibri (Body)", 15), bg="#7CFC00",relief="sunken")
        l66 = Label(root, text=da[5], width=30,font=("Calibri (Body)", 15), bg="#7CFC00",relief="sunken")
        l77 = Label(root, text=da[6], width=30,font=("Calibri (Body)", 15), bg="#7CFC00",relief="sunken")
        l88 = Label(root, text=da[7], width=30,font=("Calibri (Body)", 15), bg="#7CFC00",relief="sunken")
        l99 = Label(root, text=da[8], width=30,font=("Calibri (Body)", 15), bg="#7CFC00",relief="sunken")

        l1.place(relx=0.2,rely=0.24,anchor=W)
        l11.place(relx=0.4,rely=0.24,anchor=W)
        l2.place(relx=0.2, rely=0.29, anchor=W)
        l22.place(relx=0.4, rely=0.29, anchor=W)
        l3.place(relx=0.2, rely=0.34, anchor=W)
        l33.place(relx=0.4, rely=0.34, anchor=W)
        l4.place(relx=0.2, rely=0.39, anchor=W)
        l44.place(relx=0.4, rely=0.39, anchor=W)
        l5.place(relx=0.2, rely=0.44, anchor=W)
        l55.place(relx=0.4, rely=0.44, anchor=W)
        l6.place(relx=0.2, rely=0.49, anchor=W)
        l66.place(relx=0.4, rely=0.49, anchor=W)
        l7.place(relx=0.2, rely=0.54, anchor=W)
        l77.place(relx=0.4, rely=0.54, anchor=W)
        l8.place(relx=0.2, rely=0.59, anchor=W)
        l88.place(relx=0.4, rely=0.59, anchor=W)
        l9.place(relx=0.2, rely=0.64, anchor=W)
        l99.place(relx=0.4, rely=0.64, anchor=W)

        b21=Button(root,text="Back",width=6,font=("Times New Roman",15),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=original)
        b21.place(relx=0.20,rely=0.7)


def back():

   root.destroy()
   import Login_page
   Login_page.Login_page()

def main():
    global l111,l222,e1,e2,b1,b2

    l111 = Label(root, text="Enter Class :", font=("Calibri (Body)", 15), bg="#7CFC00")
    l222 = Label(root,text="Enter Roll No :",font=("Calibri (Body)",15),bg="#7CFC00")

    e1 = Entry(root,width=30,font=("Calibri (Body)",15))
    e2 = Entry(root,width=30,font=("Calibri (Body)",15))

    l111.place(relx=0.20,rely=0.24,anchor=W)
    e1.place(relx=0.59,rely=0.24,anchor=CENTER)

    l222.place(relx=0.20,rely=0.34,anchor=W)
    e2.place(relx=0.59,rely=0.34,anchor=CENTER)

    b1=Button(root,text="View",width=6,font=("Times New Roman",15),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=view)
    b2=Button(root,text="Back",width=6,font=("Times New Roman",15),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=back)

    b1.place(relx=0.22,rely=0.45,anchor=W)
    b2.place(relx=0.71,rely=0.45,anchor=W)

    l = Label(root, text="Student Database Software",font=("Times New Roman",40),bg="#7CFC00",fg="#008000")
    l.place(relx=0.5,rely=0.09,anchor=CENTER)



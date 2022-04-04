from tkinter import *
import sqlite3
import tkinter.messagebox
def delete_record():

    global root
    root=Tk()
    root.geometry("800x600")
    root.geometry("+275+70")
    root.configure(bg="#7CFC00")
    root.title("Delete Record")
    main()
    root.resizable(False, False)
    root.mainloop()


def delete():
    conn=sqlite3.connect('Add.db')
    c=conn.cursor()
    c.execute("SELECT * FROM addstudent WHERE class=:a AND roll=:b",
                {
                    'a':e1.get(),
                    'b':e2.get()
                })
    data=c.fetchall()
    if data==[]:
        tkinter.messagebox.showerror("Data not found","Sorry no such record in the database.")
        e1.delete(0,END)
        e2.delete(0,END)

    else:
        ans=tkinter.messagebox.askquestion("Delete Recoed","Are you sure you want to delete this record?")
        if ans=="yes":
            c.execute("DELETE FROM addstudent WHERE class=:q AND roll=:w",
                      {
                          'q':e1.get(),
                          'w':e2.get()
                      })
            conn.commit()
            conn.close()
            con=sqlite3.connect('Marks.db')
            cn=con.cursor()
            cn.execute("DELETE FROM mark WHERE class=:x AND roll=:y",
                       {
                           'x':e1.get(),
                           'y':e2.get()
                       })
            con.commit()
            con.close()
            e1.delete(0,END)
            e2.delete(0,END)
        else:
            e1.delete(0,END)
            e2.delete(0,END)




def back():
    root.destroy()
    import Login_page
    Login_page.Login_page()


def main():
    global e1,e2

    l111 = Label(root, text="Enter Class :", font=("Calibri (Body)", 15), bg="#7CFC00")
    l222 = Label(root,text="Enter Roll No :",font=("Calibri (Body)",15),bg="#7CFC00")

    e1 = Entry(root,width=30,font=("Calibri (Body)",15))
    e2 = Entry(root,width=30,font=("Calibri (Body)",15))

    l111.place(relx=0.20,rely=0.24,anchor=W)
    e1.place(relx=0.59,rely=0.24,anchor=CENTER)

    l222.place(relx=0.20,rely=0.34,anchor=W)
    e2.place(relx=0.59,rely=0.34,anchor=CENTER)

    b1=Button(root,text="Delete",width=6,font=("Times New Roman",15),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=delete)
    b2=Button(root,text="Back",width=6,font=("Times New Roman",15),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=back)

    b1.place(relx=0.22,rely=0.45,anchor=W)
    b2.place(relx=0.71,rely=0.45,anchor=W)

    l = Label(root, text="Student Database Software",font=("Times New Roman",40),bg="#7CFC00",fg="#008000")
    l.place(relx=0.5,rely=0.09,anchor=CENTER)





from tkinter import *
import sqlite3
import tkinter.messagebox
def add_marks():
    global root
    root=Tk()
    root.geometry("800x600")
    root.geometry("+275+70")
    root.configure(bg="#7CFC00")
    root.title("Add Marks")
    main()
    root.resizable(False, False)
    root.mainloop()

def back1():
    e1t.destroy()
    e1p.destroy()
    e2t.destroy()
    e2p.destroy()
    e3.destroy()
    e4t.destroy()
    e4p.destroy()
    e5t.destroy()
    e5p.destroy()
    e6t.destroy()
    e6p.destroy()
    e7.destroy()
    e8t.destroy()
    e8p.destroy()
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    l6.destroy()
    l7.destroy()
    l8.destroy()
    ln.destroy()
    lc.destroy()
    ls.destroy()
    lr.destroy()
    lnl.destroy()
    lcl.destroy()
    lsl.destroy()
    lrl.destroy()
    lt.destroy()
    lp.destroy()
    submit_button.destroy()
    back_button.destroy()
    start()

def submit():
    con=sqlite3.connect('Marks.db')
    cu=con.cursor()
    cu.execute("""INSERT INTO mark VALUES(
                    :name,
                    :class,
                    :sec,
                    :roll,
                    :english_theory,
                    :english_practical,
                    :nepali_theory,
                    :nepali_practical,
                    :maths,
                    :science_theory,
                    :science_practical,
                    :social_theory,
                    :social_practical,
                    :eph_theory,
                    :eph_practical,
                    :opt_i,
                    :opt_ii_theory,
                    :opt_ii_practical)""",
               {
                   'name': da[0],
                   'class': da[2],
                   'sec': da[3],
                   'roll': da[4],
                   'english_theory': e1t.get(),
                   'english_practical': e1p.get(),
                   'nepali_theory': e2t.get(),
                   'nepali_practical': e2p.get(),
                   'maths': e3.get(),
                   'science_theory': e4t.get(),
                   'science_practical': e4p.get(),
                   'social_theory': e5t.get(),
                   'social_practical': e5p.get(),
                   'eph_theory': e6t.get(),
                   'eph_practical': e6p.get(),
                   'opt_i': e7.get(),
                   'opt_ii_theory': e8t.get(),
                   'opt_ii_practical': e8p.get()
               })


    con.commit()
    con.close()
    e1t.delete(0, END)
    e1p.delete(0,END)
    e2t.delete(0, END)
    e2p.delete(0, END)
    e3.delete(0, END)
    e4t.delete(0, END)
    e4p.delete(0, END)
    e5t.delete(0, END)
    e5p.delete(0, END)
    e6t.delete(0, END)
    e6p.delete(0, END)
    e7.delete(0, END)
    e8t.delete(0, END)
    e8p.delete(0, END)

def add():
    connect=sqlite3.connect('Marks.db')
    cur=connect.cursor()
    cur.execute("SELECT * FROM mark WHERE class=:class AND roll=:roll",
                {
                    'class':e11.get(),
                    'roll':e22.get()
                })
    check=cur.fetchall()
    connect.commit()
    connect.close()

    conn=sqlite3.connect('Add.db')
    c=conn.cursor()
    c.execute("SELECT * FROM addstudent WHERE class=:a AND roll=:b",
              {
                  'a':e11.get(),
                  'b':e22.get()
              })
    data=c.fetchall()
    conn.commit()
    conn.close()
    if data==[]:
        tkinter.messagebox.showerror("Data Not Found","Sorry no such record in the database.")

    elif not check == []:
        tkinter.messagebox.showerror("Data already exists", "This data already exists in the database")

    else:
        global e1t,e1p,e2t,e2p,e3,e4t,e4p,e5t,e5p,e6t,e6p,e7,e8t,e8p,da,l1,l2,l3,l4,l5,l6,l7,l8,ln,lc,ls,lr,lnl,lcl,lsl,lrl,lt,lp,submit_button,back_button
        da=data[0]
        l111.destroy()
        l222.destroy()
        e11.destroy()
        e22.destroy()
        b1.destroy()
        b2.destroy()
        l1 = Label(root, text="English :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l2 = Label(root, text="Nepali :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l3 = Label(root, text="Mathematics :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l4 = Label(root, text="Science :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l5 = Label(root, text="Social :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l6 = Label(root, text="EPH :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l7 = Label(root, text="OPT I :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l8 = Label(root, text="OPT II :", font=("Calibri (Body)", 15), bg="#7CFC00")
        ln = Label(root,text="Name: ",font=("Calibri (Body)", 15), bg="#7CFC00")
        lc = Label(root,text="Class: ",font=("Calibri (Body)", 15), bg="#7CFC00")
        ls = Label(root,text="Section: ",font=("Calibri (Body)", 15), bg="#7CFC00")
        lr = Label(root,text="Roll No: ",font=("Calibri (Body)", 15), bg="#7CFC00")
        lnl = Label(root,text=da[0],font=("Calibri (Body)", 15), bg="#7CFC00")
        lcl = Label(root, text=da[2], font=("Calibri (Body)", 15), bg="#7CFC00")
        lsl = Label(root, text=da[3], font=("Calibri (Body)", 15), bg="#7CFC00")
        lrl = Label(root, text=da[4], font=("Calibri (Body)", 15), bg="#7CFC00")
        lt = Label(root, text="Theory", font=("Calibri (Body)", 15), bg="#7CFC00",relief="ridge",width=10)
        lp = Label(root, text="Practical", font=("Calibri (Body)", 15), bg="#7CFC00",relief="ridge",width=10)

        e1t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e1p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e2t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e2p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e3 = Entry(root, width=10, font=("Calibri (Body)", 15))
        e4t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e4p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e5t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e5p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e6t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e6p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e7 = Entry(root, width=10, font=("Calibri (Body)", 15))
        e8t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e8p = Entry(root, width=10, font=("Calibri (Body)", 15))

        l1.place(relx=0.04, rely=0.27, anchor=W)
        e1t.place(relx=0.30, rely=0.27, anchor=CENTER)
        e1p.place(relx=0.45,rely=0.27,anchor=CENTER)
        l2.place(relx=0.04, rely=0.32, anchor=W)
        e2t.place(relx=0.30, rely=0.32, anchor=CENTER)
        e2p.place(relx=0.45,rely=0.32,anchor=CENTER)
        l3.place(relx=0.04, rely=0.37, anchor=W)
        e3.place(relx=0.30, rely=0.37, anchor=CENTER)
        l4.place(relx=0.04, rely=0.42, anchor=W)
        e4t.place(relx=0.30, rely=0.42, anchor=CENTER)
        e4p.place(relx=0.45,rely=0.42,anchor=CENTER)
        l5.place(relx=0.04, rely=0.47, anchor=W)
        e5t.place(relx=0.30, rely=0.47, anchor=CENTER)
        e5p.place(relx=0.45,rely=0.47,anchor=CENTER)
        l6.place(relx=0.04, rely=0.52, anchor=W)
        e6t.place(relx=0.30, rely=0.52, anchor=CENTER)
        e6p.place(relx=0.45,rely=0.52,anchor=CENTER)
        l7.place(relx=0.04, rely=0.57, anchor=W)
        e7.place(relx=0.30, rely=0.57, anchor=CENTER)
        l8.place(relx=0.04, rely=0.62, anchor=W)
        e8t.place(relx=0.30, rely=0.62, anchor=CENTER)
        e8p.place(relx=0.45,rely=0.62,anchor=CENTER)
        ln.place(relx=0.68,rely=0.27, anchor=W)
        lc.place(relx=0.68, rely=0.32, anchor=W)
        ls.place(relx=0.68, rely=0.37, anchor=W)
        lr.place(relx=0.68 , rely=0.42, anchor=W)
        lnl.place(relx=0.78, rely=0.27, anchor=W)
        lcl.place(relx=0.78, rely=0.32, anchor=W)
        lsl.place(relx=0.78, rely=0.37, anchor=W)
        lrl.place(relx=0.78 , rely=0.42, anchor=W)
        lt.place(relx=0.30,rely=0.22,anchor=CENTER)
        lp.place(relx=0.45,rely=0.22,anchor=CENTER)

        submit_button=Button(root,text="Submit",width=10,font=("Times New Roman",15),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=submit)
        submit_button.place(relx=0.305, rely=0.69, anchor=CENTER)

        back_button=Button(root,text="Back",width=10,font=("Times New Roman",15),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=back1)
        back_button.place(relx=0.55,rely=0.69,anchor=CENTER)


def back():
    root.destroy()
    import Login_page
    Login_page.Login_page()

def start():

    global e11,e22,l111,l222,b1,b2

    l111 = Label(root, text="Enter Class :", font=("Calibri (Body)", 15), bg="#7CFC00")
    l222 = Label(root,text="Enter Roll No :",font=("Calibri (Body)",15),bg="#7CFC00")

    e11 = Entry(root,width=30,font=("Calibri (Body)",15))
    e22 = Entry(root,width=30,font=("Calibri (Body)",15))

    l111.place(relx=0.20,rely=0.24,anchor=W)
    e11.place(relx=0.59,rely=0.24,anchor=CENTER)

    l222.place(relx=0.20,rely=0.34,anchor=W)
    e22.place(relx=0.59,rely=0.34,anchor=CENTER)

    b1=Button(root,text="Add Marks",width=10,font=("Times New Roman",15),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=add)
    b2=Button(root,text="Back",width=6,font=("Times New Roman",15),activebackground="#228B22",bg="#32CD32",fg="dark blue",activeforeground="dark blue",command=back)

    b1.place(relx=0.22,rely=0.45,anchor=W)
    b2.place(relx=0.71,rely=0.45,anchor=W)



def main():
    l = Label(root, text="Student Database Software",font=("Times New Roman",40),bg="#7CFC00",fg="#008000")
    l.place(relx=0.5,rely=0.09,anchor=CENTER)
    start()

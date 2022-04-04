from tkinter import *
import sqlite3
import tkinter.messagebox
def modify():
    global root
    root=Tk()
    root.geometry("800x600")
    root.geometry("+275+70")
    root .configure(bg="#7CFC00")
    root.title("Add Student")
    main()
    root.resizable(False, False)
    root.mainloop()

def back():
    root.destroy()
    import Login_page
    Login_page.Login_page()

def destructionmark():
    l11.destroy()
    l22.destroy()
    l33.destroy()
    l44.destroy()
    l55.destroy()
    l66.destroy()
    l77.destroy()
    l88.destroy()
    ln.destroy()
    lc.destroy()
    ls.destroy()
    lr.destroy()
    lt.destroy()
    lp.destroy()
    e1t.destroy()
    e1p.destroy()
    e2t.destroy()
    e2p.destroy()
    e3t.destroy()
    e4t.destroy()
    e4p.destroy()
    e5t.destroy()
    e5p.destroy()
    e6t.destroy()
    e6p.destroy()
    e7t.destroy()
    e8t.destroy()
    e8p.destroy()
    submit_btn.destroy()
    back_btn.destroy()
    lnl.destroy()
    lcl.destroy()
    lsl.destroy()
    lrl.destroy()
    main()

def destructiondetail():
    e1.destroy()
    e3.destroy()
    e4.destroy()
    e5.destroy()
    e6.destroy()
    e7.destroy()
    e8.destroy()
    e9.destroy()
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    l6.destroy()
    l7.destroy()
    l8.destroy()
    l9.destroy()
    e2.destroy()
    e21.destroy()
    e221.destroy()
    submit_button.destroy()
    back_button.destroy()
    main()
def check():
    global g
    if r.get()==1:
        g="Male"
    elif r.get()==2:
        g="Female"
    elif r.get()==3:
        g="Other"

def updatemark(cno,rno):
    print(cno)
    print(rno)
    ans=tkinter.messagebox.askquestion("Student Database","Are you sure you want to update this record")
    if ans=="yes":

        conn=sqlite3.connect('Marks.db')
        c=conn.cursor()
        c.execute("""UPDATE mark SET
                    
                    english_theory=:a,
                    english_practical=:b,
                    nepali_theory=:c,
                    nepali_practical=:d,
                    mathematics=:e,
                    science_theory=:f,
                    science_practical=:g,
                    social_theory=:h,
                    social_practical=:i,
                    eph_theory=:j,
                    eph_practical=:k,
                    opt_i=:l,
                    opt_ii_theory=:m,
                    opt_ii_practical=:n
                    WHERE class=:o AND roll=:p
                    """,
                  {
                      'a': e1t.get(),
                      'b': e1p.get(),
                      'c': e2t.get(),
                      'd': e2p.get(),
                      'e': e3t.get(),
                      'f': e4t.get(),
                      'g': e4p.get(),
                      'h': e5t.get(),
                      'i': e5p.get(),
                      'j': e6t.get(),
                      'k': e6p.get(),
                      'l': e7t.get(),
                      'm': e8t.get(),
                      'n': e8p.get(),
                      'o': cno,
                      'p': rno,

                  })

        tkinter.messagebox.showinfo("Record Updated", "This data is successfully updated.")
        conn.commit()
        conn.close()
        l111.destroy()
        l222.destroy()
        e111.destroy()
        e222.destroy()
        b1.destroy()
        b2.destroy()


def updatedetail():
    global classnumber,rollnumber
    classnumber=cno
    rollnumbet=rno
    check()
    ans=tkinter.messagebox.askquestion("Student Database","Are you sure you want to update this record?")
    if ans =="yes":
        conn=sqlite3.connect('Add.db')
        c=conn.cursor()
        c.execute("""UPDATE addstudent SET
                        name=:a,
                        gender=:b,
                        class=:c,
                        sec=:d,
                        roll=:e,
                        address=:f,
                        contact=:g,
                        father_name=:h,
                        mother_name=:i
                        WHERE class=:cl AND roll=:rn
                        """,
                  {
                      'a': e1.get(),
                      'b': g,
                      'c': e3.get(),
                      'd': e4.get(),
                      'e': e5.get(),
                      'f': e6.get(),
                      'g': e7.get(),
                      'h': e8.get(),
                      'i': e9.get(),
                      'cl':cno,
                      'rn':rno
                  })
        conn2=sqlite3.connect('Marks.db')
        c2=conn2.cursor()

        c2.execute("""UPDATE mark SET
                    name=:name,
                    class=:class,
                    sec=:sec,
                    roll=:roll
                    WHERE class=:cl2 AND roll=:rl2 
                    """,
                   {
                       'name':e1.get(),
                       'class':e3.get(),
                       'sec':e4.get(),
                       'roll':e5.get(),
                       'cl2':cno,
                       'rl2':rno
                   })


        conn2.commit()
        conn2.close()
        tkinter.messagebox.showinfo("Record Updated","This data is successfully updated.")
        conn.commit()
        conn.close()
        l111.destroy()
        l222.destroy()
        e111.destroy()
        e222.destroy()
        b1.destroy()
        b2.destroy()


def record():

    global r,e1,e3,e4,e5,e6,e7,e8,e9,l1,l2,l3,l4,l5,l6,l7,l8,l9,e2,e21,e221,submit_button,back_button,cno,rno
    cno = e111.get()
    rno = e222.get()
    conn=sqlite3.connect('Add.db')
    c=conn.cursor()
    c.execute("SELECT * FROM addstudent WHERE class=:a AND roll=:b",
              {
                  'a':e111.get(),
                  'b':e222.get()
              })
    dat=c.fetchall()

    conn.commit()
    conn.close()

    if dat==[]:
        tkinter.messagebox.showerror("Record Not Found","Sorry no such record in the database.")
    else:
        backbtn.destroy()
        b1.destroy()
        b2.destroy()
        l111.destroy()
        l222.destroy()
        e111.destroy()
        e222.destroy()

        r = IntVar()
        if dat[0][1]=="Male":
            r.set("1")
        elif dat[0][1]=="Female":
            r.set("2")
        else:
            r.set("3")

        l1 = Label(root, text="Name :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l2 = Label(root, text="Gender :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l3 = Label(root, text="Class :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l4 = Label(root, text="Section :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l5 = Label(root, text="Roll No :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l6 = Label(root, text="Address :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l7 = Label(root, text="Contact No :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l8 = Label(root, text="Father's Name :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l9 = Label(root, text="Mother's Name :", font=("Calibri (Body)", 15), bg="#7CFC00")

        e1 = Entry(root, width=30, font=("Calibri (Body)", 15))
        e1.insert(0,dat[0][0])
        e2 = Radiobutton(root, text="Male", variable=r, value=1, bg="#7CFC00", activebackground="#7CFC00",font=("Calibri (Body)", 13), command=lambda: check())
        e21 = Radiobutton(root, text="Female", variable=r, value=2, bg="#7CFC00", activebackground="#7CFC00",font=("Calibri (Body)", 13), command=lambda: check())
        e221 = Radiobutton(root, text="Other", variable=r, value=3, bg="#7CFC00", activebackground="#7CFC00",font=("Calibri (Body)", 13), command=lambda: check())
        e3 = Entry(root, width=30, font=("Calibri (Body)", 15))
        e3.insert(0,dat[0][2])
        e4 = Entry(root, width=30, font=("Calibri (Body)", 15))
        e4.insert(0,dat[0][3])
        e5 = Entry(root, width=30, font=("Calibri (Body)", 15))
        e5.insert(0,dat[0][4])
        e6 = Entry(root, width=30, font=("Calibri (Body)", 15))
        e6.insert(0,dat[0][5])
        e7 = Entry(root, width=30, font=("Calibri (Body)", 15))
        e7.insert(0,dat[0][6])
        e8 = Entry(root, width=30, font=("Calibri (Body)", 15))
        e8.insert(0,dat[0][7])
        e9 = Entry(root, width=30, font=("Calibri (Body)", 15))
        e9.insert(0,dat[0][8])

        l1.place(relx=0.04, rely=0.24, anchor=W)
        e1.place(relx=0.44, rely=0.24, anchor=CENTER)
        l2.place(relx=0.04, rely=0.29, anchor=W)
        e2.place(relx=0.3, rely=0.29, anchor=CENTER)
        e21.place(relx=0.44, rely=0.29, anchor=CENTER)
        e221.place(relx=0.6, rely=0.29, anchor=CENTER)
        l3.place(relx=0.04, rely=0.34, anchor=W)
        e3.place(relx=0.44, rely=0.34, anchor=CENTER)
        l4.place(relx=0.04, rely=0.39, anchor=W)
        e4.place(relx=0.44, rely=0.39, anchor=CENTER)
        l5.place(relx=0.04, rely=0.44, anchor=W)
        e5.place(relx=0.44, rely=0.44, anchor=CENTER)
        l6.place(relx=0.04, rely=0.49, anchor=W)
        e6.place(relx=0.44, rely=0.49, anchor=CENTER)
        l7.place(relx=0.04, rely=0.54, anchor=W)
        e7.place(relx=0.44, rely=0.54, anchor=CENTER)
        l8.place(relx=0.04, rely=0.59, anchor=W)
        e8.place(relx=0.44, rely=0.59, anchor=CENTER)
        l9.place(relx=0.04, rely=0.64, anchor=W)
        e9.place(relx=0.44, rely=0.64, anchor=CENTER)

        submit_button = Button(root, text="Update", width=15, font=("Times New Roman", 20), activebackground="#228B22",bg="#32CD32", fg="dark blue", activeforeground="dark blue", command=updatedetail)
        submit_button.place(relx=0.24, rely=0.75, anchor=CENTER)
        back_button = Button(root,text="Back", width=15, font=("Times New Roman", 20), activebackground="#228B22",bg="#32CD32", fg="dark blue", activeforeground="dark blue", command=destructiondetail)
        back_button.place(relx=0.55,rely=0.75,anchor=CENTER)



def mark():

    cno=e111.get()
    rno=e222.get()

    global l11,l22,l33,l44,l55,l66,l77,l88,ln,lc,ls,lr,lt,lp,e1t,e1p,e2t,e2p,e3t,e4t,e4p,e5t,e5p,e6t,e6p,e7t,e8t,e8p,submit_btn,back_btn,lnl,lcl,lsl,lrl

    con=sqlite3.connect('Marks.db')
    cn=con.cursor()
    cn.execute("SELECT * FROM mark WHERE class=:class and roll=:roll",
              {
                  'class':e111.get(),
                  'roll':e222.get()
              })
    data=cn.fetchall()
    con.commit()
    con.close()
    if data==[]:
        tkinter.messagebox.showerror("Record Not Found","Sorry no such record in the database.")
    else:
        backbtn.destroy()
        b1.destroy()
        b2.destroy()
        l111.destroy()
        l222.destroy()
        e111.destroy()
        e222.destroy()
        l11 = Label(root, text="English :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l22 = Label(root, text="Nepali :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l33 = Label(root, text="Mathematics :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l44 = Label(root, text="Science :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l55 = Label(root, text="Social :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l66 = Label(root, text="EPH :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l77 = Label(root, text="OPT I :", font=("Calibri (Body)", 15), bg="#7CFC00")
        l88 = Label(root, text="OPT II :", font=("Calibri (Body)", 15), bg="#7CFC00")
        ln = Label(root, text="Name: ", font=("Calibri (Body)", 15), bg="#7CFC00")
        lc = Label(root, text="Class: ", font=("Calibri (Body)", 15), bg="#7CFC00")
        ls = Label(root, text="Section: ", font=("Calibri (Body)", 15), bg="#7CFC00")
        lr = Label(root, text="Roll No: ", font=("Calibri (Body)", 15), bg="#7CFC00")
        lnl = Label(root, text=data[0][0], font=("Calibri (Body)", 15), bg="#7CFC00")
        lcl = Label(root, text=data[0][1], font=("Calibri (Body)", 15), bg="#7CFC00")
        lsl = Label(root, text=data[0][2], font=("Calibri (Body)", 15), bg="#7CFC00")
        lrl = Label(root, text=data[0][3], font=("Calibri (Body)", 15), bg="#7CFC00")
        lt = Label(root, text="Theory", font=("Calibri (Body)", 15), bg="#7CFC00", relief="ridge", width=10)
        lp = Label(root, text="Practical", font=("Calibri (Body)", 15), bg="#7CFC00", relief="ridge", width=10)

        e1t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e1t.insert(0,data[0][4])
        e1p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e1p.insert(0,data[0][5])
        e2t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e2t.insert(0,data[0][6])
        e2p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e2p.insert(0,data[0][7])
        e3t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e3t.insert(0,data[0][8])
        e4t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e4t.insert(0,data[0][9])
        e4p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e4p.insert(0,data[0][10])
        e5t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e5t.insert(0,data[0][11])
        e5p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e5p.insert(0,data[0][12])
        e6t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e6t.insert(0,data[0][13])
        e6p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e6p.insert(0,data[0][14])
        e7t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e7t.insert(0,data[0][15])
        e8t = Entry(root, width=10, font=("Calibri (Body)", 15))
        e8t.insert(0,data[0][16])
        e8p = Entry(root, width=10, font=("Calibri (Body)", 15))
        e8p.insert(0,data[0][17])

        l11.place(relx=0.04, rely=0.27, anchor=W)
        e1t.place(relx=0.30, rely=0.27, anchor=CENTER)
        e1p.place(relx=0.45, rely=0.27, anchor=CENTER)
        l22.place(relx=0.04, rely=0.32, anchor=W)
        e2t.place(relx=0.30, rely=0.32, anchor=CENTER)
        e2p.place(relx=0.45, rely=0.32, anchor=CENTER)
        l33.place(relx=0.04, rely=0.37, anchor=W)
        e3t.place(relx=0.30, rely=0.37, anchor=CENTER)
        l44.place(relx=0.04, rely=0.42, anchor=W)
        e4t.place(relx=0.30, rely=0.42, anchor=CENTER)
        e4p.place(relx=0.45, rely=0.42, anchor=CENTER)
        l55.place(relx=0.04, rely=0.47, anchor=W)
        e5t.place(relx=0.30, rely=0.47, anchor=CENTER)
        e5p.place(relx=0.45, rely=0.47, anchor=CENTER)
        l66.place(relx=0.04, rely=0.52, anchor=W)
        e6t.place(relx=0.30, rely=0.52, anchor=CENTER)
        e6p.place(relx=0.45, rely=0.52, anchor=CENTER)
        l77.place(relx=0.04, rely=0.57, anchor=W)
        e7t.place(relx=0.30, rely=0.57, anchor=CENTER)
        l88.place(relx=0.04, rely=0.62, anchor=W)
        e8t.place(relx=0.30, rely=0.62, anchor=CENTER)
        e8p.place(relx=0.45, rely=0.62, anchor=CENTER)
        ln.place(relx=0.68, rely=0.27, anchor=W)
        lc.place(relx=0.68, rely=0.32, anchor=W)
        ls.place(relx=0.68, rely=0.37, anchor=W)
        lr.place(relx=0.68, rely=0.42, anchor=W)
        lnl.place(relx=0.78, rely=0.27, anchor=W)
        lcl.place(relx=0.78, rely=0.32, anchor=W)
        lsl.place(relx=0.78, rely=0.37, anchor=W)
        lrl.place(relx=0.78, rely=0.42, anchor=W)
        lt.place(relx=0.30, rely=0.22, anchor=CENTER)
        lp.place(relx=0.45, rely=0.22, anchor=CENTER)
        submit_btn = Button(root, text="Update", width=15, font=("Times New Roman", 20), activebackground="#228B22",bg="#32CD32", fg="dark blue", activeforeground="dark blue", command=lambda:updatemark(cno,rno))
        submit_btn.place(relx=0.24, rely=0.75, anchor=CENTER)
        back_btn = Button(root, text="Back", width=15, font=("Times New Roman", 20), activebackground="#228B22",bg="#32CD32", fg="dark blue", activeforeground="dark blue", command=destructionmark)
        back_btn.place(relx=0.55, rely=0.75, anchor=CENTER)



def main():


    global l111,l222,e111,e222,b1,b2,backbtn


    l111 = Label(root, text="Enter Class :", font=("Calibri (Body)", 15), bg="#7CFC00")
    l222 = Label(root, text="Enter Roll No :", font=("Calibri (Body)", 15), bg="#7CFC00")

    e111 = Entry(root, width=30, font=("Calibri (Body)", 15))
    e222 = Entry(root, width=30, font=("Calibri (Body)", 15))

    l111.place(relx=0.20, rely=0.24, anchor=W)
    e111.place(relx=0.59, rely=0.24, anchor=CENTER)

    l222.place(relx=0.20, rely=0.34, anchor=W)
    e222.place(relx=0.59, rely=0.34, anchor=CENTER)

    b1 = Button(root, text="Modify General Detail", width=20, font=("Times New Roman", 15), activebackground="#228B22",bg="#32CD32", fg="dark blue", activeforeground="dark blue", command=record)
    b1.place(relx=0.35, rely=0.44, anchor=CENTER)
    b2 = Button(text="Modify Student's Marks", width=20, font=("Times New Roman", 15), activebackground="#228B22",bg="#32CD32", fg="dark blue", activeforeground="dark blue", command=mark)
    b2.place(relx=0.65, rely=0.44, anchor=CENTER)
    l = Label(root, text="Student Database Software", font=("Times New Roman", 40), bg="#7CFC00", fg="#008000")
    l.place(relx=0.5, rely=0.09, anchor=CENTER)

    backbtn = Button(root, text="Back", width=6, font=("Times New Roman", 15), activebackground="#228B22", bg="#32CD32",fg="dark blue", activeforeground="dark blue", command=back)
    backbtn.place(relx=0.74,rely=0.75,anchor=CENTER)





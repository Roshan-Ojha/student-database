from tkinter import *
import sqlite3
import tkinter.messagebox
def gradesheet():
    global root
    root=Tk()
    root.geometry("800x600")
    root.geometry("+275+70")
    root.configure(bg="#7CFC00")
    root.title("Grade-Sheet")
    main()
    root.resizable(False, False)
    root.mainloop()


def back_entry():
    canvas.destroy()
    back_button.destroy()
    name.destroy()
    clas.destroy()
    section.destroy()
    roll.destroy()
    getname.destroy()
    getclas.destroy()
    getsection.destroy()
    getroll.destroy()
    enter()



def grade():
    global canvas,back_button,name,clas,section,roll,getname,getclas,getsection,getroll
    try:

        name=Label(root, text="Name :", font=("Calibri (Body)", 15), bg="#7CFC00")
        clas = Label(root, text="Class :", font=("Calibri (Body)", 15), bg="#7CFC00")
        section = Label(root, text="Section :", font=("Calibri (Body)", 15), bg="#7CFC00")
        roll = Label(root, text="Roll No :", font=("Calibri (Body)", 15), bg="#7CFC00")
        getname=Label(root, text=data[0][0], font=("Calibri (Body)", 15), bg="#7CFC00")
        getclas=Label(root, text=data[0][1], font=("Calibri (Body)", 15), bg="#7CFC00")
        getsection = Label(root, text=data[0][2], font=("Calibri (Body)", 15), bg="#7CFC00")
        getroll = Label(root, text=data[0][3], font=("Calibri (Body)", 15), bg="#7CFC00")

        name.place(relx=0.05,rely=0.18,anchor=W)
        section.place(relx=0.05, rely=0.25, anchor=W)
        clas.place(relx=0.6,rely=0.18,anchor=W)
        roll.place(relx=0.6, rely=0.25, anchor=W)

        getname.place(relx=0.15,rely=0.18,anchor=W)
        getclas.place(relx=0.7,rely=0.18,anchor=W)
        getsection.place(relx=0.15, rely=0.25, anchor=W)
        getroll.place(relx=0.7, rely=0.25, anchor=W)


        back_button=Button(root, text="Back", width=6, font=("Times New Roman", 10), activebackground="#228B22", bg="#32CD32",
                fg="dark blue", activeforeground="dark blue", command=back_entry)
        back_button.place(relx=0.5,rely=0.955)

        canvas=Canvas(width=775,height=400,bg="#7CFC00")
        canvas.place(relx=0.5,rely=0.62,anchor=CENTER)
        canvas.create_rectangle(2,2,775,75,fill="#87CEEB",outline="#120A8F")
        canvas.create_rectangle(2, 75, 775, 340,fill="#BFEFFF",outline="#120A8F")
        canvas.create_rectangle(2, 340, 775, 401, fill="#87CEEB",outline="#120A8F")

        canvas.create_line(50,2,50,340,fill="#120A8F")
        canvas.create_line(379, 2, 379, 340, fill="#120A8F")
        canvas.create_line(445, 2, 445, 340, fill="#120A8F")
        canvas.create_line(577, 2, 577, 340, fill="#120A8F")
        canvas.create_line(445, 42, 577, 42, fill="#120A8F")
        canvas.create_line(511, 42, 511, 340, fill="#120A8F")
        canvas.create_line(643, 2, 643, 340, fill="#120A8F")
        canvas.create_line(709, 2, 709, 340, fill="#120A8F")

        canvas.create_text(25,40,text="S.N",anchor=CENTER,font=("Calibri (Body)", 13),fill="#120A8F")
        canvas.create_text(215, 40, text="SUBJECTS", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(395, 70, text="CREDIT", anchor=NW, font=("Calibri (Body)", 13), fill="#120A8F",angle=90)
        canvas.create_text(414, 70, text="HOUR", anchor=NW, font=("Calibri (Body)", 13), fill="#120A8F", angle=90)
        canvas.create_text(510, 12, text="OBTAINED", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(510, 32, text="GRADE", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(480, 60, text="TH", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(545, 60, text="PR", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(591, 65, text="FINAL", anchor=NW, font=("Calibri (Body)", 13), fill="#120A8F", angle=90)
        canvas.create_text(610, 70, text="GRADE", anchor=NW, font=("Calibri (Body)", 13), fill="#120A8F", angle=90)
        canvas.create_text(655, 70, text="GRADE", anchor=NW, font=("Calibri (Body)", 13), fill="#120A8F", angle=90)
        canvas.create_text(674, 65, text="POINT", anchor=NW, font=("Calibri (Body)", 13), fill="#120A8F", angle=90)
        canvas.create_text(735, 72, text="REMARKS", anchor=NW, font=("Calibri (Body)", 10), fill="#120A8F", angle=90)

        canvas.create_text(40, 120, text="01", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(100, 120, text="COMP.    ENGLISH", anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(430, 120, text="4", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(480, 120, text=theory[0], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(545, 120, text=practical[0], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(610, 120, text=final_grade[0], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(674, 120, text=grade_point[0], anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")

        canvas.create_text(40, 140, text="02", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(100, 140, text="COMP.    NEPALI", anchor=W, font=("Calibri (Body)", 13),fill="#120A8F")
        canvas.create_text(430, 140, text="4", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(480, 140, text=theory[1], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(545, 140, text=practical[1], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(610, 140, text=final_grade[1], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(674, 140, text=grade_point[1], anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")

        canvas.create_text(40, 160, text="03", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(100, 160, text="COMP.    MATHEMATICS", anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(430, 160, text="4", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(480, 160, text=theory[2], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(610, 160, text=final_grade[2], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(674, 160, text=grade_point[2], anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")

        canvas.create_text(40, 180, text="04", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(100, 180, text="COMP.    SCIENCE", anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(430, 180, text="4", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(480, 180, text=theory[3], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(545, 180, text=practical[2], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(610, 180, text=final_grade[3], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(674, 180, text=grade_point[3], anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")

        canvas.create_text(40, 200, text="05", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(100, 200, text="COMP.    SOCIAL STUDIES", anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(430, 200, text="4", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(480, 200, text=theory[4], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(545, 200, text=practical[3], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(610, 200, text=final_grade[4], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(674, 200, text=grade_point[4], anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")

        canvas.create_text(40, 220, text="06", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(100, 220, text="COMP.    HEALTH, POP & ENV EDU", anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(430, 220, text="4", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(480, 220, text=theory[5], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(545, 220, text=practical[4], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(610, 220, text=final_grade[5], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(674, 220, text=grade_point[5], anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")

        canvas.create_text(40, 240, text="07", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(100, 240, text="OPT.I", anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(430, 240, text="4", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(480, 240, text=theory[6], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(610, 240, text=final_grade[6], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(674, 240, text=grade_point[6], anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")

        canvas.create_text(40, 260, text="08", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(100, 260, text="OPT.II", anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(430, 260, text="4", anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(480, 260, text=theory[7], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(545, 260, text=practical[5], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(610, 260, text=final_grade[7], anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")
        canvas.create_text(674, 260, text=grade_point[7], anchor=CENTER, font=("Calibri (Body)", 13), fill="#120A8F")

        txt1="GRADE POINT AVERAGE (GPA):   {}".format(gpa)

        canvas.create_text(360, 370, text=txt1, anchor=W, font=("Calibri (Body)", 13), fill="#120A8F")


        l111.destroy()
        l222.destroy()
        e11.destroy()
        e22.destroy()
        b1.destroy()
        b2.destroy()

    except:

        tkinter.messagebox.showerror("Error","Sorry an error occured.")



def add():

    global theory,practical,grade_point,gpa,final_grade,data

    conn=sqlite3.connect('Marks.db')
    c=conn.cursor()
    c.execute("SELECT * FROM mark WHERE class=:a AND roll=:b",
              {
                  'a':e11.get(),
                  'b':e22.get()
              })
    data=c.fetchall()
    #check=data[0]
    conn.commit()
    conn.close()
    i=0
    if data==[]:
        tkinter.messagebox.showerror("Data Not Found","Sorry No such record in the database")
    else:
        theory=[]
        practical=[]
        grade_point=[]
        final_grade=[]
        tm=[]
        pm=[]
        for m in data[0]:
            i += 1
            da=data[0][4:]
            if i == 5 or i == 12:
                if da[i-1]>=90:
                    t='A+'
                elif da[i-1]>=80:
                    t='A'
                elif da[i-1]>=70:
                    t='B+'
                elif da[i-1]>=60:
                    t='B'
                elif da[i-1]>=50:
                    t='C+'
                elif da[i-1]>=40:
                    t='C'
                elif da[i-1]>=30:
                    t='D+'
                elif da[i-1]>=20:
                    t='D'
                else:
                    t='E'
                theory.append(t)
                tm.append(da[i-1])
                pm.append(0)
                continue
            elif not (i==2 or i==4 or i==7 or i==9 or i==11 or i==14):
                if da[i-1]>=67.5:
                    th='A+'
                elif da[i-1]>=60:
                    th='A'
                elif da[i-1]>=52.5:
                    th='B+'
                elif da[i-1]>=45:
                    th='B'
                elif da[i-1]>=37.5:
                    th='C+'
                elif da[i-1]>=30:
                    th='C'
                elif da[i-1]>=22.5:
                    th='D+'
                elif da[i-1]>=15:
                    th='D'
                else:
                    th='E'
                theory.append(th)
                tm.append(da[i-1])
            else:
                if da[i-1]>=22.5:
                    pr='A+'
                elif da[i-1]>=20:
                    pr='A'
                elif da[i-1]>=17.5:
                    pr='B+'
                elif da[i-1]>=15:
                    pr='B'
                elif da[i-1]>=12.5:
                    pr='C+'
                elif da[i-1]>=10:
                    pr='C'
                elif da[i-1]>=7.5:
                    pr='D+'
                elif da[i-1]>=5:
                    pr='D'
                else:
                    pr='E'
                practical.append(pr)
                pm.append(da[i-1])


            if i == len(da):
                break
        j=0
        for a in tm:
            j=j+1
            if (tm[j-1]+pm[j-1])>=90:
                tot=4.0
                final='A+'
            elif (tm[j-1]+pm[j-1])>=80:
                tot=3.6
                final='A'
            elif (tm[j-1]+pm[j-1])>=70:
                tot=3.2
                final='B+'
            elif (tm[j-1]+pm[j-1])>=60:
                tot=2.8
                final='B'
            elif (tm[j-1]+pm[j-1])>=50:
                tot=2.4
                final='C+'
            elif (tm[j-1]+pm[j-1])>=40:
                tot=2.0
                final='C'
            elif (tm[j-1]+pm[j-1])>=30:
                tot=1.6
                final='D+'
            elif (tm[j-1]+pm[j-1])>=20:
                tot=1.2
                final='D'
            else:
                tot=0.8
                final='E'
            grade_point.append(tot)
            final_grade.append(final)


            if len(tm)==j:
                break
        gpa=sum(grade_point)/8
        gpa=round(gpa,2)

        grade()




def back():
    root.destroy()
    import Login_page
    Login_page.Login_page()

def enter():
    global e11,e22,l111,l222,b1,b2

    l111 = Label(root, text="Enter Class :", font=("Calibri (Body)", 15), bg="#7CFC00")
    l222 = Label(root, text="Enter Roll No :", font=("Calibri (Body)", 15), bg="#7CFC00")

    e11 = Entry(root, width=30, font=("Calibri (Body)", 15))
    e22 = Entry(root, width=30, font=("Calibri (Body)", 15))

    l111.place(relx=0.20, rely=0.24, anchor=W)
    e11.place(relx=0.59, rely=0.24, anchor=CENTER)

    l222.place(relx=0.20, rely=0.34, anchor=W)
    e22.place(relx=0.59, rely=0.34, anchor=CENTER)

    b1 = Button(root, text="View Grade-sheet", width=15, font=("Times New Roman", 15), activebackground="#228B22",
                bg="#32CD32", fg="dark blue", activeforeground="dark blue", command=add)
    b2 = Button(root, text="Back", width=6, font=("Times New Roman", 15), activebackground="#228B22", bg="#32CD32",
                fg="dark blue", activeforeground="dark blue", command=back)

    b1.place(relx=0.22, rely=0.45, anchor=W)
    b2.place(relx=0.71, rely=0.45, anchor=W)



def main():
    global l
    l = Label(root, text="Student Database Software",font=("Times New Roman",40),bg="#7CFC00",fg="#008000")
    l.place(relx=0.5,rely=0.09,anchor=CENTER)
    enter()




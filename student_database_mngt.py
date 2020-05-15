from tkinter import *
from tkinter import messagebox


def add_student() :
    return
def view_student() :
    return
def delete_student() :
    return
def update_student() :
    return
def clse() :
    return


root=Tk()
root.title("Student Management System")
     
student_name=StringVar()
roll_no=StringVar()
branch=StringVar()
phone=StringVar()
father=StringVar()
address=StringVar()
    
label1=Label(root,text="Student name:")
label1.place(x=0,y=0)

label2=Label(root,text="Roll no:")
label2.place(x=0,y=30)

label3=Label(root,text="Branch:")
label3.place(x=0,y=60)

label4=Label(root,text="Phone Number:")
label4.place(x=0,y=90)

label5=Label(root,text="Father Name:")
label5.place(x=0,y=120)

label6=Label(root,text="Address:")
label6.place(x=0,y=150)

e1=Entry(root,textvariable=student_name)
e1.place(x=100,y=0)

e2=Entry(root,textvariable=roll_no)
e2.place(x=100,y=30)

e3=Entry(root,textvariable=branch)
e3.place(x=100,y=60)

e4=Entry(root,textvariable=phone)
e4.place(x=100,y=90)
    
e5=Entry(root,textvariable=father)
e5.place(x=100,y=120)

e6=Entry(root,textvariable=address)
e6.place(x=100,y=150)
    
t1=Text(root,width=80,height=20)
t1.grid(row=10,column=1)
   


b1=Button(root,text="ADD STUDENT",command=add_student,width=40)
b1.grid(row=11,column=0)

b1=Button(root,text="SEARCH",command=add_student,width=40)
b1.grid(row=12,column=0)

b2=Button(root,text="VIEW ALL STUDENTS",command=view_student,width=40)
b2.grid(row=13,column=0)

b3=Button(root,text="DELETE STUDENT",command=delete_student,width=40)
b3.grid(row=14,column=0)

b4=Button(root,text="UPDATE INFO",command=update_student,width=40)
b4.grid(row=15,column=0)

b5=Button(root,text="CLOSE",command=clse,width=40)
b5.grid(row=16,column=0)


root.mainloop()



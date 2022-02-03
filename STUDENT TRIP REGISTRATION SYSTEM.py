from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter.ttk import Combobox
import mysql.connector

# creating main application window........
root=Tk()
root.title("Registration Form")
root.geometry('1350x700+0+0')
root.config(bg='brown')

frame=Frame(root, bg='white')
frame.config(width=800, height=600)
frame.place(x=300, y=100)
font1=Font(family="Arial", size=18, weight='bold')
font2=Font(family="Arial", size=18)
title=Label(frame,text="STUDENT TRIP REGISTRATION SYSTEM", font=("times new roman",20,"bold"),bg="white",fg="green").place(x=100,y=20)

firstname=Label(root, text="First Name: ", font=font1, bg='white')
firstname.place(x=350, y=180)
entr1=Entry(root, font=font2, bg='white')
entr1.place(x=350,y=220)

lastname=Label(root, text="Last Name: ", font=font1, bg='white')
lastname.place(x=700, y=180)
entr2=Entry(root, font=font2, bg='white')
entr2.place(x=700,y=220)

contact=Label(root, text="Contact No.", font=font1, bg='white')
contact.place(x=350, y=260)
entr3=Entry(root, font=font2, bg='white')
entr3.place(x=350,y=300)

emails=Label(root, text="Email: ", font=font1, bg='white')
emails.place(x=700, y=260)
entr4=Entry(root, font=font2, bg='white')
entr4.place(x=700,y=300)

semester=Label(root, text="Select Semester:",font=font1, bg='white')
semester.place(x=350, y=340)
v=["1st semster", "2nd semester", "3rd semester", "4th semester" , "5th semester", "6th semester"]
combobox=Combobox(root, values=v, font=font1)
combobox.set("Select")
combobox.place(x=350, y=380)

std_id=Label(root, text="student_ID:", font=font1, bg='white')
std_id.place(x=700, y=340)
entr6=Entry(root, font=font2, bg='white')
entr6.place(x=700,y=380)

gender=Label(root, text="Select_Gender:", font=font1, bg='white')
gender.place(x=350, y=420)
g=["Male", "Female"]
combobox=Combobox(root, values=g, font=font2)
combobox.set("Select")
combobox.place(x=350, y=460)

remarks=Label(root, text="Why did you want to join trip?", font=font1, bg='white')
remarks.place(x=700, y=420)
entr8=Entry(root, font=font2, bg='white')
entr8.place(x=700,y=460)

def reset():
    entr1.delete(0, END)
    entr2.delete(0, END)
    entr3.delete(0, END)
    entr4.delete(0, END)
    entr6.delete(0, END)
    entr8.delete(0, END)

def submit():
    if(entr1.get()=="" or entr2.get()=="" or entr3.get()=="" or entr4.get()=="" or entr6.get()==""  or entr8.get()==""):
        messagebox.showerror("Error", "All Fields are requied to fill.")
    else:
        a=entr1.get()
        b=entr2.get()
        c=entr3.get()
        d=entr4.get()
        h=combobox.get()
        e=entr6.get()
        f=combobox.get()
        g=entr8.get()
        
        #Creating the connection of db..........
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="register"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO trip (Name, Last_Name, contact, email, semester, std_id, gender, remarks) VALUES (%s, %s,%s,%s, %s,%s,%s, %s)"
        val = (a,b,c,d,h,e,f,g)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Success.", " Thanks for submitting your form. We are happy to see you joining us for the trip.")
        reset()
        print(mycursor.rowcount, "Record inserted Successfully.")
button=Button(root, bg='green', fg='white', text='Submit', bd=0, cursor="hand2",font=font1, command=submit)
button.place(x=623, y=540)

# Call the main event loop
root.mainloop()
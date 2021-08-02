#imports
from tkinter import *
import os
from PIL import ImageTk, Image

#Main Screen
master = Tk()
master.title('Banking App')

#Functions
def Finish_register():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()

    all_accounts = os.listdir()
    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red",text="All Fields Requierd *")
        return
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red",text="Account Alredy exits")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(password+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="Account Created Succesfully")
    
def register():
    
    #Variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()


    #Register screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Labels
    Label(register_screen,text="Please enetr your details below to register",font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen,text="Name",font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen,text="Age",font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen,text="Gender",font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen,text="Password",font=('Calibri',12)).grid(row=4,sticky=W)
    notif = Label(register_screen,font=('Calibri',12))
    notif.grid(row=6,sticky=N,pady=10)

    #Entris
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=0)

    #Buttons
    Button(register_screen, text="Register",command=Finish_register,font=('Calibri',12)).grid(row=5,sticky=N,pady=10)

def Login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[3]

            #Account Dashbord
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')

                #Labels
                Label(account_dashboard,text = "Account Dashboard",font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard,text = "Welcome  "+name,font=("Calibri",12)).grid(row=1,sticky=N,pady=5)
                
                #Buttons
                Button(account_dashboard,text="Personal Details",font=("Calibri",12),width=30,command=Personal_details).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard,text="Deposit",font=("Calibri",12),width=30,command = Deposit).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard,text="Withdraw",font=("Calibri",12),width=30,command = Withdraw).grid(row=4,sticky=N,padx=10)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="red",text="Password Incorrect!!")
            return
    login_notif.config(fg="red",text="No Account Found !!")

def Deposit():
    print("Deposit")

def Withdraw():
    print("Withdraw")

def Personal_details():
    #Variables

    file = open(login_name,'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[1]
    details_gender = user_details[2]
    details_balance = user_details[4]

    #Personal Details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')

    #Label

    Label(personal_details_screen,text="Personal Details",font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen,text="Name : "+details_name,font=('Calibri',12)).grid(row=1,sticky=W)
    Label(personal_details_screen,text="Age : "+details_age,font=('Calibri',12)).grid(row=2,sticky=W)
    Label(personal_details_screen,text="Gender : "+details_gender,font=('Calibri',12)).grid(row=3,sticky=W)
    Label(personal_details_screen,text="Balance :$"+details_balance,font=('Calibri',12)).grid(row=4,sticky=W)

def login():
    #Variable
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen

    temp_login_name = StringVar()
    temp_login_password = StringVar()
    
    
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title("Login")

    #Labels
    Label(login_screen,text="Login To Your Account",font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen,text="Enter User Name",font=('Calibri',12)).grid(row=1,stick=W)
    Label(login_screen,text="Enter Password",font=("Calibri",12)).grid(row=2,sticky=W)
    login_notif = Label(login_screen,font=('Calibri',12))
    login_notif.grid(row=4,sticky=N,pady=10)
    #Entry
    Entry(login_screen,textvariable = temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen,textvariable = temp_login_password,show="*").grid(row=2,column=1,padx=5)

    #Button
    Button(login_screen,text="Login",command = Login_session,width=20,font=('Calibri',12)).grid(row=3,sticky=N,pady=5,padx=5)

    
#image import
img = Image.open('banking_logo.jpg')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(master,text = "Custome Banking Beta",font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master,text = "The Most Secure Bank ",font=('Calibri',12)).grid(row=1,sticky=N)
Label(master,image = img).grid(row=2,sticky=N,pady=15)

#Button
Button(master, text ='Register',font=('Calibri',12),width=20,command=register).grid(row=3,sticky=N)
Button(master,text ='Login',font=('Calibri',12),width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()

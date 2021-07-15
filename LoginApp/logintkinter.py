from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import pymongo


def loginpage():
    loginwindow = Tk()
    loginwindow.geometry('500x500')
    loginwindow.resizable(0, 0)
    loginwindow.title("SIGN UP")

    loginusertxt = StringVar()
    loginpwdtxt = StringVar()

    def loginvalidation():
        if loginusertxt.get() == '' or loginpwdtxt.get() == '':
            messagebox.showerror("Error", "All Fields Are Required", parent=loginwindow)
        else:
            try:
                cloudclient = pymongo.MongoClient(
                    r"mongodb+srv://ishwarya:ishusonu@cluster0.riei5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                myclouddb = cloudclient.MyDB
                userdetailscollection = myclouddb.userdetails
                if userdetailscollection.count_documents(
                        {'UserName': loginusertxt.get(), 'Password': loginpwdtxt.get()}):
                    loginwindow.destroy()
                    portalpage(loginusertxt.get())
                elif userdetailscollection.count_documents({'UserName': loginusertxt.get()}):
                    messagebox.showerror("Error", "Incorrect password. Please try again!!", parent=loginwindow)
                else:
                    messagebox.showerror("Error", "Account not created. Please Signup", parent=loginwindow)

            except Exception as e:
                messagebox.showerror("Error", f"Error Due to : {str(e)}", parent=loginwindow)

    def clearlogindetails():
        loginusertxt.set('')
        loginpwdtxt.set('')

    def opensignup():
        loginwindow.destroy()
        createsignup()

    wellbl = Label(loginwindow, text="Welcome back!!", font='Verdana 19 bold', bg="#339966", fg="white")
    wellbl.pack(side=TOP, fill=BOTH)

    lbl1 = Label(loginwindow, text="Don't miss to keep track of your work", font='Verdana 10 bold')
    lbl1.place(x=100, y=50)

    usernamelbl = Label(loginwindow, text="UserName :", font='Verdana 10 bold')
    usernamelbl.place(x=60, y=130)
    user = Entry(loginwindow, width=40, textvariable=loginusertxt)
    user.place(x=200, y=133)

    createlbl = Label(loginwindow, text="Password: ", font='Verdana 10 bold')
    createlbl.place(x=60, y=180)
    password = Entry(loginwindow, width=40, textvariable=loginpwdtxt,show="*")
    password.place(x=200, y=183)

    btn_login = Button(loginwindow, text="Login", font='Verdana 10 bold', command=loginvalidation, bg="#339966",
                       fg="white")
    btn_login.place(x=150, y=240)

    btn_clear = Button(loginwindow, text="Clear", font='Verdana 10 bold', command=clearlogindetails, bg="#339966",
                       fg="white")
    btn_clear.place(x=230, y=240)

    btn_signup = Button(loginwindow, text="Signup", font='Verdana 10 bold', command=opensignup, bg="#339966",
                        fg="white")
    btn_signup.place(x=300, y=240)

    loginwindow.mainloop()


def createsignup():
    signupwindow = Tk()
    signupwindow.geometry('500x500')
    signupwindow.resizable(0, 0)
    signupwindow.title("SIGN UP")

    nametext = StringVar()
    createpwdtxt = StringVar()
    confirmpwdtxt = StringVar()
    phnotxt = StringVar()
    emailtxt = StringVar()
    ds = StringVar()

    def openlogin():
        signupwindow.destroy()
        loginpage()

    def cleardetails():
        nametext.set('')
        createpwdtxt.set('')
        confirmpwdtxt.set('')
        phnotxt.set('')
        emailtxt.set('')
        ds.set('Yes')

    def signupvalidation():
        emailre = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if nametext.get() == "" or createpwdtxt.get() == "" or confirmpwdtxt.get() == "" or phnotxt.get() == "" or emailtxt.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=signupwindow)
        elif createpwdtxt.get() != confirmpwdtxt.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=signupwindow)
        elif emailre.match(emailtxt.get()) == None:
            messagebox.showerror("Error", "Mailid is not valid", parent=signupwindow)
        else:
            try:
                cloudclient = pymongo.MongoClient(
                    r"mongodb+srv://ishwarya:ishusonu@cluster0.riei5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                myclouddb = cloudclient.MyDB
                userdetailscollection = myclouddb.userdetails
                user = {
                    'UserName': nametext.get(),
                    'Password': createpwdtxt.get(),
                    'PhoneNumber': phnotxt.get(),
                    'EmailId': emailtxt.get(),
                    'InterestedDS': ds.get(),
                    'Preferredlanguage': lng.get()
                }
                print(nametext.get())
                print(createpwdtxt.get())
                print(phnotxt.get())
                print(emailtxt.get())
                print(ds.get())
                print(lng.get())

                try:
                    if userdetailscollection.count_documents({'UserName': nametext.get()}):
                        messagebox.showerror("Info", "Account already created. Try to login", parent=signupwindow)
                        openlogin()
                    else:
                        userdetailscollection.insert_one(user)
                        messagebox.showinfo("Success", "Registration Successful. Login to proceed", parent=signupwindow)
                except Exception as e:
                    messagebox.showerror("Error", f"DatabaseError Due to : {str(e)}", parent=signupwindow)
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=signupwindow)

    def isvalidnumber(signupwindow):
        phonere = re.compile(r'^[0-9]{0,10}$')
        return phonere.match(signupwindow) != None

    createaccountlbl = Label(signupwindow, text="Create Account", font='Verdana 19 bold', bg="#339966", fg="white")
    createaccountlbl.pack(side=TOP, fill=BOTH)

    lbl1 = Label(signupwindow, text="Please enter details below", font='Verdana 10 bold')
    lbl1.place(x=130, y=50)

    namelbl = Label(signupwindow, text="UserName :", font='Verdana 10 bold')
    namelbl.place(x=60, y=130)
    username = Entry(signupwindow, width=40, textvariable=nametext)
    username.place(x=220, y=133)

    createlbl = Label(signupwindow, text="Create password: ", font='Verdana 10 bold')
    createlbl.place(x=60, y=160)
    password = Entry(signupwindow, width=40, textvariable=createpwdtxt)
    password.place(x=220, y=163)

    confirmlbl = Label(signupwindow, text="Confirm password: ", font='Verdana 10 bold')
    confirmlbl.place(x=60, y=190)
    confirmpassword = Entry(signupwindow, width=40, textvariable=confirmpwdtxt)
    confirmpassword.place(x=220, y=193)

    phoneNumberlbl = Label(signupwindow, text="PhoneNumber :", font='Verdana 10 bold')
    phoneNumberlbl.place(x=60, y=220)
    phoneno = Entry(signupwindow, width=40, textvariable=phnotxt)
    valresult = signupwindow.register(isvalidnumber)
    phoneno['validate'] = 'key'
    phoneno['validatecommand'] = (valresult, '%P')
    phoneno.place(x=220, y=223)

    emailidlbl = Label(signupwindow, text="EmailID :", font='Verdana 10 bold')
    emailidlbl.place(x=60, y=250)
    email = Entry(signupwindow, width=40, textvariable=emailtxt)
    email.place(x=220, y=253)

    interestdslbl = Label(signupwindow, text="Interested in DS :", font='Verdana 10 bold')
    interestdslbl.place(x=60, y=280)
    yesradio = Radiobutton(signupwindow, value="Yes", text="YES", variable=ds, cursor="hand2")
    yesradio.place(x=220, y=283)
    noradio = Radiobutton(signupwindow, value="No", text="NO", variable=ds, cursor="hand2")
    noradio.place(x=300, y=283)
    ds.set('Yes')

    proglangdslbl = Label(signupwindow, text="Preferred languages :", font='Verdana 10 bold')
    proglangdslbl.place(x=60, y=310)
    lng = ttk.Combobox(signupwindow)
    lng['values'] = ('Python', 'Java', 'C', 'C++', 'R')
    lng.current(0)
    lng.place(x=250, y=310)

    btn_signup = Button(signupwindow, text="Signup", font='Verdana 10 bold', bg="#339966", fg="white",
                        command=signupvalidation)
    btn_signup.place(x=120, y=380)

    btn_clear = Button(signupwindow, text="Clear", font='Verdana 10 bold', bg="#339966", fg="white",
                       command=cleardetails)
    btn_clear.place(x=200, y=380)

    btn_login = Button(signupwindow, text="Switch to Login", font='Verdana 10 bold', bg="#339966", fg="white",
                       command=openlogin)
    btn_login.place(x=260, y=380)

    signupwindow.mainloop()


def addprojectwork(username):
    addprojectwindow = Tk()
    addprojectwindow.geometry('500x500')
    addprojectwindow.resizable(0, 0)
    addprojectwindow.title("ADD WORK")

    projnamevar = StringVar()
    projdescriptionvar = StringVar()
    languageusedvar = StringVar()
    toolsusedvar = StringVar()
    gitlinkvar = StringVar()
    usernamevar = "Hi " + username + "!!"

    def addprojecttodb():
        if projnamevar.get() == "" or projdescriptionvar.get() == "" or languageusedvar.get() == "" or toolsusedvar.get() == "" or gitlinkvar.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=addprojectwindow)
        else:
            try:
                print (usernamevar)
                print (projnamevar.get())
                print(projdescriptionvar.get())
                print(languageusedvar.get())
                print(toolsusedvar.get())
                print(gitlinkvar.get())
                cloudclient = pymongo.MongoClient(
                    r"mongodb+srv://ishwarya:ishusonu@cluster0.riei5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
                myclouddb = cloudclient.MyDB
                UserProjectcollection = myclouddb.UserProjectDetails

                project = {
                    'UserName' :usernamevar,
                    'ProjectName' :projnamevar.get(),
                    'ProjectDescription' : projdescriptionvar.get(),
                    'LanguageUsed' : languageusedvar.get(),
                    'Toolsused' : toolsusedvar.get(),
                    'GitPath' : gitlinkvar.get()
                }

                UserProjectcollection.insert_one(project)
                messagebox.showinfo("Success","Project addition successful",parent = addprojectwindow)
            except Exception as e:
                messagebox.showerror("Error",f"Error Due to : {str(e)}", parent=addprojectwindow)

    lbl1 = Label(addprojectwindow, text=f"{usernamevar}", font='Verdana 10 bold')
    lbl1.place(x=380, y=25)

    projnamelbl = Label(addprojectwindow, text="Project Name :", font='Verdana 10 bold')
    projnamelbl.place(x=60, y=130)
    projname = Entry(addprojectwindow, width=40, textvariable=projnamevar)
    projname.place(x=220, y=133)

    projdeslbl = Label(addprojectwindow, text="Project Description: ", font='Verdana 10 bold')
    projdeslbl.place(x=60, y=160)
    projdes = Entry(addprojectwindow, width=40, textvariable=projdescriptionvar)
    projdes.place(x=220, y=163)

    langusedlbl = Label(addprojectwindow, text="Language used: ", font='Verdana 10 bold')
    langusedlbl.place(x=60, y=190)
    langused = Entry(addprojectwindow, width=40, textvariable=languageusedvar)
    langused.place(x=220, y=193)

    toolusedlbl = Label(addprojectwindow, text="Tools used: ", font='Verdana 10 bold')
    toolusedlbl.place(x=60, y=223)
    toolused = Entry(addprojectwindow, width=40, textvariable=toolsusedvar)
    toolused.place(x=220, y=223)

    gitlbl = Label(addprojectwindow, text="Git path: ", font='Verdana 10 bold')
    gitlbl.place(x=60, y=253)
    git = Entry(addprojectwindow, width=40, textvariable=gitlinkvar)
    git.place(x=220, y=253)

    btn_signup = Button(addprojectwindow, text="Add project", font='Verdana 10 bold', bg="#339966", fg="white",
                        command=addprojecttodb)
    btn_signup.place(x=200, y=300)

    addprojectwindow.mainloop()


def portalpage(username):
    portalwindow = Tk()
    portalwindow.geometry('500x500')
    portalwindow.resizable(0, 0)
    portalwindow.title("USER PORTAL")
    usernamevar = "Hi " + username + "!!"

    def openaddproject():
        portalwindow.destroy()
        addprojectwork(username)

    lbl1 = Label(portalwindow, text=f"{usernamevar}", font='Verdana 10 bold')
    lbl1.place(x=380, y=25)

    caption = Label(portalwindow, text="Make it simple, but significant", font='Verdana 10 bold')
    caption.place(x=130, y=80)

    btn_addwork = Button(portalwindow, text="Add project", font='Verdana 10 bold', bg="#339966", fg="white",command=openaddproject)
    btn_addwork.place(x=180, y=130)

    btn_displaywork = Button(portalwindow, text="Projects in track", font='Verdana 10 bold', bg="#339966", fg="white")
    btn_displaywork.place(x=180, y=180)

    portalwindow.mainloop()


if __name__ == '__main__':
    loginpage()

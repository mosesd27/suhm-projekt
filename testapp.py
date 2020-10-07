from tkinter import*
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import time
import random
tk = Tk()
tk.resizable(0,0)
tk.title("Totally Iluminate")
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = 800, height = 500,background = "white", highlightthickness = 5, highlightbackground = "black")
canvas.pack()
def enteraccount():
    global activeaccount
    #canvas.bind_all("<Button-1>",detectmouse)
    canvas.delete("all")
    removeallbuttons()
    profilepicture.place(x = 130,y = 370)
    entercode.place(x = 180,y = 340)
    confirmcode.place(x = 220,y = 340)
    Logout.place(x = 700, y = 450)
    #if self.teacher == True:
    #   MakeTestButton.place(x = 550,y = 300)
    y = 200
    for count in range(0,len(activeaccount.test)):
        canvas.create_text(500,y,text = "%s" % activeaccount.test[count].name, font = ("Courier", 12))
        canvas.create_text(600,y,text = "%s" % activeaccount.test[count].grade, font = ("Courier", 12))
        y = y +20
    canvas.create_text(200,100,text = "Welcome %s" % activeaccount.id, font = ("Courier", 20))
    canvas.create_text(435,380,text = "Enter A Code", font = ("Courier", 20))
    canvas.create_text(580,100, text = "Your Recent Tests",font = ("Courier", 20))
    canvas.create_rectangle(100,150,300,350, fill = "grey")

def receiveresponse(answer):
    global results 
    name = answer["text"]
    position = answer.pos
    print(name)
    print(position)
    results.remove(results[position])
    results.insert(position,name)
    print(results)
    
def grade_test(self):
    pass
            

def openimage():
    path=askopenfilename(filetypes=[("Image File",'.png')])
    tkimage = ImageTk.PhotoImage(Image.open(path))
    label = Label(canvas, image=tkimage)
    label.image = tkimage # keep a reference!
    label.place(x = 100, y = 150)


def choose_students(self):
    global accounrecord
    global Done
    canvas.bind_all("<Button-1>",detectmouse)
    QuestionMaker.place_forget()
    AnswerMaker.place_forget()
    Confirm2.place_forget()
    cd.place_forget()
    possiblestudents = []
    y = 200
    for blah in range(0,len(accountrecord)):
        newaccountpossibilities = ["account", str(blah)]
        the_text = "".join(newaccountpossibilities)
        current = accountrecord[the_text]
        if current.student == True:
            possiblestudents.append(current)
            canvas.create_text(500,y,text = "%s" % current.name, font = ("Courier", 20), tags = the_text)
            y = y +40
    Done = False
    cd.place(x = 200, y = 100)
    while 1:
        tk.update()
        tk.update_idletasks()
        if Done == True:
            hi = canvas.find_withtag("selected")
            for blah in range (0,len(hi)):
                current = hi[blah]
                tags = canvas.gettags(current)
                current = accountrecord[tags[0]]
                current.tests.append(EnterTestName.get())
            break
    canvas.delete("all")
    canvas.unbind_all("<Button-1>")
    setup()             
    
#Classes
class Account():
    def __init__(self,accounttype):
        global accountid
        accountid = accountid + 1
        self.id = accountid
        self.type = accounttype
        self.active = True  #Set to false when fully functional
        self.test = []
        self.username = username.get()
        self.password = password.get()
        accounts.append(self)

    def __str__(self):
        return self.id
        
class Student(Account):
    pass
class Teacher(Account):
    pass
class Admin(Account):
    pass
#Variables
accountid = 0
accounts = []
tests = []
activeaccount = None
activetest = None
#Basic Functions
scroll = Scrollbar(canvas, orient=VERTICAL)
scroll.config(command=canvas.yview)
canvas.config(yscrollcommand=scroll.set)
scroll.place(x = 795, y = 5)
def createaccount():
    canvas.delete("all")
    removeallbuttons()
    username.place(x = 570, y = 350)
    password.place(x = 570, y = 400)
    Confirmaccount.place(x = 570, y = 440)
    teacher.place(x = 450,y = 350)
    student.place(x = 450,y = 400)

def confirmaccount():
    if (len(username.get()) > 0) and (len(password.get()) > 0):
        newaccount = Account(selection.get())
        setup()
        
def logout():
    global activeaccount
    activeaccount = None
    canvas.delete("all")
    setup()
    
def checklogin():
    global activeaccount
    ReceiveUsername = username.get()
    ReceivePassword = password.get()
    for count in range(0,len(accounts)):
        currentaccount = accounts[count]
        if (currentaccount.username == ReceiveUsername) and (currentaccount.password == ReceivePassword):
            activeaccount = currentaccount
            enteraccount()
            return True
    canvas.create_text(640,450,text = "Login Invalid", font = ("Courier", 12), fill = "red")

def checkcode():    
    ReceiveCode = entercode.get()
    for count in range(0,len(tests)):
        currenttest = tests[count]
        if (currenttest.code == ReceiveCode):
            activetest = tests[count]
            entertest(tests[count])
            return True
    canvas.create_text(640,450,text = "Invalid Code", font = ("Courier", 12), fill = "red")
    
def removeallbuttons():
    username.place_forget()
    password.place_forget()
    entercode.place_forget()
    confirmlogin.place_forget()
    confirmcode.place_forget()
    Createaccount.place_forget()
    Confirmaccount.place_forget()
    teacher.place_forget()
    student.place_forget()
    profilepicture.place_forget()
    Logout.place_forget()
    
def setup():
    canvas.create_text(400,150,text = "Welcome To Under\nConstruction Online Testing", font = ("Courier", 30))
    canvas.create_text(350,320,text = "Put In A Code        Or        Sign In", font = ("Courier", 20))
    canvas.create_text(515, 360, text= "Username:", font = ("Helvetica", 12))
    canvas.create_text(515, 410, text= "Password:", font = ("Helvetica", 12))
    removeallbuttons()
    username.place(x = 570, y = 350)
    password.place(x = 570, y = 400)
    entercode.place(x = 180,y = 340)
    confirmlogin.place(x = 690,y = 395)
    confirmcode.place(x = 220,y = 340)
    Createaccount.place(x = 400,y = 450)
   
def detectmouse(event):
    try:
        if event.widget.find_withtag("current"):
            clicked_object = event.widget.find_withtag("current")    
    except TypeError:
        pass
    except AttributeError:
        pass

#Buttons
username = Entry(canvas,width = 18)
password = Entry(canvas,width = 18)
entercode = Entry(canvas,width = 10)
confirmlogin = Button(tk, text = "Login", command = checklogin)
confirmcode = Button(tk, text = "Enter", command = checkcode)
Createaccount = Button(tk, text = "Create Account", command = createaccount)
Confirmaccount = Button(tk, text = "Create Account", command = confirmaccount)
selection = StringVar()  #For Creating Account Type
teacher = Radiobutton(canvas, text = "Teacher", variable = selection, value = 0) #For Creating Account Type
student = Radiobutton(canvas, text = "Student", variable = selection, value = 1) #For Creating Account Type
profilepicture = Button(tk, text = "Update Photo", command = openimage)
Logout = Button(tk, text = "Logout", command = logout)



setup()
























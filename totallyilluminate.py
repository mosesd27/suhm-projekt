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
def enteraccount(self):
    global Done
    global testrecord
    Done = False
    canvas.bind_all("<Button-1>",detectmouse)
    canvas.delete("all")
    username4.place_forget()
    password4.place_forget()
    EnterLogin.place_forget()
    Create_Account.place_forget()
    Teacher.place_forget()
    Student.place_forget()
    UploadImage.place(x = 130,y = 370)
    EnterCode.place(x = 450,y = 400)
    code.place(x = 400,y = 400)
    if self.teacher == True:
        MakeTestButton.place(x = 550,y = 300)
    viewtest(self)
    canvas.create_text(200,100,text = "Welcome %s" % self.name, font = ("Courier", 20))
    canvas.create_text(435,380,text = "Enter A Code", font = ("Courier", 20))
    canvas.create_text(580,100, text = "Your Recent Tests",font = ("Courier", 20))
    canvas.create_rectangle(100,150,300,350, fill = "grey")
    cd.place(x = 600,y = 350)
    while 1:
        if (Done == True) and (len(canvas.find_withtag("selected")) == 1):
            current = canvas.find_withtag("selected")[0]
            real2 = canvas.gettags(current)[0]
            real =  testrecord[real2]
            canvas.unbind_all("<Button-1>")
            take_test(real)
            break
        else:
            Done == False
        tk.update()
        tk.update_idletasks()

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
        



        
class accounts():
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
    
        
def viewtest(self):
    length = len(self.tests)
    if length > 10:
        length = 10
    y = 200
    for blah in range(0,length):
        canvas.create_text(500,y,text = "%s" % self.tests[blah], font = ("Courier", 12), tags = str(self.tests[blah]))
        y = y +20
def Createaccount():
    pass
#Variables
accounts = []
tests = []
activeaccount = None
#Basic Functions
scroll = Scrollbar(canvas, orient=VERTICAL)
scroll.config(command=canvas.yview)
canvas.config(yscrollcommand=scroll.set)
scroll.place(x = 795, y = 5)
def checklogin():
    ReceiveUsername = username.get()
    ReceivePassword = password.get()
    for count in range(0,len(accounts)):
        currentaccount = accounts[count]
        if (currentaccount.username == ReceiveUsername) and (currentaccount.password == ReceivePassword):
            activeaccount = currentaccount
            enteraccount()
            return True
    canvas.create_text(640,450,text = "Login Invalid", font = ("Courier", 12), fill = "red")
    return False

def checkcode():    
    ReceiveCode = entercode.get()
    for count in range(0,len(tests)):
        currenttest = tests[count]
        if (currenttest.code == ReceiveCode):
            entertest(tests[count])
            return True
    canvas.create_text(640,450,text = "Code Invalid", font = ("Courier", 12), fill = "red")
    return False


    
def buttonreload(topost = None):
    pass

def setup():
    canvas.create_text(400,150,text = "Welcome To Under\nConstruction Online Testing\nlel", font = ("Courier", 30))
    canvas.create_text(350,320,text = "Put In A Code        Or        Sign In", font = ("Courier", 20))
    canvas.create_text(515, 360, text= "Username:", font = ("Helvetica", 12))
    canvas.create_text(515, 410, text= "Password:", font = ("Helvetica", 12))
    buttonreload("login")
    username.place(x = 570, y = 350)
    password.place(x = 570, y = 400)
    entercode.place(x = 180,y = 340)
    confirmlogin.place(x = 690,y = 395)
    confirmcode.place(x = 220,y = 340)
    createaccount.place(x = 400,y = 450)

    
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
createaccount = Button(tk, text = "Create Account", command = Createaccount)





setup()
























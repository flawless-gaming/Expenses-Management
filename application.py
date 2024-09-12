from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#creating a application window
app = Tk()
app.title("Expense Management")#window title
app.geometry("600x400")#window size
app.config(bg="#030f1e")#window colour
#app.config(bg="#FAF9F6")#window colour

# Read the Image
image1 = Image.open("nightmode.png")
image2 = Image.open("daymode.png")
image3 = Image.open("login_image.jpg")
# Resize the image using resize() method
resize_image1 = image1.resize((75, 25))
resize_image2 = image2.resize((75, 25))
resize_image3 = image3.resize((200,300))
daymode = ImageTk.PhotoImage(resize_image1)
nightmode = ImageTk.PhotoImage(resize_image2)
loign_image = ImageTk.PhotoImage(resize_image3)

#darkmode and light mode function
def mode():
    global screenmode
    if screenmode:
        mode_button.config(image = nightmode)
        app.config(bg="#FAF9F6")#window colour
        header.config(bg="#FAF9F6",fg="#030f1e")
        user.config(bg="#FAF9F6",fg="#030f1e")
        underline.config(bg="#030f1e")
        pswd.config(bg="#FAF9F6",fg="#030f1e")
        underline2.config(bg="#030f1e")
        conf_pswd.config(bg="#FAF9F6",fg="#030f1e")
        underline3.config(bg="#030f1e")
        screenmode = False
    else:
        mode_button.config(image = daymode)
        app.config(bg="#030f1e")#window colour
        header.config(bg="#030f1e",fg="#FAF9F6")
        user.config(bg="#030f1e",fg="#FAF9F6")
        underline.config(bg="#FAF9F6")
        pswd.config(bg="#030f1e",fg="#FAF9F6")
        underline2.config(bg="#FAF9F6")
        conf_pswd.config(bg="#030f1e",fg="#FAF9F6")
        underline3.config(bg="#FAF9F6")
        screenmode = True

def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name=user.get()
    if name == "":
        user.insert(0,"Username")

def on_enter_pswd(e):
    pswd.delete(0,'end')
    
def on_leave_pswd(e):
    name=pswd.get()
    if name == "":
        pswd.insert(0,"Password")
        
def on_enter_cpswd(e):
    conf_pswd.delete(0,'end')
    
def on_leave_cpswd(e):
    name=conf_pswd.get()
    if name == "":
        conf_pswd.insert(0,"Confirm Password")
        
screenmode = True#screenmode set to darkmode
#screen mode button
mode_button = Button(app, image = daymode, bd='0',
                     command = mode )
mode_button.place(x=10,y=5)
image_label = Label(app,image = loign_image)
image_label.place(x=30,y=50)
header = Label(app,text="Login",font=(" Times New Roman",25,"bold"),
               bg="#030f1e",fg="#FAF9F6")
user = Entry(app,border=0,bg="#030f1e",fg="#FAF9F6",font=("Microsoft YaHei UI Light",14,"bold"))
user.insert(0,"Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>",on_leave)
underline = Frame(bg="#FAF9F6",width=250,height=3)

pswd = Entry(app,border=0,bg="#030f1e",fg="#FAF9F6",font=("Microsoft YaHei UI Light",14,"bold"))
pswd.insert(0,"Password")
pswd.bind("<FocusIn>", on_enter_pswd)
pswd.bind("<FocusOut>",on_leave_pswd)
underline2 = Frame(bg="#FAF9F6",width=250,height=3)

conf_pswd = Entry(app,border=0,bg="#030f1e",fg="#FAF9F6",font=("Microsoft YaHei UI Light",14,"bold"))
conf_pswd.insert(0,"Confirm Password")
conf_pswd.bind("<FocusIn>", on_enter_cpswd)
conf_pswd.bind("<FocusOut>",on_leave_cpswd)
underline3 = Frame(bg="#FAF9F6",width=250,height=3)

login = Button(app,text="Log In",bg="#880085",fg="#FAF9F6",font=("serif",13,"bold"))


header.place(x=355,y=20)
user.place(x=270,y=100)
underline.place(x=270,y=130)
pswd.place(x=270,y=150)
underline2.place(x=270,y=180)
conf_pswd.place(x=270,y=200)
underline3.place(x=270,y=230)
login.place(x=300,y=260,width=180)

#to generate the application
app.mainloop()
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
image4 = Image.open("hide.png")
image5 = Image.open("visible.png")
# Resize the image using resize() method
resize_image1 = image1.resize((75, 25))
resize_image2 = image2.resize((75, 25))
resize_image3 = image3.resize((200,300))
resize_image4 = image4.resize((25, 25))
resize_image5 = image5.resize((25,25))
daymode = ImageTk.PhotoImage(resize_image1)
nightmode = ImageTk.PhotoImage(resize_image2)
loign_image = ImageTk.PhotoImage(resize_image3)
hide   = ImageTk.PhotoImage(resize_image4)
visible  = ImageTk.PhotoImage(resize_image5)


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
        see_pswd.config(bg="#FAF9F6")
        underline2.config(bg="#030f1e")
        conf_pswd.config(bg="#FAF9F6",fg="#030f1e")
        see_confpswd.config(bg="#FAF9F6")
        underline3.config(bg="#030f1e")
        c_acc.config(bg="#FAF9F6",fg="#030f1e")
        c_acc_button.config(bg="#FAF9F6")
        screenmode = False
    else:
        mode_button.config(image = daymode)
        app.config(bg="#030f1e")#window colour
        header.config(bg="#030f1e",fg="#FAF9F6")
        user.config(bg="#030f1e",fg="#FAF9F6")
        underline.config(bg="#FAF9F6")
        pswd.config(bg="#030f1e",fg="#FAF9F6")
        see_pswd.config(bg="#030f1e")
        underline2.config(bg="#FAF9F6")
        conf_pswd.config(bg="#030f1e",fg="#FAF9F6")
        see_confpswd.config(bg="#030f1e")
        underline3.config(bg="#FAF9F6")
        c_acc.config(bg="#030f1e",fg="#FAF9F6")
        c_acc_button.config(bg="#030f1e")
        screenmode = True

def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name=user.get()
    if name == "":
        user.insert(0,"Username")

def on_enter_pswd(e):
    pswd.delete(0,'end')
    pswd.config(show="⦿")
    
def on_leave_pswd(e):
    name=pswd.get()
    if name == "":
        pswd.config(show="")
        pswd.insert(0,"Password")
        
def on_enter_cpswd(e):
    conf_pswd.delete(0,'end')
    conf_pswd.config(show="⦿")
    
def on_leave_cpswd(e):
    name=conf_pswd.get()
    if name == "":
        conf_pswd.config(show="")
        conf_pswd.insert(0,"Confirm Password")
        
def pswd_see():
    global see
    if see:
        see_pswd.config(image=visible)
        pswd.config(show="")
        see = False
    else:
        see_pswd.config(image=hide)
        pswd.config(show="⦿")
        see = True

def confpswd_see():
    global see
    if see:
        see_confpswd.config(image=visible)
        conf_pswd.config(show="")
        see = False
    else:
        see_confpswd.config(image=hide)
        conf_pswd.config(show="⦿")
        see = True

def colour(e):
    c_acc_button.config(fg="#0096FF")
def normal(e):
    c_acc_button.config(fg="#71797E")
        
screenmode = True#screenmode set to darkmode
see = True
#screen mode button
mode_button = Button(app, image = daymode, bd='0',
                     command = mode )
mode_button.place(x=10,y=5)
image_label = Label(app,image = loign_image)
image_label.place(x=30,y=50)
header = Label(app,text="Login",font=(" Times New Roman",25,"bold"),
               bg="#030f1e",fg="#FAF9F6")
user = Entry(app,border=0,bg="#030f1e",fg="#FAF9F6",
             font=("Microsoft YaHei UI Light",14,"bold"))
user.insert(0,"Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>",on_leave)
underline = Frame(bg="#FAF9F6",width=250,height=3)

pswd = Entry(app,border=0,bg="#030f1e",fg="#FAF9F6",
             font=("Microsoft YaHei UI Light",14,"bold"))
pswd.insert(0,"Password")
pswd.bind("<FocusIn>", on_enter_pswd)
pswd.bind("<FocusOut>",on_leave_pswd)
see_pswd = Button(app,image=hide,bg="#030f1e",bd=0,command=pswd_see)
underline2 = Frame(bg="#FAF9F6",width=250,height=3)

conf_pswd = Entry(app,border=0,bg="#030f1e",fg="#FAF9F6",
                  font=("Microsoft YaHei UI Light",14,"bold"))
conf_pswd.insert(0,"Confirm Password")
conf_pswd.bind("<FocusIn>", on_enter_cpswd)
conf_pswd.bind("<FocusOut>",on_leave_cpswd)
see_confpswd = Button(app,image=hide,bg="#030f1e",
                      bd=0,command=confpswd_see)
underline3 = Frame(bg="#FAF9F6",width=250,height=3)

login = Button(app,text="Log In",bg="#880085",fg="#FAF9F6",
               font=("serif",13,"bold"),cursor="hand2")

c_acc = Label(app,text="Don't have an account ?",font=("forte",10),
              bg="#030f1e",fg="#FAF9F6")
c_acc_button = Button(app,text="Create Account",font=("serif",10,"bold"),
                      bg="#030f1e",fg="#71797E",bd=0,cursor="hand2")
c_acc_button.bind("<Enter>",colour)
c_acc_button.bind("<Leave>",normal)

header.place(x=355,y=20)
user.place(x=270,y=100)
underline.place(x=270,y=130)
pswd.place(x=270,y=150)
see_pswd.place(x=525,y=150)
underline2.place(x=270,y=180)
conf_pswd.place(x=270,y=200)
see_confpswd.place(x=525,y=200)
underline3.place(x=270,y=230)
login.place(x=320,y=250,width=180)
c_acc.place(x=270,y=300)
c_acc_button.place(x=415,y=298)

#to generate the application
app.mainloop()
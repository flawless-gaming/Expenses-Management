from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#creating a application window
app = Tk()
app.title("Expense Management")#window title
app.geometry("600x400")#window size
app.config(bg="#0e1111")#window colour
#app.config(bg="#FAF9F6")#window colour

# Read the Image
image1 = Image.open("nightmode.png")
image2 = Image.open("daymode.png")
# Resize the image using resize() method
resize_image1 = image1.resize((75, 25))
resize_image2 = image2.resize((75, 25))
daymode = ImageTk.PhotoImage(resize_image1)
nightmode = ImageTk.PhotoImage(resize_image2)

#darkmode and light mode function
def mode():
    global screenmode
    if screenmode:
        mode_button.config(image = nightmode)
        app.config(bg="#FAF9F6")#window colour
        header.config(bg="#FAF9F6",fg="#0e1111")
        screenmode = False
    else:
        mode_button.config(image = daymode)
        app.config(bg="#0e1111")#window colour
        header.config(bg="#0e1111",fg="#FAF9F6")
        screenmode = True

def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name=user.get()
    if name == "":
        user.insert(0,"Username")
    

screenmode = True#screenmode set to darkmode
#screen mode button
mode_button = Button(app, image = daymode, bd='0',
                     command = mode )
mode_button.place(x=10,y=5)

header = Label(app,text="Login",font=(" Times New Roman",25,"bold"),
               bg="#0e1111",fg="#FAF9F6")
user = Entry(app,border=0,bg="#0e1111",fg="#FAF9F6",font=("Microsoft YaHei UI Light",14,"bold"))
user.insert(0,"Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>",on_leave)

gender = [
    "Gender",
    "Male",
    "Female",
    "Not Specified"
]
clicked=StringVar()
clicked.set("Gender")
drop = OptionMenu(app,clicked,*gender)
drop.config(border=0,bg="#0e1111",fg="#FAF9F6",font=("Microsoft YaHei UI Light",14,"bold"))
drop["menu"].config(border=0,bg="#0e1111",fg="#FAF9F6",font=("Microsoft YaHei UI Light",14,"bold"))
age = Label(app,text="Age",bg="#0e1111",fg="#FAF9F6",font=("Microsoft YaHei UI Light",14,"bold"))
spinbox = Spinbox(app, from_=0, to=100, width=5, relief="sunken", repeatdelay=500, repeatinterval=100,
                     bg="#0e1111",fg="#FAF9F6",font=("Microsoft YaHei UI Light",13,"bold"))
# Setting options for the Spinbox
spinbox.config(state="normal", cursor="hand2", bd=3, justify="center", wrap=True,buttonbackground="#0e1111",buttoncursor="hand2")
login = Button(app,text="Log In",bg="#880085",fg="#FAF9F6",font=("serif",13,"bold"))

header.place(x=275,y=30)
user.place(x=220,y=100)
drop.place(x=240,y=140)
age.place(x=220,y=190)
spinbox.place(x=280,y=190,)
login.place(x=220,y=240,width=180)

#to generate the application
app.mainloop()
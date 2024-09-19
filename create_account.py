from tkinter import *
from tkvideo import tkvideo

def create_page():
    app = Tk()
    app.title("Create Account")
    app.geometry("805x605")
    app.config(bg="#030f1e")
    
    bg_video = Label(app)
    bg_video.place(x=0,y=0)
    bg_player = tkvideo("video.mp4",bg_video,loop=1,size=(800, 600))
    bg_player.play()
    
    back = Button(app,bg = "#0c0b0b" , fg = "#FAF9F6" , text="<<BACK" , command=app.destroy)
    back.place(x=15,y=10)
    
    frame = Frame(app , bg = "white" , width = 550  , height = 500 )
    frame.place(x=125,y=50)
    
    header = Label(frame,text="Create Account",bg = "#0c0b0b" , fg = "#FAF9F6",font=("Arial",25,"bold"))
    f_name = Entry(frame,bg = "#0c0b0b" , fg = "#FAF9F6",font=("Arial",18),bd=1,width=12)
    f_name.insert(0,"First Name")
    l_name = Entry(frame,bg = "#0c0b0b" , fg = "#FAF9F6",font=("Arial",18),bd=1,width=12)
    l_name.insert(0,"Last Name")
    email =  Entry(frame,bg = "#0c0b0b" , fg = "#FAF9F6",font=("Arial",18),bd=1,width=21)
    email.insert(0,"Email")
    verify_email = Button(frame,bg = "#FF3131" , fg = "#FAF9F6",font=("Arial",13),text="Verify",width=8)
    verify_email.place(x=385,y=148.5)
    username = Entry(frame,bg = "#0c0b0b" , fg = "#FAF9F6",font=("Arial",18),bd=1,width=18)
    username.insert(0,"Username")
    pswd = Entry(frame,bg = "#0c0b0b" , fg = "#FAF9F6",font=("Arial",18),bd=1,width=18)
    pswd.insert(0,"Password")
    conf_pswd = Entry(frame,bg = "#0c0b0b" , fg = "#FAF9F6",font=("Arial",18),bd=1,width=18)
    conf_pswd.insert(0,"Confirm Password")
    submit = Button(frame,bg = "#FF3131" , fg = "#FAF9F6",font=("Arial",15),text="Submit",width=20)
    submit.place(x=160,y=350)
    conf_pswd.place(x=80,y=300)
    pswd.place(x=80,y=250)
    username.place(x=80,y=200)
    email.place(x=80,y=150)
    l_name.place(x=310,y=100) 
    f_name.place(x=80,y=100)
    header.place(x=160,y=10)
    
    app.mainloop()
    
create_page()
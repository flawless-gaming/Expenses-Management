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
    
    frame = Frame(app , bg = "#0c0b0b" , width = 550  , height = 500 )
    frame.place(x=125,y=50)

    back = Button(app,bg = "#0c0b0b" , fg = "#FAF9F6" , text="<<BACK" , command=app.destroy)
    back.place(x=15,y=10)
    
    
    
    app.mainloop()
    
create_page()
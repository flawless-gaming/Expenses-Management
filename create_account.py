from tkinter import *
from tkvideo import tkvideo

def create_page():
    app = Tk()
    app.title("Create Account")
    app.geometry("643x365")
    app.config(bg="#030f1e")
    
    bg_video = Label(app)
    bg_video.place(x=0,y=0)
    bg_player = tkvideo("video.mp4",bg_video,loop=1)
    bg_player.play()
    
    app.mainloop()
    
create_page()
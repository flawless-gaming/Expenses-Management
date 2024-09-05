from tkinter import *

#creating a application window
app = Tk()
app.title("Expense Management")#window title
app.geometry("300x200")#window size
app.config(bg="#0e1111")#window colour
#app.config(bg="#FAF9F6")#window colour

daymode = PhotoImage(file="daymode.png")
nightmode = PhotoImage(file="nightmode.png")

def mode():
    global screenmode
    if screenmode:
        mode_button.config(image = nightmode)
        app.config(bg="#FAF9F6")#window colour
        screenmode = False
    else:
        mode_button.config(image = daymode)
        app.config(bg="#0e1111")#window colour
        screenmode = True

screenmode = False

mode_button = Button(app, image = daymode, bd='0',
                     command = mode)
mode_button.pack(pady = 50)


app.mainloop()
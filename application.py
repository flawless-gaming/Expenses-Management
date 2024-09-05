from tkinter import *
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
        screenmode = False
    else:
        mode_button.config(image = daymode)
        app.config(bg="#0e1111")#window colour
        screenmode = True

screenmode = True#screenmode set to darkmode
#screen mode button
mode_button = Button(app, image = daymode, bd='0',
                     command = mode )
mode_button.place(x=10,y=5)



#to generate the application
app.mainloop()
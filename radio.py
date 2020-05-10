from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('E:/Gitstaffs/guis/Acquisition.ico')

#Create radio button function
def radio():
    if v.get() == "one":
        my_label = Label(root, text="You clicked Radio Button One")
    else:
        my_label = Label(root, text="You clicked Radio Button Two")

    my_label.pack(pady=10)

#Radio Buttons
v = StringVar()
v.set("one") # default value

rbutton_1 = Radiobutton(root, text="One", variable=v, value="one").pack()
rbutton_2 = Radiobutton(root, text="Two", variable=v, value="two").pack()


my_button = Button(root, text="Click me!", command=radio)
my_button.pack(pady=20)





root.mainloop()
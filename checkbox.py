from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('E:/Gitstaffs/guis/Acquisition.ico')

#Create toppings function

def toppings():
    if v.get() == "pepperoni":
        my_label = Label(root, text="You have ordered pepperoni")
    else:
        my_label = Label(root, text="You don't want pepperoni")
    # my_label = Label(root, text=v.get())
    my_label.pack(pady=10)



#Check Boxes
v = StringVar()

my_check = Checkbutton(root, text="Pepperoni", variable=v, onvalue="pepperoni", offvalue="no_pepperoni")
my_check.deselect()
my_check.pack()

my_button =Button(root, text="Select Toppings", command=toppings).pack(pady=10)
root.mainloop()
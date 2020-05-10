from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x700")
root.iconbitmap('E:/Gitstaffs/guis/Acquisition.ico')
#Create clicked function

my_label2 = Label(root)

def clicked():
    global my_label2
    input = e.get()
    global my_label2
    clear()
    # my_label2.destroy()
    my_label2 = Label(root, text="Hello " + input )
    my_label2.pack()

def hide():
    my_label2.pack_forget()
    #grid system can use gird_forget() and destroy() also works if you want the label disappear forever
def show():
    my_label2.pack()

def clear():
     my_label2.pack_forget()
     # my_label2.destroy()

# Add Images
my_image = ImageTk.PhotoImage(Image.open("kyoani.jpg"))
image_label = Label(image=my_image)
image_label.pack()

# Create a label
my_label = Label(root, text="Enter your name")
my_label.pack()
#grid(row=0, column=0, columnspan=2)

# grid & pack 不能同时用
#my_label2 = Label(root, text="second thing!")
#my_label2.grid(row=1, column=0)

#my_label3 = Label(root, text="third thing!")
#my_label3.grid(row=2, column=1)

#Create Entry Widget Input Box
e = Entry(root, font=("Helvetica", 18))
e.pack(pady=20)

# Create button
my_button = Button(root, text="Click me !", command=clicked )
my_button.pack(pady=20)

# hide_button = Button(root, text="Hide", command=hide )
# hide_button.pack(pady=20)

# show_button = Button(root, text="Show", command=show )
# show_button.pack(pady=20)

clear_button = Button(root, text="clear", command=clear).pack(pady=10)

root.mainloop()
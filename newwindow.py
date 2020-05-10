from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('E:/Gitstaffs/guis/Acquisition.ico')

#Create second window function
def open_window():
    new = Toplevel()
    new.title("second window")
    new.geometry("400x400")
    new.iconbitmap('E:/Gitstaffs/guis/Acquisition.ico')
    my_label = Label(new, text="label in second window")
    my_label.pack()

    my_img = ImageTk.PhotoImage(Image.open("kyoani.jpg"))
    img_label = Label(new, image=my_img)
    img_label.pack(pady=5)

    destroy_button = Button(new, text="Quit", command=new.destroy)
    destroy_button.pack(pady=5)

    # Minimize Original window
    # hide_button = Button(new, text="hide the window", command=root.iconify).pack()
    # show_button = Button(new, text="show the window", command=root.deiconify).pack()

    # Withdraw Original Window
    hide_button = Button(new, text="hide the window", command=root.withdraw).pack()
    show_button = Button(new, text="show the window", command=root.deiconify).pack()

    kill_original = Button(new, text="Quit original ", command=root.destroy).pack()

    new.mainloop()


# Create New Windows
my_button = Button(root, text="Open 2nd window", command=open_window).pack()















root.mainloop()
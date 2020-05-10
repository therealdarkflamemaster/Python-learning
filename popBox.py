from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('E:/Gitstaffs/guis/Acquisition.ico')

# Create popup function
def popup():
    # messagebox.showinfo("Popup Title", "Look at my popup message")
    response = messagebox.askquestion("Popup Title", "Look at my popup message")
    my_label = Label(root, text=response).pack(pady=10)
    if response == 1:
        my_label = Label(root, text="you clicked yes").pack(pady=10)
    else:
        my_label = Label(root, text="you clicked no").pack(pady=10)

# Popup Boxes
# show info, showwarning, showerror, askquestion, askokcancel, askyesno

pop_button = Button(root, text="Click to pop up !", command=popup)
pop_button.pack(pady=20)

root.mainloop()
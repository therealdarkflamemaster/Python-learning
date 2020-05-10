from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('E:/Gitstaffs/guis/Acquisition.ico')

# Create Select function
def select():
    if my_combo.get() == "monday":
        my_label = Label(root, text="Monday you have chosen").pack(pady=10)
    elif my_combo.get() == "tuesday":
        my_label = Label(root, text="Tuesday you have chosen").pack(pady=10)
    else:
        my_label = Label(root, text="Wednesday you have chosen").pack(pady=10)

    my_label = Label(root, text=my_combo.get()).pack(pady=10)


# Combo Boxes
options = [
    "monday",
    "tuesday",
    "wednesday"
]
my_combo = ttk.Combobox(root, value=options)
my_combo.current(1) # default value
my_combo.pack(pady=10)

my_button = Button(root, text="select", command=select).pack()

root.mainloop()
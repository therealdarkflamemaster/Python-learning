from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
# root.geometry("400x400")
root.iconbitmap('E:/Gitstaffs/guis/Acquisition.ico')

def fake_command():
    pass

def new():
    hide_menu_frames()
    current_status.set("File status")
    file_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

def cut():
    hide_menu_frames()
    current_status.set("Cut status")
    edit_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)


def hide():
    file_frame.grid_forget()

def show():
    file_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

def hide_menu_frames():
    edit_frame.grid_forget()
    file_frame.grid_forget()

# Define a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu Items
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_separator()
file_menu.add_command(label="Close", command=root.quit)

# Create another submenu Edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=fake_command)
edit_menu.add_command(label="Paste", command=fake_command)
'''
show_button = Button(root, text="Show", command=show)
hide_button = Button(root, text="Hide", command=hide)

show_button.grid(row=0, column=0)
hide_button.grid(row=0, column=1)
'''
#File Menu Frame
file_frame = Frame(root, width=400, height=400, bd=5, bg="blue", relief="sunken")
# file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

file_frame_label = Label(file_frame, text="File Frame", font=("Helvetica", 20))
file_frame_label.pack(padx=20, pady=20)

#Edit Menu Frame
edit_frame = Frame(root, width=400, height=400, bd=5, bg="blue", relief="sunken")
# edit_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

edit_frame_label = Label(edit_frame, text="Cut Frame", font=("Helvetica", 20))
edit_frame_label.pack(padx=20, pady=20)

current_status = StringVar()
current_status.set("Waiting")


my_status = Label(root, textvariable=current_status, bd=2, relief="sunken", width=56, anchor=E)
my_status.grid(row=1, column=0)

root.mainloop()
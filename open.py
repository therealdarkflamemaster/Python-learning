from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('E:/Gitstaffs/guis/Acquisition.ico')


# Create open dialog box function
def open_image():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Open a image file",
                                               filetypes=(("JPG File", "*.jpg"), ("All Files", "*.*")))
    my_label = Label(root, text=root.filename).pack(pady=10)
    global my_img
    # Open image and print on screen
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = Label(root, image=my_img)
    img_label.pack(pady=10)

# Open Dialog Box

my_button = Button(root, text="Open Image", command=open_image).pack(pady=10)















root.mainloop()
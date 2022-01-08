from tkinter import Tk, Label  # specifically imports Tk and Label rather than * (global)
                               # global import (*) caused problems
root = Tk()  # creates main window object (named root)
root.title("First_Program")  # gives a title to the main window

label = Label(root, text = "Hello world!")  # output shown in the window
label.pack()

root.mainloop()

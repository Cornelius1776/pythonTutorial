# In python GUI, there are 2 main components
# widgets: these are GUI elements such as textboxes, labels, buttons, images.
# windows: this is a container that holds the widgets
from tkinter import *

count = 0

fruits = ["Apple", "Strawberry", "Banana", "Watermelon"]


def click_button():
    global count
    count += 1
    if count == 1:
        print("You have clicked the button once")
    else:
        print(f"You have clicked the button {count} times")


def submit():
    user_name = my_entry.get()
    print(f"Hi {user_name}")


def delete():
    my_entry.delete(0, END)


def backspace():
    my_entry.delete(len(my_entry.get())-1, END)


def show():
    if var.get() == 1:
        print("No")
    else:
        print("yes")


window = Tk()  # this intantiates object window, an instance of Tk class
window.geometry("500x500")
window.title("Aeon")

icon = PhotoImage(file="images.png")  # converts the image to become usable
window.iconphoto(True, icon)

window.config(background="#4fa3a5")  # changes the screen background color

# label is an area that holds text and/or image in the window
label_image = PhotoImage(file="screen.png")

my_label = Label(window,
                 text="Hello Aeon",
                 font=("Arial", 15, "bold"),
                 foreground="#264248",
                 background="#FDAE38",
                 relief=RAISED, bd=5,
                 padx=10,
                 pady=5,
                 # image=label_image,
                 )
my_label.pack()

# Buutons
my_button = Button(window,
                   text="click here",
                   command=click_button,
                   font=("comic sans", 15),
                   foreground="#F9AC66",
                   background="#876D97",
                   activebackground="#876D97",
                   activeforeground="#F9AC66",
                   # state=DISABLED # disables the button
                   )
my_button.pack()

my_entry = Entry(window,
                 font=("comic sans", 10),
                 foreground="#876D97",
                 background="black",
                 # show="*",  # This hides the text, useful for passwords
                 )
my_entry.pack(side=LEFT)


submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)


delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)


backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)


# Check button
var = IntVar()  # on/offvalues must be of the variable type int, bool, etc
check_button = Checkbutton(window,
                           text="Is the earth flat?",
                           variable=var,
                           onvalue=1,
                           offvalue=0,
                           command=show,
                           font=("comic sans", 15),
                           foreground="green",
                           activeforeground="green",
                           background="black",
                           activebackground="black",
                           )
check_button.pack()

# mainloop() listens for events and displays the window on the computer screen,and should always be
# at the bottom
window.mainloop()

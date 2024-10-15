# Radiobutton is used to select one item from a group
from tkinter import *

fruits = ["Apple", "Strawberry", "Banana", "Watermelon"]


def eat():
    if fruit.get() == 0:
        print("I want to eat an apple")
    elif fruit.get() == 1:
        print("I've never taste a strawberry before, I'd love to have one")
    elif fruit.get() == 2:
        print("I'll take the banana")
    elif fruit.get() == 3:
        print("yummm i love watermelons")


my_window = Tk()
my_window.geometry("400x400")
my_window.title("Radio button")

apple_image = PhotoImage(file="apple.png")
strawberry_image = PhotoImage(file="strawberry.png")
banana_image = PhotoImage(file="banana.png")
watermelon_image = PhotoImage(file="watermelon.png")

fruit_images = [apple_image, strawberry_image, banana_image, watermelon_image]

fruit = IntVar()  # enables the item to be ticked, value=i enables individual ticking

for i in range(len(fruits)):
    radio_button = Radiobutton(my_window,
                               text=fruits[i],
                               variable=fruit,
                               value=i,
                               padx=20,
                               font=("comic sans", 25),
                               # adds image to radio buttons
                               image=fruit_images[i],
                               compound="right",  # makes both image and text visible
                               command=eat  # calls thhe function for the buttons
                               )

    radio_button.pack(anchor=W)


my_window.mainloop()

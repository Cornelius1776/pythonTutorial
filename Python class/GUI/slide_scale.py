from tkinter import *

my_title = "Sliding scale"


def check():
    print(f"The temperature is {my_scale.get()} degrees C")


window = Tk()
window.title(my_title)

my_scale = Scale(window,
                 from_=100,
                 to=0,
                 length=650,
                 orient=VERTICAL,  # or horizontal
                 font=("consolas", 15),
                 tickinterval=10,
                 # showvalue=False,  # this will hide the number of the slide
                 # resolution=5, # this set the slider to increment and decrement at a certain value
                 troughcolor="#264248",
                 foreground="red",
                 background="black",
                 )

# set() is used to set the scale at a specific point
# my_scale.set(50) this is not flexible, it will remain at 50 even if the scale is increased

# this is flexible even if the scale is increased
my_scale.set(((my_scale["from"] - my_scale["to"]) / 2) + my_scale["to"])

my_scale.pack()

my_button = Button(window,
                   text="check",
                   command=check,
                   font=("comic sans", 15),
                   )

my_button.pack()

window.mainloop()

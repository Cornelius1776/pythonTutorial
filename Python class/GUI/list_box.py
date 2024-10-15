from tkinter import *


def buy():
    """
    # functionality for multiple item selection
     dishes = []
    for i in my_listbox.curselection():
        dishes.insert(i, my_listbox.get(i))

    for i in dishes:
        print(F"You have ordered {i} in your cart")
 """
    print(f"You have ordered {my_listbox.get(my_listbox.curselection())}")


def add_to_menu():
    my_listbox.insert(my_listbox.size(), entry_box.get())
    my_listbox.config(height=my_listbox.size())


def delete():
    entry_box.delete(0, END)


def menu_delete():
    """ 
    # Functionality for multiple deletes
    for i in reversed(my_listbox.curselection()):
        my_listbox.delete(i)
 """
    print(
        f"You have removed {my_listbox.get(my_listbox.curselection())} from the menu")

    my_listbox.delete(my_listbox.curselection())
    my_listbox.config(height=my_listbox.size())


window = Tk()

my_listbox = Listbox(window,
                     foreground="#4FA3A5",
                     font=("roboto", 20),
                     width=15,
                     selectmode=MULTIPLE  # enables selecting more than one item
                     )
my_listbox.pack()

my_listbox.insert(1, "Sharwama")
my_listbox.insert(2, "Cow leg peppersoup")
my_listbox.insert(3, "Spaghetti")
my_listbox.insert(4, "Fish peppersoup")
my_listbox.insert(5, "Turkey peppersoup")


my_listbox.config(height=my_listbox.size())

# Entry box
entry_box = Entry(window)
entry_box.pack()

# add button for entry box
add_button = Button(window,
                    text="add to menu",
                    command=add_to_menu)

add_button.pack()

# delete button for entry box
delete_button = Button(window,
                       text="Delete",
                       command=delete)

delete_button.pack()


# deletes items on the menu
delete_menu_item = Button(window,
                          text="delete item",
                          command=menu_delete)

delete_menu_item.pack()

# Buy button
buy_button = Button(window,
                    text="Buy",
                    command=buy)

buy_button.pack()
window.mainloop()

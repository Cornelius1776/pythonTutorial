class Phone:
    color = "pink"


class Earpod:
    color = None


def change_color(obj, color):
    obj.color = color


p_1 = Phone()
p_2 = Phone()
p_3 = Phone()

change_color(p_1, "blue")
change_color(p_2, "white")
change_color(p_3, "red")

print(p_1.color)
print(p_2.color)
print(p_3.color)


e_1 = Earpod()
e_2 = Earpod()

change_color(e_1, "black")
change_color(e_2, "purple")

print(e_1.color)
print(e_2.color)

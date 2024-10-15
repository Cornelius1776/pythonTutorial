# map() executes a function for items in an iterable individually
phones = [("iPhone 14", "Apple", 1099),
          ("S 23", "Samsung", 1199),
          ("Pixel 7", "Google", 700)]


def to_naira(element):
    return element[0], element[2] * 550


jumia = list(map(to_naira, phones))
for i in jumia:
    print(i)

# sort() method rearranges the elements of the list alphabetically works only for list

fruits = ["Mango", "Strawberry", "Cashew", "Apple"]
fruits.sort()
# fruits.sort(reverse=True) print the reverse
for fruit in fruits:
    print(fruit)


# sorted() works for iterables
# tuples
carnivores = ("lion", "sharks", "crocodiles", "tiger")
sorted_canivores = sorted(carnivores)
#sorted_canivores = sorted(carnivores, reverse=True)
for animal in sorted_canivores:
    print(sorted_canivores)

# list of tuples using sort()
phones = [("iPhone 14", "Apple", 2022),
          ("S 23", "Samsung", 2023),
          ("Pixel 7", "Google", 2022)]

# The index of the elements in the tuple declared in a lambda function can be used to sort


def element(element): return element[0]


phones.sort(key=element)
for phone in phones:
    print(phone)


# tiple of tuples using sorted()
laptops = (("M1 Macbook pro", "Apple", 2021),
           ("Dell xps 17", "Dell", 2022),
           ("Envy", "HP", 2023))


def item(item): return item[1]


sorted_item = sorted(laptops, key=item)

for i in sorted_item:
    print(i)

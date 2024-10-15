names = ["John", "Sam", "Trust", "Ola"]
for name in names:
    print(f'Hi {name}')

for name in names:
    print(f"Hi {name}")
    if name == "Trust" or name == "Ola":
        print(f"{name} is my personal padi")


# linear search using range
def search_1(a, target):
    for i in range(len(a)):
        if a[i] == target:
            print(f'{target} found at index {i}')
            return
    print(f'{target} not found!')


search_1(names, "Ola")


# linear search using enumerate
def search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            print(f'{target} was found at index {index}')
            return

    print(f'{target} not found!')


price = [3, 2, 5, 24, 15, 7]
search(price, 2)

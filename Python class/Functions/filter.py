# filter() creates a collection of similar items that meets a criteria from an iterable.
phones = [("iPhone 14", "Apple", 2022),
          ("iPhone 11", "Apple", 2019),
          ("S 23", "Samsung", 2023),
          ("Note 9", "Samsung", 2018),
          ("Note 20 ultra", "Samsung", 2020),
          ("Pixel 7", "Google", 2022)]


def year(element):
    return element[2] >= 2020


refresh_rate_120 = list(filter(year, phones))
for i in refresh_rate_120:
    print(i)

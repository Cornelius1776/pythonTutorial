class Phone:
    # class variables/attributes similar to global variables but inside a class
    network = "5G"
    is_flagship = True
    all: list = []

    # Constructor or init
    # self represents the object
    # type casting can be done to prevent the parameters from receiving the wrong argument type
    # e.g. name: str, year: int, etc. This ensures the proper types are used.
    # assert can be used to run validations
    def __init__(self, name, color, year, company):
        print(f"Constructor called for {name} ")

        # assert year to the age of smartphones
        assert year >= 2007, f"{year} is longer than the age of smartphones"

        # instance variables/attributes
        self.m_name = name
        self.m_color = color
        self.m_year = year
        self.m_company = company

        Phone.all.append(self)

    # instance methods
    def __repr__(self) -> str:  # this allows Phone.all to display the objects as strings
        return f"Device is( {self.m_name}, {self.m_color}, {self.m_year}, {self.m_company})"

    def description(self):
        print(
            f"My {self.m_name} was made by {self.m_company} in {self.m_year}, the color's {self.m_color} ")


# instantiation
phone_1 = Phone("iPhone 14", "white", 2022, "Apple")
print(phone_1.m_name)
print(phone_1.m_color)
phone_1.description()

phone_2 = Phone("S 22", "Burgundy", 2022, "Samsung")
phone_2.description()

phone_3 = Phone("Note 10 plus", "Aura glow", 2019, "Samsung")
phone_3.network = "4G"
print(phone_3.network)
print(phone_3.is_flagship)
phone_3.description()

# the class can change class variables for all the objects
Phone.is_flagship = False

phone_4 = Phone("Spark 8", "grey", 2022, "Techno")
phone_4.network = "4G"
print(phone_4.network)
print(phone_4.is_flagship)
phone_4.description()

# See Class attributes printed as a dictionary
print(Phone.__dict__)

# See instance attributes
print(phone_1.__dict__)
print(phone_2.__dict__)
print(phone_3.__dict__)

# prints the objects and their memory addresses
print(Phone.all)

for my_object in Phone.all:
    print(my_object.m_name)

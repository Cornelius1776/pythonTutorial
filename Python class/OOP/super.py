# Super() helps to prevent repetition of code
"""
# without super()
class Electronic:
    pass # just a placeholder

class Phone(Electronic):

    def __init__(self, name, color, company):
        self.m_name = name
        self.m_color = color
        self.m_company = company

    def description(self):
        print(f"The name of the phone is {self.m_name} made by {self.m_company}, with a {self.m_color} color.")


class Airpod(Electronic):

    def __init__(self, name, color):
        self.m_name = name
        self.m_color = color
        
    def description(self):
        print(
            f"The name of the pod is {self.m_name}, and the color is {self.m_color}") """


# With super()
class Electronic:
    def __init__(self, name, color):
        self.m_name = name
        self.m_color = color


class Phone(Electronic):

    def __init__(self, name, color, company):
        super().__init__(name, color)
        self.m_company = company

    def description(self):
        print(
            f"The name of the phone is {self.m_name} made by {self.m_company}, with a {self.m_color} color.")


class Airpod(Electronic):
    def __init__(self, name, color):
        super().__init__(name, color)

    def description(self):
        print(
            f"The name of the pod is {self.m_name}, and the color is {self.m_color}")


phone_1 = Phone("iPhone 14", "white", "Apple")
pod = Airpod("buds pro", "black")

pod.description()
phone_1.description()

class Animal:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def print_height(self):
        print(f'height is {self.height}')

    @statistics
    def greet():
        print("greet")

animal = Animal(height=180, weight=30)
animal.print_height()

class Dog(Animal):
    def __init__(self, height, weight):
        super().__init__(height=height, weight=weight)

    @classmethod
    def greet(self):
        print("woof woof")


dog = Dog(height=100, weight=20)
dog.greet()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age)) #This is like calling init
    
    def print_details(self):
        print(f'The age of {self.name} is {self.age}')

p1 = Person.from_string('Python, 33')
p1.print_details()
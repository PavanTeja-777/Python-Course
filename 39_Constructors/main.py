#class with Default constructor
class Language_without_init:
    name = 'Python'
    invented = 1989

    # Default Constructor
    def __init__(self):
        print('This is a default constructor')

    def print_details(self):
        print(f'{self.name} was invented in {self.invented}')

#class with Parameter constructor
class Language_with_init:

    # Parameter Constructor
    def __init__(self,name,invented):
        self.name = name
        self.invented = invented
        print('__init__ with args has been invoked')

    def print_details(self):
        print(f'{self.name} was invented in {self.invented}')

py = Language_without_init()
java = Language_with_init('Java', 1995)

py.print_details()
java.print_details()
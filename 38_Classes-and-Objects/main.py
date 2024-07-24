#creating a class
class Language:
    name = 'Python' # Default Values
    invented = 1989 # Default Values

    def print_details(self): #Self refers to the same obj
        print(f'{self.name} was invented in {self.invented}')

#creating object
py = Language()
java = Language()

#accessing class methods
java.name = 'Java'
java.invented = 1995

py.print_details()
java.print_details()
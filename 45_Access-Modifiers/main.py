# Public
class Cokroach:
    # constructor is defined
    def __init__(self, name):
        self.name = name             # public variable

joey = Cokroach('Joey')
print(joey.name)  # Joey

# Private
class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
print(obj.__age)       # AttributeError: type object 'Student' has no attribute '__age'
print(obj.__funName()) # AttributeError: type object 'Student' has no attribute '__funName()'

# calling by object  of class Subject
print(obj1.__age)       # AttributeError: type object 'Subject' has no attribute '__age'
print(obj1.__funName()) # AttributeError: type object 'Subject' has no attribute '__funName()'

# Protected
class Student:
    def __init__(self):
        self._name = "XYZ"   # Protected Variable

    def _funName(self):      # Protected method
        return "My self XYZ"

class Subject(Student):       #Inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      # XYZ
print(obj._funName()) # My self XYZ
 
# calling by object of Subject class
print(obj1._name)      # XYZ
print(obj1._funName()) # My self XYZ
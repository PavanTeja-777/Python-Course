# Access Specifiers/Modifiers
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

Let us see the each one of access specifiers in detail:
# Types of access specifiers
## 1. Public Access Specifier
All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
### Example:
```py
class Cokroach:
    # constructor is defined
    def __init__(self, name):
        self.name = name             # public variable

joey = Cokroach('Joey')
print(joey.name)  # Joey
```

## 2. Private Access Modifier
By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

- In Python, there is no strict concept of "private" access modifiers like in some other programming languages.
- However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__).
- This is known as a "weak internal use indicator" and it is a convention only, not a strict rule.
- Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.
### Example:
```py
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
```

Private members of a class cannot be accessed or inherited outside of class. If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error.

# 3. Protected Access Modifier
In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. 

- In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). 
- For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

## Example:
```py
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
```

## Note:
- Python doesn't supports strictly implementation of private and protected variables, they are just naming conventions
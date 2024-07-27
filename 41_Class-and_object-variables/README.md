# Instance vs Class variables
## Class Variables
- Class variables are defined at the class level and are shared among all instances of the class. 
- They are defined outside of any method and are usually used to store information that is common to all instances of the class. 

## Instance Variables
- Instance variables are defined at the instance level and are unique to each instance of the class. 
- They are defined inside the \_\_init__ method and are usually used to store information that is specific to each instance of the class.

Example:
```py
class Fruit:

    objectsCreated = 0

    def __init__(self, name, color):
        Fruit.objectsCreated += 1
        self.name = name
        self.color = color
    
    def __repr__(self):
        return f'{self.name} is {self.color} color'


orange = Fruit('Orange', 'Orange')
print(orange)
print(Fruit.objectsCreated)

banana = Fruit('Banana', 'Yellow')
print(banana)
print(Fruit.objectsCreated)
```
Output:
```
Orange is Orange color
1
Banana is Yellow color
2
```

In the above example `objectsCreated` is a class variable like a global variable for all instances and `name` & `color` are instance variable, they are different for every instance
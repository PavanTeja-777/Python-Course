# Inheritance
When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

## Inheritance Syntax
```python
class BaseClass:
    ...
    # Body of base class
class DerivedClass(BaseClass):
    ...
    # Body of derived class
```

### Example
```py
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Example usage
my_dog = Dog()
my_dog.make_sound()
```
### Output :
```
Woof
```
Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

## Types of inheritance:
1. **Single** Inheritance
   - The Inheritance in which a class derived properties only from a single Base class
   - This can be done by using `class Derived(Base)`

2. **Multiple** Inheritance
   - The Inheritance in which a class derived properties from a 2 or more Base class.
   - This can be done by using `class Derived(Base1, Base2)`

3. **Multilevel** Inheritance
   - The Inheritance a class is derived form which is derived from another class. This is similar to a relationship representing a child and a grandfather.
   - This can be done by using `class Derived1(Base)` & `class Derived2(Derived1)`

4. **Hierarchical** Inheritance
   - The Inheritance in which many classes are derived from a Single Base class
   - This can be done by using `class Derived1(Base)` & `class Derived2(Base)`

5. **Hybrid** Inheritance
   - The Inheritance consisting of multiple types of inheritance is called hybrid inheritance.


For Examples Check [main.py](main.py)
# Getters
- Getters in Python are methods that are used to access the values of an object's properties.
- They are used to return the value of a specific property, and are typically defined using the `@property` decorator.

Here is an example of a simple class with a getter method:
```python
class MyClass:
    def __init__(self, value):
        self.value = value

    @property
    def val(self):
        return self.value
```
In this example, the MyClass class has a single property, value, which is initialized in the \_\_init__ method. The val method is defined as a getter using the `@property` decorator, and is used to return the value of the value property.

To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute:
```python
obj = MyClass(10)
print(obj.val) #Getter #Output:10
```
# Setters
- It is important to note that the getters do not take any parameters and we cannot set the value through getter method.
- For that we need setter method which can be added by decorating method with `@property_name.setter`

Here is an example of a class with both getter and setter:

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    @property
    def val(self):
        return self.value

    @val.setter
    def val(self, new_value):
        self.value = new_value
```
We can use setter method like this:
```python
obj = MyClass(10)
obj.val = 20 # Setter
print(obj.val) #Output: 20
```
In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for **encapsulation** and data validation.
# Dunder Method

- These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behavior.

- They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

Let’s take a look at some of the most commonly used magic methods in Python.

## \_\_init\_\_ method
- This methods is used to initialize values upon an object creation.
- This method is also known as Constructor

## \_\_str\_\_ method
This method is used when we want to convent a user defined class into a string object.

## \_\_int\_\_ method
This method is used when we want to convent a user defined class into a integer object.

## \_\_len\_\_ methpd
This method is used to get the length of an object.

### **Example:**

```py
class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'The price of {self.name} is ₹{self.price}.'

    def __int__(self):
        return self.price

    def __add__(self, other):
        return self.price + other.price

mango = item('Mango',20)
laptop = item('Laptop',60000)

print(int(mango))
print(str(laptop))

print('The total cost of laptop and mango is :', laptop+mango)
```

Output :

```
20
The price of Laptop is ₹60000.
The total cost of laptop and mango is : 60020
```

### Note: Most of the Dunder Methods will return a value
### Fun fact
- Dunder methods, got it name from the ***D***ouble ***under***scores surrounding their names. 
---

These are just a few of the many magic methods available in Python. They are incredibly powerful tools that allow you to customize the behaviour of your objects, and can make your code much cleaner and easier to understand. So if you’re looking for a way to take your Python code to the next level, take some time to learn about these magic methods.
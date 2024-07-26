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
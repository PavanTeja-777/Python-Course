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
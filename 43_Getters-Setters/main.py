class MyClass:
    def __init__(self, value):
        self.value = value

    @property
    def val(self):
        return self.value

    @val.setter
    def val(self, new_value):
        self.value = new_value

obj = MyClass(10)
obj.val = 20 # Setter
print(obj.val)
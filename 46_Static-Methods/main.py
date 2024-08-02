class Math:

    @staticmethod
    def add(a, b):
        return a + b

m1 = Math()
print(m1.add(2, 3)) # Output: 3
print(Math.add(2, 3)) # Output: 3
# The Walrus Operator
- The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression.
- This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
- The Walrus Operator is represented by the `:=` syntax and can be used in a variety of contexts including while loops and if statements.

Here's an example of using the Walrus Operator in an if statement:
```py
usernames = ["ABC", "XYZ", "123"]

if (name := input("Enter a name: ")) in usernames:
    print(f"Hello, {name}!")
    login(name) # Assume this logins the username
else:
    print("Username not found.")
```
In this example, 
- the user input is assigned to the variable `name` using the Walrus Operator.
- The value of `name` is then used in the if statement to determine whether it is in the names list and trying to login.
- If it is, the corresponding message is printed, otherwise, a different message is printed.

Here is another example 
```py
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
```
## Note:
It is important to note that the Walrus Operator should be used sparingly as it can make code less readable if overused.

In conclusion, the Walrus Operator is a useful tool for Python developers to have in their toolkit. It can help streamline code and reduce duplication, but it should be used with care to ensure code readability and maintainability.
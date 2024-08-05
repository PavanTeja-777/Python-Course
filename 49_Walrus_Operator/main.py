usernames = ["ABC", "XYZ", "123"]

if (name := input("Enter a name: ")) in usernames:
    print(f"Hello, {name}!")
    login(name) # Assume this logins the username
else:
    print("Username not found.")

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

print(foods)
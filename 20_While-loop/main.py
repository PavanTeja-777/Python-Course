# While Loop

count = 5
while (count > 0):
    print(count)
    count = count - 1

# Do while Loop

sum = 0
while True:
    number = int(input("Enter numbers to sum (Enter Zero to exit): "))
    
    if number == 0:
        break

    sum += number
    print(f'The number {number} is added\n')

print(f'The sum is {sum}')
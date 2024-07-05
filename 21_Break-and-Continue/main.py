# Break
counter = 0
while True:

    if counter == 6: break
    
    print(f'Counter value is {counter}')

    counter += 1

# Countinue
for i in range(1,11):

    if i % 2 != 0:
        continue

    print(i)
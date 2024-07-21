#just to open a file
f = open('filename.txt')

#to close a file
f.close()

# To read from a file
with open('test.txt', 'r') as f:
    text = f.read()
    print(text)

# To write in a file
with open('test.txt', 'w') as f:
    f.write('I am written by a Py code')

# To append to a file
with open('test.txt', 'a') as f:
    f.write('I am appended by a Py code')

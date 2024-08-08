import os

# Get a list of the files in the current directory
files = os.listdir('.')
print(files)

# Create a new directory
os.mkdir('newdir')

output = os.system('ls')
print(output)


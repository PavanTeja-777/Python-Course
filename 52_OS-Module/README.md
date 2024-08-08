# OS Module

- The os module in Python is a built-in library that provides functions for interacting with the operating system.
- It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

Here are some common tasks you can perform with the os module:

## Interacting with the file system

The os module also provides functions for interacting with the file system. For example, you can use the `os.listdir` function to get a list of the files in a directory:

```py
import os

files = os.listdir('.')
print(files)
```

You can also use the `os.mkdir` function to create a new directory:

```py
import os

os.mkdir('newdir')
```

## Running system commands

Finally, the os module provides functions for running system commands. For example, you can use the `os.system` function to run a command and get the output:

```py
import os

output = os.system('ls')
print(output)
```

## Some cool things with os module

```py
import os

while 1:
    os.system('color 40')
    os.system('color 20')
    os.system('color 10')
```

Try to execute the code in your Device.(_Flash Warning_)

## Conclusion

- These are the some of the popular fuynction in, os module, has variety diffrent function which deals with Operating System operations

- In summary, the os module in Python is a built-in library that provides a wide variety of functions for interacting with the operating system.

- It allows you to perform tasks such as reading and writing files, interacting with the file system, and running system commands.

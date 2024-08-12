## `if __name__ == "__main__"` Idiom
The `if __name__ == "__main__"` idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

- In Python, the `__name__` variable is a built-in variable that is automatically set to the name of the current module.
- When a Python script is run directly, the `__name__` variable is set to the string `__main__` When the script is imported as a module into another script, the `__name__` variable is set to the name of the module.

Here's an example of how the if `__name__` == `__main__` idiom can be used:

### Assume this code is written in module.py
```py
def main():
    print("Running script directly")

if __name__ == "__main__":
    main() # Prints the code if executed as `python3 module.py`
```
### this code is importing module.py
```py
import module

module.main()
```
## Try without writing if statement in module.py
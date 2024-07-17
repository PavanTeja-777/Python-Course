# Match Case Statements
- Match-case characteristics very similar to if-else functionality, we use a match case in python. In C, C++ or Java like language, we have switch-case statements.

- A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main stages :

1. **Match** keyword
1. One or more **case**
1. **Expression** for each case

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

### Syntax:
```py
match var_to_be_matched:
    case 'pattern_1':
        # statement 1
        ...
    case 'pattern_2':
        # statement 2
        ...
    

    case 'pattern_n':
        # statement n
        ...
    case _:
        # Default Case
        ...
```

### A program to understand Match Case better:

```py
x = int(input())

match x:
    case 1: #Executes if the value of x is 1
        print("If we want to match with certain value")

    case 1: #To demonstrate, if any case matched it breaks from match unlike in other lang
        print("In Python if a case is matched it automatically\
               breaks from match after executing case block")

    case _ if (x > 2 and x < 10): # Executes if x matches the condition
        print("If we have any condition")

    case _: # If any case doesn't match then this block will execute
        print("It's Default case.")
```

**Output 1**:
```
1
If we want to match with certain value
```

**Output 2**:
```
5
If we have any condition
```

**Output 3**:
```
10
It's Default case.
```

### Note: Match cases were added in Python 3.10 version onwards
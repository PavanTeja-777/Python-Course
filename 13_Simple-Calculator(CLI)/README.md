# Calculator - CLI Based
- A Calculator program is a basic program in all kind of languages 
- By doing a basic Calculator program we can familiar with the operator, output and input statemets

Code :

```py
n1 = int(input("Enter the value of n1: "))
n2 = int(input("Enter the value of n2: "))

print("The Result of of n1 + n2 is:  ",n1+n2)
print("The Result of of n1 - n2 is:  ",n1-n2)
print("The Result of of n1 * n2 is:  ",n1*n2)
print("The Result of of n1 / n2 is:  ",n1/n2)
print("The Result of of n1 // n2 is: ",n1//n2)
print("The Result of of n1 % n2 is:  ",n1%n2)
print("The Result of of n1 ** n2 is: ",n1**n2)

# ------------------(or)----------------------

print(eval(input("Enter a Expression: ")))
```

Output:
```
Enter the value of n1: 14
Enter the value of n2: 3
The Result of of n1 + n2 is:   17
The Result of of n1 - n2 is:   11
The Result of of n1 * n2 is:   42
The Result of of n1 / n2 is:   4.666666666666667
The Result of of n1 // n2 is:  4
The Result of of n1 % n2 is:   2
The Result of of n1 ** n2 is:  2744
Enter a Expression: ((13*4)+(2**12))/(2**5)
129.625
```

**Fun Fact: eval() is a best function when we have an equation to be solved**

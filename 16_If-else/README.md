# Conditional Statements
- Till now we have seen the code which is flowing from top to bottom with left to right 
- If we want some of our code based on a condition it can be done with Conditional Statements
- Before seeing Conditional Statements we see some operators which are helpful

## Comparison & Logical Operators

### **Comparison Operators**
- We use Comparison operators between 2 variables to a result in Boolean i.e. True or False
- The comparsion Operators in Python are ```>,>=,<,<=,==,!=```  
For example visit [main.py](/16_If-else/main.py)

### **Logical Operators**
- We use Logical operators mostly between Booleans and the result is in Boolean i.e. True or False
- The Logical Operators in Python are ```and, or, not```  
For example visit [main.py](/16_If-else/main.py)

<br>
<br>

There are three types of Conditional Statements

1. **If**
2. **If-else**
3. **If-elif-else**

## If

If we have a one condition to execute a block of code then we have to use a code sample like this

```py
havingSkills = True
if havingSkills:
    print('You may get a good package!')
```
Output:  
```
You may get a good package!
```

You might be wondering why we have gave space for print statement.  
In Python we don't use ```{``` ```}``` for creating a block,  
instead we use colon (:) to tell interpreter that a block is starting
and we will give a Indentation (Deafult 4 white spaces or One Tab) to create a block.

The above code in other language may look like
```c
bool havingSkills = true;
if (havingSkills){
    printf("You may get a good package!");
}
```

## If-else

If we have a one condition to execute a block of code and another block of code if the condition fails then we have to use a code sample like this
```py
havingSkills = False
if havingSkills:
    print('You may get a good package!')

else:
    print('Make projects to get skills!')
```
Output:  
```
Make projects to get skills!
```

## If-elif-else

If we have a multiple condition to execute a multiple block of code and another block of code if the condition fails then we have to use a code sample like this

- In simple if we have many conditions for different blocks then we use elif followed with if
```py
havingSkills = False
havingMarks = True

if havingSkills:
    print('You may get a good package!')

elif havingMarks:
    print('Having only marks is not enough. Get skills!')

else:
    print('Make projects to get skills! and learn Concepts')
```
Output:  
```
Having only marks is not enough. Get skills!
```

# Note
- elif and else are not mandatory
- Make sure Indentation is correct

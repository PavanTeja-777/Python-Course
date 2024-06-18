# Type Conversion
- Converting from one Datatype to another is called as Type Conversion

Suppose we have 2 numbers in a string format like below and when we want to add those numbers we get output as below 

```py
a, b = "10", "11"
print(a + b)
```
Output :
```
1011
```

If we the ouput as addition of integers then we need to Type cast them into int like
```py
a, b = "10", "11"
a, b = int(a), int(b)
print(a + b)
```
Output :
```
21
```

Not only for int, we have every type casting function for every data type
```py
int()    # Any datatype into int
str()    # Any datatype into str
float()  # Any datatype into float
bool()   # Any datatype into bool
list()   # Any datatype into list
tuple()  # Any datatype into tuple
set()    # Any datatype into set
dict()   # Any datatype into dict
```
### Note: This function only converts if there is any chance of conversion otherwise they throw error

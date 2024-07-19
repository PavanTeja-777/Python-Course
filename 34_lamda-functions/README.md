# Lambda Functions
In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

```py
lambda arguments: expression
```
Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce ; we will see in later post.

Here is an example of how to use a lambda function:

```py
# Function to calculate the product of two numbers
def multiply(x, y):
  return x * y

# Lambda function to calculate the product of two numbers
lambda x, y: x * y
```
Lambda functions can also include multiple statements, but they are limited to a single expression. For example:

### Example
```py
mul = lambda x, y: x*y

print(f'The Multiplication of 3.26 & 5.68: {mul(3.26,5.68)}')
```
Output :
```
The Multiplication of 3.26 & 5.68: 18.516799999999996
```
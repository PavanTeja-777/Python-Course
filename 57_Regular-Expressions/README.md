# Regular Expressions
- Regular expressions, or 'regex' for short, are a powerful tool for working with strings and text data in Python.
- They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.
## Metacharacters in regular expressions
```
[] - Represent a character class
^  - Matches the beginning
$  - Matches the end
.  - Matches any character except newline
?  - Matches zero or one occurrence.
|  - Means OR (Matches with any of the characters separated by it.)
*  - Any number of occurrences (including 0 occurrences)
+  - One or more occurrences
{} - Indicate number of occurrences of a preceding RE to match.
() - Enclose a group of REs
```
Find list of more meta characters [Click Here](http://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions).

## Importing re Package
In Python, regular expressions are supported by the `re` module. The basic syntax for working with regular expressions in Python is as follows:

```py
import re
```

## re.search()
- `re.search()` method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string.
- This method stops after the first match, so this is best suited for testing a regular expression more than extracting data.
- We can use `re.search()` method like this to search for a pattern in regular expression:
```py
import re

# Define a regular expression pattern (Prefix string with r)
pattern = r'world'
text = 'Hello, world!'

match = re.search(pattern, text)

if match: print('Match found!')
else: print('Match not found.')
```

## re.findall()
You can also use the `re.findall()` function to find all occurrences of the pattern in a string:

```py
import re

text = 'The email address1 is example1@example.com, \
        The email address2 is example2@example.com,\
        The email address3 is example3@example.com,'

pattern = r'\w+@\w+\.\w+'

match = re.findall(pattern, text)
print(match)
# ['example1@example.com', 'example2@example.com', 'example3@example.com']
```

## Replacing a pattern
The following example shows how to replace a pattern in a string:
```py
import re

pattern = r'[a-z]+at'
text = 'The cat is hidden under hat.'

new_text = re.sub(pattern, 'dog', text)
print(new_text) # The dog is hidden under dog.
```
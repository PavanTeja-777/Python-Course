import re

# Searching a pattern in a string
pattern = r'world'
text = 'Hello, world!'

match = re.search(pattern, text)

print(match)
if match: print('Match found!')
else: print('Match not found.')

print('*'*30)

# Replacing a pattern
pattern = r'[a-z]+at'
text = 'The cat is hidden under hat.'

new_text = re.sub(pattern, 'dog', text)
print(new_text) # The dog is hidden under dog.

print('*'*30)

# Extracting Information
text = 'The email address1 is example1@example.com, \
        The email address2 is example2@example.com,\
        The email address3 is example3@example.com,'

pattern = r'\w+@\w+\.\w+'

match = re.findall(pattern, text)
print(match) 
# ['example1@example.com', 'example2@example.com', 'example3@example.com']
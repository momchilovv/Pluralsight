# Extract an email address out of a text file
import re

with open('info.txt', 'r') as file:
    content = file.read()

pattern = r'\S+@\S+\.\S+'

result = re.search(pattern, content)

print(result.group())
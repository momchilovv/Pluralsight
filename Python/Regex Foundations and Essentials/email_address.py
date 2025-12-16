# Extract an email address out of a text file
import re

with open('info.txt', 'r') as file:
    content = file.read()

result = re.search(r'\S+@\S+\.\S+', content)

print(result.group())
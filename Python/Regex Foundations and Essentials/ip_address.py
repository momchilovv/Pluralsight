# Find the IP address inside the text file
import re

with open('info.txt', 'r') as file:
    content = file.read()

pattern = r'\b(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])' \
            r'(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}\b'

result = re.search(pattern, content)

print(result.group())
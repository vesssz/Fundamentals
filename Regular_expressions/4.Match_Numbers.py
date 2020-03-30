import re

text = input()
regex = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(regex, text)

for match in matches:
    print(match.group(0), end=" ")

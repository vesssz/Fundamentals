import re

regex = r"\d+"

test_str = input()
while True:
    if not test_str:
        break
    matches = re.findall(regex, test_str)
    for match in matches:
        print(match, end=" ")
    test_str = input()

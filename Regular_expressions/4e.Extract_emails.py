import re
text = input()

pattern = r"( |^)[a-z0-9]+([\.\-_][a-z0-9]+)*@[a-z]+(-[a-z]+)*(\.[a-z]+(-[a-z]+)*)+"
matches = re.finditer(pattern, text)
for match in matches:
    mail = match[0].strip()
    print(mail)
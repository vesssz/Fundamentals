import re

text = input()
pattern = r"(www\.)([a-zA-Z0-9]+(-[a-zA-z0-9]+)*)(\.[a-z]+)+"
while text != "":
    matches = re.finditer(pattern, text)

    for match in matches:
        mail = match[0].strip()
        print(mail)
    text = input()



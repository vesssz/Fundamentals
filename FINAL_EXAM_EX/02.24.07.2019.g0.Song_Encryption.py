def key_define(letter, number):
    key = ord(letter) + number
    if letter.islower():
        if key > 122:
            key -= 26
    if letter.isupper():
        if key > 90:
            key -= 26
    return chr(key)

import re
pattern = r"^[A-Z][a-z']+[ ]*[a-z']+:[A-Z ]+$"

data = input()
while data != "end":
    match = re.findall(pattern, data)
    if len(match) != 0:
        line = "".join(match[0])
        key_data = line.split(":")
        key = len(key_data[0])
        encrypted = ""
        for item in line:
            if item == "'":
                encrypted += item
            elif item == " ":
                encrypted += item
            elif item == ":":
                encrypted += "@"
            else:
                encrypted += key_define(item, key)
        print(f"Successful encryption: {encrypted}")
    else:
        print("Invalid input!")


    data = input()
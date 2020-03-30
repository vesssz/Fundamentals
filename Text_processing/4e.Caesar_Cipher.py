text = input()
newtext = ""
for i in text:
    newtext += chr(ord(i) + 3)
print(newtext)
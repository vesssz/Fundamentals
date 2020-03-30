string = input()
newstring = ""
newstring += string[0]
for i in string:
    if newstring[-1] != i:
        newstring += i
print(newstring)
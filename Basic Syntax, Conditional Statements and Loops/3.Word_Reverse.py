word = input()
newword = ""
for i in range(len(word) -1, -1, -1):
    newword += word[i]
print(newword)
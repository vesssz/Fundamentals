

crypto_message = input().split()
decrypted = []
new_message = []
number = ""
for word in crypto_message:
    word = list(word)
    for element in word:
        if element.isdigit():
            number += element

    decrypted.append(chr(int(number)))
    number = ""
    for element in word:
        if not element.isdigit():
            decrypted.append(element)
    decrypted[-1], decrypted[1] = decrypted[1], decrypted[-1]
    new_message.append("".join(decrypted))
    decrypted = []

print(" ".join(new_message))

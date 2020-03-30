def letter_position(letter):
    if letter.isupper():
        position = ord(letter) - 64
    elif letter.islower():
        position = ord(letter) - 96
    return position


strings = input().split()
temp_sum = 0
for item in strings:
    first_letter = item[0]
    last_letter = item[-1]
    number = int(item[1:-1])
    if first_letter.isupper():
        temp_sum += number/letter_position(first_letter)

    elif first_letter.islower():
        temp_sum += number * letter_position(first_letter)

    if last_letter.islower():
        temp_sum += letter_position(last_letter)
    elif last_letter.isupper():
        temp_sum -= letter_position(last_letter)
print(f"{temp_sum:.2f}")

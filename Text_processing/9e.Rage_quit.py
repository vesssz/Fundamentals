original_message = input()

multiply_number = 1

symbols = ""
rage_message = ""
for i in range(len(original_message)):

    if not original_message[i].isdigit():
        symbols += original_message[i]


    else:
        multiply_number = int(original_message[i])
        if i + 1 < len(original_message) and original_message[i + 1].isdigit():
            multiply_number = int(str(multiply_number) + original_message[i + 1])
        rage_message += (symbols * multiply_number).upper()
        multiply_number = 1
        symbols = ""
uniquesymbols = set(rage_message)

print(f"Unique symbols used: {len(uniquesymbols)}")
print(rage_message)

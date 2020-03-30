data = input()
power = 0
i = 0
while i < len(data):
    for symbol in data:
        if symbol == ">":
            power += int(data[i + 1])
        elif power > 0:
            data = data[:i] + data[i + 1:]
            power -= 1
            i -= 1
        i += 1
print(data)

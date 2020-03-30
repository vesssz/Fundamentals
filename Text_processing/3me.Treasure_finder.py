key_sequence = "".join(input().split())
data = input()
newdata = ""


def decipher(message):
    data = message.split("&")
    treasure = data[1]
    data2 = data[-1]
    start_index = data2.index("<")
    end_index = data2.index(">")
    coordinates = data2[start_index + 1:end_index]

    result = {treasure: coordinates}
    return result


counter = 0

while data != "find":
    for i in data:
        key = int(key_sequence[counter])
        newdata += chr(ord(i) - key)
        counter += 1
        if counter == len(key_sequence):
            counter = 0
    for k, v in decipher(newdata).items():
        print(f"Found {k} at {v}")

    newdata = ""
    counter = 0
    data = input()

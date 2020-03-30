username = input()
line = input().split(" ")
while line[0] != "Sign":
    command = line[0]
    if command == "Case":
        type_command = line[1]
        if type_command == "lower":
            username = username.lower()
            print(username)
        elif type_command == "upper":
            username = username.upper()
            print(username)
    elif command == "Reverse":
        start = int(line[1])
        stop = int(line[2])
        if not start > (len(username) - 1) or not stop > (len(username) - 1) or not start >= start:
            substring = username[start: stop + 1]
            print(substring[::-1])

    elif command == "Cut":
        substring = line[1]
        if substring in username:
            username = username.replace(substring, "", -1)
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif command == "Replace":
        char = line[1]
        username = username.replace(char, "*", -1)
        print(username)
    elif command == "Check":
        char = line[1]
        if char not in username:
            print(f"Your username must contain {char}.")
        else:
            print("Valid")

    line = input().split(" ")

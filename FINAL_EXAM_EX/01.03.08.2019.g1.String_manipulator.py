message = input()
data = input()
while data != "End":
    args = data.split(" ")
    command = args[0]
    if command == "Translate":
        old = args[1]
        new = args[2]
        message = message.replace(old, new, -1)
        print(message)
    elif command == "Includes":
        substring = args[1]
        print(substring in message)
    elif command == "Start":
        startstring = args[1]
        long = len(startstring)
        print(message[:long] == startstring)

    elif command == "Lowercase":
        message = message.lower()
        print(message)
    elif command == "FindIndex":
        char = args[1]
        index = message.rfind(char)
        print(index)

    elif command == "Remove":
        start = int(args[1])
        stop = start + int(args[2])
        message = message[:start] + message[stop:]
        print(message)
    data = input()

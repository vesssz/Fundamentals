message = input()
command_line = input().split(" ")
while command_line[0] != "Done":
    command = command_line[0]
    if command == "Change":
        old_char = command_line[1]
        new_char = command_line[2]
        if old_char in message:
            message = message.replace(old_char, new_char, -1)
            print(message)
    elif command == "Includes":
        char = command_line[1]
        print(char in message)
    elif command == "End":
        char = command_line[1]
        len_char = len(char)
        print(message[-len_char:] == char)

    elif command == "Uppercase":
        message = message.upper()
        print(message)
    elif command == "FindIndex":
        char = command_line[1]
        index_char = message.index(char)
        print(index_char)
    elif command == "Cut":
        start = int(command_line[1])
        stop = start + int(command_line[2])
        message = message[start:stop]
        print(message)
    command_line = input().split(" ")
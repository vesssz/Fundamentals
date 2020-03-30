message = input()
line = input().split(" ")
while line[0] != "Finish":
    command = line[0]
    if command == "Replace":
        current_char = line[1]
        new_char = line[2]
        message = message.replace(current_char,new_char, -1)
        print(message)
    elif command == "Cut":
        start_index = int(line[1])
        end_index = int(line[2])
        if start_index > len(message)-1 or end_index > len(message)-1 or start_index < 0 or end_index < 0:
            print("Invalid indexes!")
        else:
            message = message[:start_index] + message[end_index+1:]
            print(message)

    elif command == "Make":
        type_action = line[1]
        if type_action == "Upper":
            message = message.upper()
        else:
            message = message.lower()
        print(message)
    elif command == "Check":
        substring = line[1]
        if substring in message:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")
    elif command == "Sum":
        start_index = int(line[1])
        end_index = int(line[2])
        if start_index > len(message)-1 or end_index > len(message)-1 or start_index < 0 or end_index < 0:
            print("Invalid indexes!")
        else:
            sum = 0
            message_sub = message[start_index:end_index +1]
            for i in message_sub:
                sum += ord(i)
            print(sum)

    line = input().split(" ")
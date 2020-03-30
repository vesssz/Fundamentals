email = input()
command_line = input()
while command_line != "Complete":
    command_line = command_line.split(" ")
    command = command_line[0]
    if command == "Make":
        type_action = command_line[1]
        if type_action == "Upper":
            email = email.upper()
            print(email)
        elif type_action == "Lower":
            email = email.lower()
            print(email)
    elif command == "GetDomain":
        count = int(command_line[1])
        print(email[-count:])
    elif command == "GetUsername":
        if "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            index = email.index("@")
            print(email[:index])
    elif command == "Replace":
        old_char = command_line[1]
        email = email.replace(old_char, "-", -1)
        print(email)
    elif command == "Encrypt":
        for character in email:
            print(ord(character), end=" ")

    command_line = input()
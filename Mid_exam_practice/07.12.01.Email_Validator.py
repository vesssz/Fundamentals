email = input()
line = input().split()

while line[0] != "Complete":
    command = line[0]

    if command == "Make":
        if line[1] == "Upper":
            email = email.upper()
            print(email)
        elif line[1] == "Lower":
            email = email.lower()
            print(email)

    elif command == "GetDomain":
        count_char = int(line[1])
        print(email[-count_char:])

    elif command == "GetUsername":
        if "@" in email:
            username = ""
            for i in email:
                if i != "@":
                    username += i
                if i == "@":
                    break

            print(username)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif command == "Replace":
        char = line[1]
        if char in email:
            new_mail = ""
            for i in email:
                if i == char:
                    new_mail += "-"
                else:
                    new_mail += i
            print(new_mail)
            email = new_mail

    elif command == "Encrypt":
        encrypted = [ord(i) for i in email]
        encrypted = (map(lambda x: str(x), encrypted))
        print(" ".join(encrypted))

    line = input().split()

line_input = input()
data = {}
while line_input != "Statistics":
    line = line_input.split("->")
    command = line[0]
    username = line[1]
    if command == "Add":
        if username not in data.keys():
            data[username] = []
        else:
            print(f"{username} is already registered")
    elif command == "Send":
        email = line[2]
        data[username].append(email)
    elif command == "Delete":
        if username in data.keys():
            del data[username]
        else:
            print(f"{username} not found!")

    line_input = input()

data = dict(sorted(data.items(), key=lambda u: (-len(u[1]), u[0])))
print(f"Users count: {len(data)}")
for k, v in data.items():
    print(k)
    for item in v:
        print(f"- {item}")


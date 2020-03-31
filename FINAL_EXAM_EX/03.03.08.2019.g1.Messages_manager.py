capacity = int(input())
data = input()
users = {}
while data != "Statistics":  #Send :received
    args = data.split("=")
    command = args[0]
    if command == "Add":
        username = args[1]
        sent = int(args[2])
        received = int(args[3])
        if username not in users.keys():
            users[username] = [sent, received]
    elif command == "Message":
        sender = args[1]
        receiver = args[2]
        if sender in users.keys() and receiver in users.keys():
            users[sender][0] += 1
            users[receiver][1] += 1
            if sum(users[sender]) >= capacity:
                print(f"{sender} reached the capacity!")
                del users[sender]
            if sum(users[receiver]) >= capacity:
                print(f"{receiver} reached the capacity!")
                del users[receiver]
    elif command == "Empty":
        username = args[1]
        if username == "All":
            users.clear()
        else:
            if username in users.keys():
                del users[username]

    data = input()

users = dict(sorted(users.items(), key=lambda x:(-x[1][1], x[0])))

print(f"Users count: {len(users)}")
for k, v in users.items():
    print(f"{k} - {sum(v)}")
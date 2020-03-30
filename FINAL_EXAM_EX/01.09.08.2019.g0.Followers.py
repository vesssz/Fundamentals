line = input()
all_users = {}
while line != "Log out":
    data = line.split(":")
    command = data[0]
    username = data[1]
    if command == "New follower":
        if username not in all_users.keys():
            all_users[username] = 0

    elif command == "Like":
        count = int(data[2])
        all_users.setdefault(username, 0)
        all_users[username] += count
    elif command == "Comment":
        if username not in all_users.keys():
            all_users[username] = 1
        else:
            all_users[username] += 1
    elif command == "Blocked":
        if username not in all_users.keys():
            print(f"{username} doesn't exist.")
        else:
            del all_users[username]
    line = input()

all_users = dict(sorted(all_users.items(), key=lambda x: (-x[1], x[0])))
print(f"{len(all_users)} followers")
for k, v in all_users.items():
    print(f"{k}: {v}")

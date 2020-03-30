


initial_friends = input().split(", ")
line = input().split()

while line[0] != "Report":
    command = line[0]

    if command == "Blacklist":
        name = line[1]
        if name not in initial_friends:
            print(f"{name} was not found.")
        else:
            index = initial_friends.index(name)
            initial_friends[index] = "Blacklisted"
            print(f"{name} was blacklisted.")
    elif command == "Error":
        index = int(line[1])
        if initial_friends[index] == "Blacklisted" or initial_friends[index] == "Lost":
            pass
        else:
            print(f"{initial_friends[index]} was lost due to an error.")
            initial_friends[index] = "Lost"

    elif command == "Change":
        index = int(line[1])
        new_name = line[2]

        if 0<= index < len(initial_friends):
            print(f"{initial_friends[index]} changed his username to {new_name}.")
            initial_friends[index] = new_name

    line = input().split()

blacklist = initial_friends.count("Blacklisted")
lost = initial_friends.count("Lost")
print(f"Blacklisted names: {blacklist}")
print(f"Lost names: {lost}")
for name in initial_friends:
    print(name, end=" ")

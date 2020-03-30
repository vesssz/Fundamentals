targets = list(map(lambda x: int(x), input().split("|")))
coins = 0
while True:
    string = input()
    if string == "Reverse":
        targets.reverse()
        continue
    elif string == "Game over":
        print(f"{targets[0]} - {targets[1]} - {targets[2]} - {targets[3]} - {targets[4]}")
        print(f"Iskren finished the archery tournament with {coins} points!")
        break

    command = string.split("@")
    start = int(command[1])
    if start < 0:
        start = start + len(targets)
    stop = int(command[2])
    if len(targets) - 1 < start:
        continue
    if command[0] == "Shoot Right":
        index = start + stop
        while index >= len(targets):
            index -= len(targets)
        if targets[index] >= 5:
            targets[index] -= 5
            coins += 5
    elif command[0] == "Shoot Left":
        index = start - stop
        while abs(index) >= len(targets):
            index += len(targets)
        if targets[index] >= 5:
            targets[index] -= 5
            coins += 5
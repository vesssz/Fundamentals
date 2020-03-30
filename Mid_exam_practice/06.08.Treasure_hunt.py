initial_loot = input().split("|")
line = input().split()

while line[0] != "Yohoho!":
    command = line[0]

    if command == "Loot":
        treasures = line[1::]
        for treasure in treasures:
            if treasure not in initial_loot:
                initial_loot.insert(0, treasure)

    elif command == "Drop":
        index = int(line[1])
        if index <= len(initial_loot) - 1:
            current_loot = initial_loot[index]
            initial_loot.remove(current_loot)
            initial_loot.append(current_loot)

    elif command == "Steal":
        stolen_items = []
        stolen_count = int(line[1])
        if stolen_count > len(initial_loot):
            stolen_count = len(initial_loot)
        for _ in range(stolen_count):
            stolen_items.insert(0, (initial_loot[-1]))
            initial_loot.pop()
        print(", ".join(stolen_items))

    line = input().split()

if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    counter = 0
    for item in initial_loot:
        for symbol in item:
            counter += 1
    average = counter / len(initial_loot)
    print(f"Average treasure gain: {average:.2f} pirate credits.")

items = input().split(", ")
line = input().split(" - ")

while line[0] != "Craft!":
    command = line[0]
    if command == "Collect":
        item = line[1]
        if item not in items:
            items.append(item)

    elif command == "Drop":
        item = line[1]
        if item in items:
            items.remove(item)

    elif command == "Combine Items":
        item_line = line[1].split(":")
        old_item = item_line[0]
        new_item = item_line[1]
        if old_item in items:
            index = items.index(old_item) + 1
            items.insert(index, new_item)
    elif command == "Renew":
        item = line[1]
        if item in items:
            items.append(item)
            items.remove(item)

    line = input().split(" - ")

print(", ".join(items))

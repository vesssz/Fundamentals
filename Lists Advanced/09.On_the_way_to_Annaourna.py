

shops = []
items = []
command = input()
notes = []
while command != "End":
    temp_list = []
    command = command.split("->")
    shop = command[1]
    items = command[2]
    if command[0] == "Add":
        items = items.split(",")
        if shop in shops:
            index_ = shops.index(shop)
            for item in items:
                items.insert(item)



    elif command[0] == "Remove":
        pass
    command = input()
print(notes)

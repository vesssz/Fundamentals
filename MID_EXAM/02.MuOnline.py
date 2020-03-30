health = 100
bitcoins = 0
went_all_rooms = True
dungeon_rooms = input().split("|")

for best_room in range(len(dungeon_rooms)):
    room = dungeon_rooms[best_room].split()
    command = room[0]

    if command == "potion":
        number = int(room[-1])
        if health == 100:
            number = 0
        else:
            health = health + number
            if health + number > 100:
                number = number - (health - 100)
                health = 100

        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        number = int(room[-1])
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        number = int(room[-1])
        health -= number
        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room + 1}")
            went_all_rooms = False
        else:
            print(f"You slayed {command}.")

    if not went_all_rooms:
        break

if went_all_rooms:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

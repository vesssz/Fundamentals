health = 100
total_coins = 0
rooms = input().split("|")
game_over = False
last_room = 0
for room in rooms:
    last_room += 1
    tokens = room.split(" ")
    command = tokens[0]

    if command == "potion":
        recover = int(tokens[1])
        health += recover
        if health == 100:
            pass
        elif health < 100:
            pass
        elif health > 100:
            recover = recover - (health - 100)
            health = 100
        print(f"You healed for {recover} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        coins = int(tokens[1])
        total_coins += coins
        print(f"You found {coins} bitcoins.")
    elif command != "potion" and command != "chest":
        monster = tokens[0]
        damage = int(tokens[1])
        health -= damage
        if health <= 0:
            game_over = True
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {last_room}")
            break
        else:
            print(f"You slayed {monster}.")

if not game_over:
    print("You've made it!")
    print(f"Bitcoins: {total_coins}")
    print(f"Health: {health}")

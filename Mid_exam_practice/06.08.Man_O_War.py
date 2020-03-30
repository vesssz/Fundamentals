pirate_ship = input().split(">")
pirate_ship = list(map(lambda x: int(x), pirate_ship))
war_ship = input().split(">")
war_ship = list(map(lambda x: int(x), war_ship))
max_health = int(input())
line = input().split()
game_over = False


def index_is_valid(index, my_list):
    return 0 <= index < len(my_list)


while line[0] != "Retire":
    command = line[0]

    if command == "Fire":
        index = int(line[1])
        damage = int(line[2])
        if index_is_valid(index, war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                game_over = True
                break

    elif command == "Defend":
        start_index = int(line[1])
        end_index = int(line[2])
        damage = int(line[3])
        if index_is_valid(start_index, pirate_ship) and index_is_valid(end_index, pirate_ship):
            for i in range(len(pirate_ship)):
                if start_index <= i <= end_index:
                    pirate_ship[i] -= damage
                    if pirate_ship[i] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        game_over = True
                        break
                    #BREAK!!!

    elif command == "Repair":
        index = int(line[1])
        health = int(line[2])
        if index_is_valid(index, pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health
    elif command == "Status":
        status_count = 0
        for i in pirate_ship:
            if i < max_health * 0.2:
                status_count += 1
        print(f"{status_count} sections need repair.")

    line = input().split()

if not game_over:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
line = input()
players = {}
while line != "Results":
    args = line.split(":")
    command = args[0]
    if command == "Add":
        name = args[1]
        health = int(args[2])
        energy = int(args[3])
        if name in players.keys():
            players[name][0] += health
        else:
            players[name] = [health, energy]
    elif command == "Attack":
        attacker = args[1]
        defender = args[2]
        damage = int(args[3])
        if attacker in players.keys() and defender in players.keys():
            players[defender][0] -= damage
            if players[defender][0] <= 0:
                del players[defender]
                print(f"{defender} was disqualified!")
            players[attacker][1] -= 1
            if players[attacker][1] <= 0:
                del players[attacker]
                print(f"{attacker} was disqualified!")
    elif command == "Delete":
        username = args[1]
        if username == "All":
            players.clear()
        else:
            if username in players.keys():
                del players[username]
    line = input()

players = dict(sorted(players.items(),key=lambda x: ((-x[1][0]), x[0])))
print(f"People count: {len(players)}")
for k,v in players.items():
    print(f"{k} - {v[0]} - {v[1]}")
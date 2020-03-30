line_input = input()
liked_meals = {}
unliked_meals = 0
while line_input != "Stop":
    line = line_input.split("-")
    command = line[0]
    guest = line[1]
    meal = line[2]
    if command == "Like":
        liked_meals.setdefault(guest, [])
        if meal not in liked_meals[guest]:
            liked_meals[guest].append(meal)

    elif command == "Unlike":
        if guest not in liked_meals.keys():
            print(f"{guest} is not at the party.")
        else:
            if meal not in liked_meals[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{guest} doesn't like the {meal}.")
                liked_meals[guest].remove(meal)
                unliked_meals += 1


    line_input = input()
liked_meals = dict(sorted(liked_meals.items(), key=lambda u: (-len(u[1]), u[0])))
for user, meal_list in liked_meals.items():
    print(f"{user}: {', '.join(meal_list)}")
print(f"Unliked meals: {unliked_meals}")
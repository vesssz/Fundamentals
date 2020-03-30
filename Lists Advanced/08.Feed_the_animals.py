from collections import Counter
data1 = input()
animals = []
food_allow = []
places = []
while data1 != "Last Info":

    data = data1.split(":")
    command = data[0]
    name = data[1]
    value = int(data[2])
    aria = data[3]

    if command == "Add":
        if name not in animals:
            animals.append(name)
            food_allow.append(int(value))
            places.append(aria)
        else:
            index = animals.index(name)
            food_allow[index] += value
    if command == "Feed":
        if name in animals:
            index = animals.index(name)
            food_allow[index] -= value
            if food_allow[index] <= 0:
                print(f"{name} was successfully fed")
                places.remove(aria)
                food_allow.pop(index)
                animals.pop(index)
    data1 = input()

print("Animals:")

animals = sorted(list(zip(food_allow, animals)), reverse=True)
animals = list(zip(*animals))
i = 0

while i <= len(animals[0])-1:
    print(f"{animals[1][i]} -> {animals[0][i]}g")
    i += 1

print("Areas with hungry animals:")
places = sorted(places, key=Counter(places).get, reverse=True)
for place in places:
    index_ = places.count(place)
    if index_ > 1:
        places.remove(place)
    print(f"{place} : {index_}")

n = int(input())
for _ in range(n):
    line = input()

    start_index = line.index("@")
    stop_index = line.index("|")
    name = line[start_index + 1:stop_index]

    start_index_age = line.index("#")
    stop_index_age = line.index("*")
    age = line[start_index_age + 1: stop_index_age]
    print(f"{name} is {age} years old.")
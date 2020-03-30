names = input().split(", ")
code = input()
clean_code = ""
name = ""
dist = 0
data = {}
while code != "end of race":
    for char in code:
        if char.isalnum():
            clean_code += char
    for i in clean_code:
        if i.isdigit():
            dist += int(i)
        else:
            name += i
    if name in names:
        data.setdefault(name, 0)
        data[name] += dist

    code = input()
    clean_code = ""
    name = ""
    dist = 0

data = dict(sorted(data.items(),key=lambda x: -x[1]))

while len(data)>= 4:
    data.popitem()
data_list = [key for key in data.keys()]
print(f"1st place: {data_list[0]}")
print(f"2nd place: {data_list[1]}")
print(f"3rd place: {data_list[2]}")
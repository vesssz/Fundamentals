import re

def key(line):
    key = 0
    letters = ["s", "t", "a", "r", "S", "T", "A", "R"]
    for char in line:
        if char in letters:
            key += 1
    return key


def alter_line(line, key):
    new_line = ""
    for char in line:
        new_line += chr(ord(char) - key)
    return new_line


n = int(input())
attacked = []
destroyed = []
pattern = r"\@\S*([A-Z][a-z]+)\S*\:\D*(\d+)\D*\!\S*([A,D])\S*\!\S*[\->]\D(\d+)"
for i in range(n):
    line = input()
    key_code = key(line)
    message = alter_line(line, key_code)
    matches = re.findall(pattern, message)
    if len(matches) != 1:
        continue
    planet = matches[0][0]
    action = matches[0][2]

    if action == "A":
        attacked.append(planet)
    else:
        destroyed.append(planet)

attacked = sorted(attacked)
destroyed = sorted(destroyed)
print(f"Attacked planets: {len(attacked)}")
if len(attacked) > 0:
    for planet in attacked:
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed)}")
if len(destroyed) > 0:
    for planet in destroyed:
        print(f"-> {planet}")
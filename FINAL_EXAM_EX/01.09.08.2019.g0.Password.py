import re
n = int(input())
for _ in range(n):
    password = input()
    match = re.findall(r"(\S+)\>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})\<\1", password)
    if len(match) != 1:
        print("Try another password!")
    else:
        print(f"Password: {''.join(match[0][1:])}")

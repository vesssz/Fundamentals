import re
n = int(input())
count_valid = 0
for _ in range(n):
    data = input()
    match = re.findall(r"U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}\d+)P@\$", data)
    if len(match) != 1:
        print("Invalid username or password")
    else:
        username = match[0][0]
        password = match[0][1]
        print("Registration was successful")
        print(f"Username: {username}, Password: {password}")
        count_valid += 1
print(f"Successful registrations: {count_valid}")
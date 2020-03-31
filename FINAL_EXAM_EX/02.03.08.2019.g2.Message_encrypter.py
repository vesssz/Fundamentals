import re
n = int(input())
pattern = r"([\*|@])([A-z][a-z]{2,})\1\:[ ]\[([A-Za-z0-9]\]\|\[[A-Za-z0-9]\]\|\[[A-Za-z0-9])\]\|$"
for _ in range(n):
    message = input()
    match = re.findall(pattern, message)
    if len(match) == 1:
        matches = list(match[0])
        command = matches[1]
        message = matches[2].split("]|[")
        message = [str(ord(i)) for i in message]
        print(f"{command}: {' '.join(message)}")
    else:
        print("Valid message not found!")
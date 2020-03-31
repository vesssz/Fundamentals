import re
n = int(input())
pattern = r"^(\%|\$)([A-Z][a-z]{2,})\1:[ ]\[([0-9]+\]\|\[[0-9]+\]\|\[[0-9]+)\]\|$"
for _ in range(n):
    message = input()
    match = re.findall(pattern, message)
    if len(match) != 0:
        result = match[0]
        command = result[1]
        numbers = result[2].split("]|[")
        output_message = [chr(int(i)) for i in numbers]
        output_message = "".join(output_message)
        print(f'{command}: {output_message}')
    else:
        print("Valid message not found!")
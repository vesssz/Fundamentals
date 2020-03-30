import re
line = input()
total = 0
pattern = r"\%(?P<name>[A-Z][a-z]+)\%\S*\<(?P<product>[A-Z]\w+)\>\S*\|(?P<quantity>\d+)\|\D*(?P<price>\d+\.*\d+)\$"
while line != "end of shift":
    match = re.findall(pattern, line)
    if len(match) == 1:
        name = match[0][0]
        product = match[0][1]
        quantity = int(match[0][2])
        price = float(match[0][3])
        print(f'{name}: {product} - {(quantity* price):.2f}')
        total += quantity * price
    line = input()
print(f"Total income: {total:.2f}")
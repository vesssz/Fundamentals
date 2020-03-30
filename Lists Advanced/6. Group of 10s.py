ages = (list(map(lambda x: int(x), input().split(", "))))

boundary = 10
while len(ages) != 0:
    newages = [age for age in ages if age <= boundary]

    print(f"Group of {boundary}'s: {newages}")
    boundary += 10
    ages = [age for age in ages if age not in newages]


num = int(input())
stars = 1

while num > stars:
    print("*" * stars)
    stars += 1
while stars != 0:
    print("*" * stars)
    stars -= 1

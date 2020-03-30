n = float(input())
tpe = None
if n == 0:
    print("zero")
else:
    if n > 0:
        tpe = "positive"

    elif n < 0:
        tpe = "negative"
if abs(n) <= 1:
    print("small", tpe)
elif abs(n) > 100000:
    print("large", tpe)
else:
    print(tpe)

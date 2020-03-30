a = "ILIKESHEREN"
start = 1
stop = 4
count = 0
new = (a[start:stop + 1])
for i in new:
    count += ord(i)
    print(count)
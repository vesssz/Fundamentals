y = int(input())


def number_unique(n):
    old_num = n
    a = []
    while n != 0:
        d = n % 10
        if d in a:
            break
        else:
            a.append(d)
            n = n // 10
    if len(a) == 4:
        number = str(a[3]) + str(a[2]) + str(a[1]) + str(a[0])
        print(int(number))
        return

    else:
        n = old_num + 1
        list.clear(a)
        number_unique(n)


number_unique(y)

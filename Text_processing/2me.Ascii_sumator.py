first_symbol = ord(input())
last_symbol = ord(input())
string_line = input()
sum = 0
for i in string_line:
    if first_symbol < ord(i) < last_symbol:
        sum += ord(i)
print(sum)
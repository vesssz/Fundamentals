data = input().split(" ")
sum = 0
word1 = data[0]
word2 = data[1]
min_len = min(len(word1), len(word2))
longest_word = word1
if len(word2) > len(word1):
    longest_word = word2
for i in range(min_len):
    sum += ord(word1[i]) * ord(word2[i])
for n in range(min_len, len(longest_word)):
    sum += ord(longest_word[n])
print(sum)







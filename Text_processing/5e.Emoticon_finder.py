text = input()
for i in range(len(text)):
    if i + 1 < len(text) and text[i] == ":":
        print(f":" + text[i + 1])
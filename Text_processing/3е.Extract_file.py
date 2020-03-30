data = input().split('\\')
args = data[-1].split(".")
print(f"File name: {args[-2]}")
print(f"File extension: {args[-1]}")
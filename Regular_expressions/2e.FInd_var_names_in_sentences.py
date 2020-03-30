import re
text = input()
result = []
regex = r"\b(_)([a-zA-Z0-9]+)\b"
matches = re.findall(regex, text)
for match in matches:
    result.append(match[1])
print(",".join(result))
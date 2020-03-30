import re
text = input()
regex = r"\b(?P<day>\d\d)([.\-/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
matches = re.finditer(regex, text)

for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")
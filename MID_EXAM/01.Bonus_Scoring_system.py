import math
students = int(input())
lectures = int(input())
additional_bonus = int(input())
best_bonus = 0
best_attendances = 0
for student in range(students):
    attendances = int(input())

    bonus = attendances / lectures * (5 + additional_bonus)
    if bonus >= best_bonus:
        best_bonus = bonus
        best_attendances = attendances
print(f"Max Bonus: {math.ceil(best_bonus)}.")
print(f"The student has attended {best_attendances} lectures.")
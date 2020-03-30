experience_needed = float(input())
battles = int(input())
collected_exp = 0

for battle in range(1, battles + 1):
    current_exp = int(input())
    collected_exp += current_exp

    if battle % 3 == 0:
        collected_exp += current_exp * 0.15
    if battle % 5 == 0:
        collected_exp -= current_exp * 0.1
    if collected_exp >= experience_needed:
        break
if collected_exp >= experience_needed:
    print(f"Player successfully collected his needed experience for {battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {(experience_needed - collected_exp):.2f} more needed.")

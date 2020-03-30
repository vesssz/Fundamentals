days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
collected_plunder = 0

for day in range(1, days + 1):
    collected_plunder += daily_plunder
    if day %3 == 0:
        collected_plunder += daily_plunder * 0.5
    if day % 5 == 0:  #elif?
        collected_plunder -= collected_plunder * 0.3

if collected_plunder >= expected_plunder:
    print(f"Ahoy! {collected_plunder:.2f} plunder gained.")
else:
    percentage = collected_plunder/expected_plunder*100
    print(f"Collected only {percentage:.2f}% of the plunder.")


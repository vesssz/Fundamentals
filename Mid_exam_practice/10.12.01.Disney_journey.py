journey_cost = float(input())
months = int(input())
collected_money = 0

for month in range(1, months + 1):

    if month % 2 != 0 and month != 1:
        collected_money -= 0.16 * collected_money
    if month == 4:
        collected_money += collected_money * 0.25
    collected_money += journey_cost * 0.25

if collected_money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {(collected_money - journey_cost):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {(journey_cost - collected_money):.2f}lv. more.")
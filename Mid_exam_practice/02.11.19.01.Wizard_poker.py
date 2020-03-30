cards = input().split(":")
line = input().split()
new_cards = []

while line[0] != "Ready":
    command = line[0]
    if command == "Add":
        card = line[1]
        if card in cards:
            cards.remove(card)
            new_cards.append(card)
        else:
            print("Card not found.")
    elif command == "Insert":
        card = line[1]
        index = int(line[2])
        if card in cards and 0<= index <len(new_cards):
            new_cards.insert(index, card)
            cards.remove(card)
        else:
            print("Error!")

    elif command == "Remove":
        card = line[1]
        if card in new_cards:
            new_cards.remove(card)
            cards.append(card)
        else:
            print("Card not found.")
    elif command == "Swap":
        card1 = line[1]
        card2 = line[2]
        index1 = new_cards.index(card1)
        index2 = new_cards.index(card2)
        new_cards[index1], new_cards[index2] = new_cards[index2], new_cards[index1]
    elif command == "Shuffle":
        new_cards = new_cards[::-1]

    line = input().split()
print(" ".join(new_cards))
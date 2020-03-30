all_tickets = input()
all_tickets = ''.join(all_tickets.split())
all_tickets = all_tickets.split(",")
all_special_symbols = ["@", "#", "$", "^"]


def check_if_special_symbol(ticket):
    all_special_symbols = ["@", "#", "$", "^"]
    result = False
    for i in ticket:
        if i in all_special_symbols:
            result = True
    return result


def continuous_symbols(ticket_part):
    counter = 1
    biggest_count = 0
    special_symbol = ticket_part[0]
    for i in range(10):
        if i + 1 < len(ticket_part):
            if special_symbol == ticket_part[i + 1]:
                counter += 1

            else:
                special_symbol = ticket_part[i + 1]
                counter = 1
        if biggest_count <= counter:
            biggest_count = counter
    return biggest_count


def special_symbol(ticket_part):
    for i in ticket_part:
        if ticket_part.count(i) >= 6:
            special_symbol = i
            break
    return special_symbol


for ticket in all_tickets:

    if len(ticket) != 20:
        print("invalid ticket")
        continue
    if not check_if_special_symbol(ticket):
        print(f'ticket "{ticket}" - no match')

    elif len(set(ticket)) == 1:
        print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')

    else:
        first_part = ticket[:10]
        second_part = ticket[10:]
        winning_symbol_count = continuous_symbols(first_part)
        if continuous_symbols(second_part) > continuous_symbols(first_part):
            winning_symbol_count = continuous_symbols(second_part)
        if continuous_symbols(first_part) >= 6 and continuous_symbols(second_part) >= 6:

        print(f'ticket "{ticket}" - {winning_symbol_count}{special_symbol(first_part)}')

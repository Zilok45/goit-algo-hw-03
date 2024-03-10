import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1 or max >= 1000:
        return []
    elif quantity <= 0 or min >= max:
        return []
    elif min <= quantity <= max:
        set_number_ticket = set()
        while len(set_number_ticket) < quantity:
            set_number_ticket.add(random.randint(min, max))
        list_number_ticket = list(set_number_ticket)
        list_number_ticket.sort()
        return list_number_ticket
    else:
        return []


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

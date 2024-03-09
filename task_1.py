from datetime import datetime


def get_days_from_today(date: str) -> int:
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    today_date = datetime.today()
    date_difference = today_date - date_obj
    days_difference = date_difference.days

    if days_difference == 1:
        print(f"Різниця у днях: {days_difference} дeнь")
    elif 1 < days_difference <= 4:
        print(f"Різниця у днях: {days_difference} дні")
    else:
        print(f"Різниця у днях: {days_difference} днів")

    return days_difference


get_days_from_today("2024-03-09")

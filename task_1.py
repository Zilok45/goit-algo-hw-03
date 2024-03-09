from datetime import datetime


def get_days_from_today(date: str) -> int:
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    today_date = datetime.today()
    date_difference = today_date - date_obj
    days_difference = date_difference.days
    print(f"Різниця у днях: {days_difference} днів")
    return days_difference


get_days_from_today("2025-01-09")

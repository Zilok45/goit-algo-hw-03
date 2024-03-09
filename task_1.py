from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
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
    except ValueError:
        print("Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'.")


get_days_from_today("2022-12-24")

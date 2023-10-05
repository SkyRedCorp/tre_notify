import datetime

today = datetime.date.today()

target_dates = {
    1: datetime.date(today.year, 1, 27),
    2: datetime.date(today.year, 2, 28),
    3: datetime.date(today.year, 3, 28),
    4: datetime.date(today.year, 4, 28),
    5: datetime.date(today.year, 5, 26),
    6: datetime.date(today.year, 6, 28),
    7: datetime.date(today.year, 7, 28),
    8: datetime.date(today.year, 8, 28),
    9: datetime.date(today.year, 9, 28), 
    10: datetime.date(today.year, 10, 27),
    11: datetime.date(today.year, 11, 28),
    12: datetime.date(today.year, 12, 28),
}

def check_date():
    current_month = today.month
    try:
        target_date = target_dates[current_month]
        days_remaining = (target_date - today).days
        print("Hoy pagan!" if days_remaining == 0 else f"Faltan: {days_remaining} dias para que paguen.")
    except KeyError:
        print(f"No target date defined for {current_month}.")

check_date()

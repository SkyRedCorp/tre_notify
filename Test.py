import datetime

def check_date():
    today = datetime.date.today()
    target_dates = {
        1: 27,
        2: 28,
        3: 28,
        4: 28,
        5: 26,
        6: 28,
        7: 28,
        8: 28,
        9: 28, 
        10: 27,
        11: 28,
        12: 28,
        # Format: M - D
    }

    current_month = today.month

    if current_month in target_dates:
        target_day = target_dates[current_month]
        target_date = datetime.date(today.year, current_month, target_day)

        if today == target_date:
            print("Hoy pagan!")
        else:
            def days_until_pay():
                return (target_date - today).days
            
            days_remaining = days_until_pay()
            print(f"Faltan: {days_remaining} días para que paguen.")
    else:
        print(f"No target date defined for {current_month}.")

check_date()

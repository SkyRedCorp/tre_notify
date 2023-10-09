# SPDX-FileCopyrightText: © 2023 Peter Tacon <contacto@petertacon.com>
# Original code made by: Santiago Paipilla
# Optimized by: Juan Francisco Hamon
# SPDX-License-Identifier: MIT

import rtc
import time

clock = rtc.RTC()

t = clock.datetime

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print("The date is {} {}/{}/{}".format(days[int(t.tm_wday)], t.tm_mday, t.tm_mon, t.tm_year))
print("The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))


today = (t.tm_mday, t.tm_mon, t.tm_year)

target_dates = {
    1: [27, 1, t.tm_year],
    2: [28, 2, t.tm_year],
    3: [28, 3, t.tm_year],
    4: [28, 4, t.tm_year],
    5: [26, 5, t.tm_year],
    6: [28, 6, t.tm_year],
    7: [28, 7, t.tm_year],
    8: [28, 8, t.tm_year],
    9: [28, 9, t.tm_year],
    10: [27, 10, t.tm_year],
    11: [28, 11, t.tm_year],
    12: [28, 12, t.tm_year]
}

def check_date():
    current_month = today[1]
    try:
        target_date = target_dates[current_month]
        days_remaining = target_date[0] - int(today[0])
        print("Hoy Pagan!" if days_remaining == 0 else f"faltan: {days_remaining} dias para que paguen.")
    except KeyError:
        print(f"Error al calcular dias en {current_month}.")

check_date()

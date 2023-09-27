import rtc
import time

timeclock =rtc.RTC()

def clock_int(i):
	timeclock =rtc.RTC()
	l_clk = list(timeclock.datetime)
	i_clk = []
	for element in l_clk:
		i_clk.append(int(element))
	return(i_clk[i])

year = clock_int(0)
month = clock_int(1)
day = clock_int(2)

#print(type(month_day()))

if day == 26 and month == 9:
	print("One day to pay!")
elif day == 29 and month == 10:
	print("31 days for pay!")
else:
	print("error")


from datetime import datetime

def counter(NOW = datetime.now()):
	HNY = datetime(int(NOW.year)+1,1,1,00,00) - NOW
	return str(HNY.days) + days(HNY.days) + str(HNY.seconds//3600) + hours(HNY.seconds//3600) + str(HNY.seconds//60%60) + minuts(HNY.seconds//60%60)

def days(day):
	if (day%10 == 1) and not (day==11) :
		return " день "
	elif (2 <= day%10 <= 4) and not (12<=day<=14) :
		return " дня "
	else :
		return " дней "

def hours(hour):
	if (hour == 1) or (hour == 21):
		return " час "
	elif (2 <= hour <= 4) or (22 <= hour <=24):
		return " часа "
	elif (hour == 0) or (5 <= hour <= 20):
		return " часов "

def minuts(minute):
	if (minute%10 == 1) and not (minute==11) :
		return " минута "
	elif (2 <= minute%10 <= 4) and not (12<=minute<=14):
		return " минуты "
	else :
		return " минут "




if __name__ ==  '__main__' :
	print(counter(datetime(2018,12,18,2,13,5)))
	print(counter(datetime(2007,9,1,23,59,0)))
	print(counter(datetime(1800,2,1,15,0,2)))
	print(counter(datetime(2000,5,9,0,0,0)))

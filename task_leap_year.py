year = int(input())
if (year%100==0) and (year%400!=0):
	print('no')
elif (year%4!=0):
	print('no')
else:
	print('yes')
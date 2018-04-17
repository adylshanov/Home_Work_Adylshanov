plates = int(input())
soap = int(input())
while (plates > 0)and(soap >0):
	plates -=1
	soap -= 0.5
if (plates == 0) and (soap == 0):
	print("Все тарелки вымыты, моющее средство закончилось")
elif (soap > 0):
	print('Все тарелки вымыты. Осталось',soap,'ед. моющего средства')
elif (plates > 0):
	print('Моющее средство закончилось. Осталось',plates,'тарелок')
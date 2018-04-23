def bubble_sort(lst):
	for i in range(len(lst)):
		for j in range(i+1, len(lst),1):
			if (lst[i]>lst[j]):
				lst[i],lst[j] = lst[j],lst[i]
	return lst

"""
def bubble_sort(lst):
	for i in range(len(lst)): делаем проход по списку от 1 по последнего. текущий элемент i
		for j in range(i+1, len(lst),1):   делаем проход чисел от i+1 по последнего. 
			if (lst[i]>lst[j]): производим сравнение. Если элемент i больше элемента j, то они меняются местами.
				lst[i],lst[j] = lst[j],lst[i]
	return lst

mas = [14,8,3,1,89,2,45]
mas2 = [0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45]
print(mas2)
print(bubble_sort(mas2))
"""
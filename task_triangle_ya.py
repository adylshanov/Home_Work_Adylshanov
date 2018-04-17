x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

A2 = (x2-x1)**2 + (y2-y1)**2 
B2 = (x3-x1)**2 + (y3-y1)**2 
C2 = (x2-x3)**2 + (y2-y3)**2 

if (A2 == B2 + C2) or (B2 == A2 + C2) or (C2 == A2 + B2):
	print("yes")
else:
	print("no")
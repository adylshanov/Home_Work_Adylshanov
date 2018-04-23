def encode(str, ROT=0):
	return (code(str,ROT))

def decode(str, ROT=0):
	return (code(str,-1*ROT))

def code(str, ROT):
	str1=''
	for i in range(len(str)):
		if str[i].isalpha() == True:
			str1 += chr(ord(str[i])+ROT)
			#print()
		else: 
			str1 += str[i]
	return str1

"""
test1 = "Hello, Python3"
ROT1 = 1
print(test1)
print(encode(test1,ROT1))
test1 = encode(test1,ROT1)
print(decode(test1,ROT1))
"""
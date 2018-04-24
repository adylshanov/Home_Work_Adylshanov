def encode(str, ROT=0):
	return (code(str,ROT))

def decode(str, ROT=0):
	return (code(str,-1*ROT))

def code(str, ROT):
	outstr = ''
	for i in range(len(str)):
		if str[i].isalpha() == True:
			if (str[i].isupper() == True):
				outstr += change(str[i],ROT,65,90)
			else:
				outstr += change(str[i],ROT,97,122)
		else: 
			outstr += str[i]
	return outstr

def change(ch,ROT,begin,end):
	ROT = ROT % 26
	if ((ord(ch) + ROT) > end):
		return chr(ord(ch) + ROT - 26)
		
	elif (ROT < 0) and ((ord(ch) - ROT) < begin):
		return chr(ord(ch) - ROT + 26)
		
	else:
		return chr(ord(ch) + ROT)


if __name__ == '__main__':
	test1 = "Hello, Python3!"
	test2 = "Gur pyrnare naq avpre gur cebtenz, gur snfgre vg'f tbvat gb eha. Naq vs vg qbrfa'g, vg'yy or rnfl gb znxr vg snfg."
	test3 = "There is no programming language, no matter how structured, that will prevent programmers from making bad programs."
	ROT1 = 1
	ROT2 = 13
	ROT3 = 25
	print(encode(test1,ROT1))
	print(decode(test2,ROT2))
	print(encode(test3,ROT3))
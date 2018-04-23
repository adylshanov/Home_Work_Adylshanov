def is_palindrome(s):
	t = (',. !?') 				#символы для отбрасывания если проверяется строка
	s = str(s)    				#если проверям число, то переводим в текст
	for i in range(len(t)):
		s = s.replace(t[i],'')
	if (s[::-1].lower() == s.lower()):
		return True
	else :
		return False
'''
test1=int(input())
print(is_palindrome(test1))
'''
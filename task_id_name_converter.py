def camel_to_shake(name):
	for i in range(len(name)-1,1,-1):
		if (name[i].isupper() == True):
			name = name[0:i] +'_'+ name[i:]
	return name.lower()


def snake_to_camel(name):
	words = name.split('_')
	for i in range(len(words)):
		words[i] = words[i].title()
	return ''.join(words)


test1 = "CamelRase"
test2 = "getUserId"
test3 = "snake_case"
test4 = "set_ripository"

print(camel_to_shake(test1))
print(camel_to_shake(test2))

print(snake_to_camel(test3))
print(snake_to_camel(test4))

string = 'Geeks'
obj = iter(string)

count = 5
while count>0:
	item = next(obj)
	print(item)
	count -=1

try:
	print(a)
except:
	print("a not defined!")


a = 100

try:
	print(a)
except NameError:
	print("a not defined!")
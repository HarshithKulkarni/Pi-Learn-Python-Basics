# def simpleGeneratorFun():
# 	yield 1			
# 	yield 2			
# 	yield 3			

# # Driver code to check above generator function
# for value in simpleGeneratorFun():
# 	print(value)


def ourRange(n,end=0):

	if(end != 0):
		while(n < end):
			
			yield n
			n += 1
	else:
		cnt = 0
		while(cnt < n):
			yield cnt
			cnt += 1


for j in ourRange(2,8):
	print(j)


print("\n")



for i in ourRange(5):
	print(i)
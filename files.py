# Reading a file #
file = open('geek.txt', 'r')

for each in file:
	print (each)

file.close()

# Writing to a file #

file = open('geek.txt','w')
file.write("This is the write command\n")
file.write("It allows us to write in a particular file\n")
file.close()


#Appending to a file #
file = open('geek.txt','a')
file.write("We are appending to geek.txt\n")
file.write("This is appended text\n")
file.close()


# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
	f.write("Hello World!!!\n")

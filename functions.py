def add(a,b):  # a -> 5, b -> 6    This function adds two numbers
    return a + b


a = int(input("Enter A : ")) # convert user input to integer because by default it is accepted as a STRING
b = int(input("Enter B : ")) # convert user input to integer because by default it is accepted as a STRING

addition = add(a,b)

print(addition)

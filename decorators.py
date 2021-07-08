# # Function inside function ##
# def create_adder(x): 
#     def adder(y): 
#         return x+y 
  
#     return adder 
  
# add_15 = create_adder(15) 
  
# print(a_15(10)) 

##############################


def hello_decorator(func):
  
    def inner1():
        print("Hello, this is before function execution")
  
        func()
  
        print("This is after function execution")
          
    return inner1
  

@hello_decorator
def function_to_be_used():
    print("This is inside the function !!")
  
  
# function_to_be_used = hello_decorator(function_to_be_used)
  
  
# # calling the function
# function_to_be_used()


function_to_be_used()
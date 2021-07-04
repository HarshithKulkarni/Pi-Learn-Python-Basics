class Test:
    def __init__(self, a, b):
        pass
  
    def __repr__(self):
        return "from __repr__ Hello World"
  
    def __str__(self):
        return "from __str__ Hello World"
  
# Driver Code        
t = Test(1234, 5678)
print(t)
print([t])
print([t][0])
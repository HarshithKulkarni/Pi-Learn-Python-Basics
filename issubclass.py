class Base(object):
    pass   # Empty Class
  
class Derived(Base):
    pass   # Empty Class
  
# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))
  
dog = Derived()
bag = Base()
  
# b is not an instance of Derived
print(isinstance(bag, Derived))
  
# But d is an instance of Base
print(isinstance(dog, Base))

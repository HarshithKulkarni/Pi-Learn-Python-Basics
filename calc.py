class Calculator:
    
    def __init__(this,a,b):
        this.a = a
        this.b = b

    def add(this):

        return sum([this.a,this.b])

    def sub(this):
        
        return abs(this.a-this.b)

    def multiply(this):

        return this.a * this.b

    def div(this):

        return this.a / this.b

    def __repr__(this):
        return "This is a Calculator"

if __name__ == '__main__':

    new_obj = Calculator(65,45)
    print(f"Multiplied value : {new_obj.multiply()}")

if __name__ == 'calc':
    print("Im in main block of calc")   
    calc_1 = Calculator(5,5)
    print(f"Added Value : {calc_1.add()}")
class Calculator:
    def square (self):
        print(f"The Square of {self} is {self**2}")
    
    def cube (self):
        print(f"The cube of {self} is {self**3}")

    def sqrt (self):
        print(f"The Square of {self} is {self**(1/2)}")

Calculator.square(3)
Calculator.cube(3)
Calculator.sqrt(3)
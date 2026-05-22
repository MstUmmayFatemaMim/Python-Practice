#########   5. Car class //Create a Car with brand, model, year. Add a method age()
##########that returns how old the car is. Add a __str__ method for pretty printing.

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def age(self):
        print(f"Car Age: {self.year}")
        return self.year
    def __str__(self):
        print(f"Car Name: {self.brand}")
        print(f"Car Model: {self.model}")
        return self.brand,self.model

x=Car("Toyato","Model 3",2020)
x.age()
x.__str__()

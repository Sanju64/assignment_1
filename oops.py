class car:  
    def __init__(self,modelname, year,type):  
        self.modelname = modelname  
        self.year = year  
        self.type = type
    def display(self):  
        print(self.modelname,self.year,self.type)  
        
  
c1 = car("Toyota", 2016,"Diesel")
c2 = car("TATA",2021,"Petrol")
c3 = car("Maruti",2018,"Petrol")
c1.display()
c2.display()
c3.display()



# Python3 program introducing f-string

val = 'Sanju'
print(f"{val} for {val} is a portal for {val}.")

val2 = "Palace"
val3 = "Goa"

print(f"The Best {val2} in the World is In {val3}")

name = 'Mark'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

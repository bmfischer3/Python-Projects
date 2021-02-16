
# Practice found here: http://introtopython.org/classes.html


class TeslaCar(object):
    def __init__(self):
        self.CarSpeed = 0
        self.BatteryLife = 0
        self.Color = ''
        self.Mileage = 0
    def move_forward(self):
        self.CarSpeed += 11
    def move_backward(self):
        self.CarSpeed -= 7

# The above gives TeslaCar the ability to store information. This does not actually create the Tesla Car yet. 

class TeslaModelX(object):
    def __init__(self):
        self.FlyDoors = "Yes"
        self.CarSpeed = 0

RedTesla = TeslaCar()
print(RedTesla)

# Creates the variable RedTesla. RedTesla has been set to the TeslaCar class and Python creates an object from the TeslaCar class. 
# The class has a copy of each of the variables listed in TeslaCar
# RedTesla can do any action that is defined for the class. 

RedTesla = TeslaCar()
print("My Tesla is going: ", RedTesla.CarSpeed)

RedTesla.move_forward()
print("My Tesla is going: ", RedTesla.CarSpeed)

RedTesla.move_backward()
print("My Tesla is going: ", RedTesla.CarSpeed)

# To acces the object's variables or methods, name the object  and use the dot notation to acccess the variable/method.
#  

RedTesla = TeslaModelX()
print(RedTesla)

RedTesla = TeslaModelX()
print("My Tesla Model X, does it have fly doors? ", RedTesla.FlyDoors)

# References the TeslaModelX class. Dot notation used to reference the MyTeslaCar class will render invalid. 



my_teslas = []
for x in range (0,5):
    my_teslas.append(TeslaCar())

# Creates a fleet of 5 teslas and stores them in a list that references MyTeslaCar Class
# The line my_teslas.append(TeslaCar()) is executed 5 times.
# Each time, a new teslacar object is created and added to the my_teslas list
# The __init__() method is executed once for each of these objects, so each object gets its own x andy value
# each object can be worked with individually 

for TeslaCar in my_teslas:
    print(TeslaCar)

# Shows each rocket is a separate object




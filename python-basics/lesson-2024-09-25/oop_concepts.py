# Class

class Vehicle:
    # Class attributes
    bmw = 'It is one of the most popular car brands.'
    mercedes = 'It is another luxary car brand.'

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print('This is init method and I am always called at the time of object creation.')
        print(self.stop())
    
    # def initial(self, brand, model):
    #     self.brand = brand
    #     self.model = model
    #     return f'I am driving {self.brand} {self.model}.'


    # Instance methods
    def start(self, key, horn):
        self.key = key
        self.horn = horn
        accelerate = True
        return f'Start the engine with {self.key}. Check the horn level {self.horn}.'
    
    def drive(self):
        speed = 120
        return f'Drive the car using {self.key}.'
    
    def stop(self):
        brake = True
        return 'Stop the car.'
    
    def fuel(self):
        tank_low = True
        return f'Re-fill the tank and make a sound at {self.horn} dB.'
    

# vehicle_1 = Vehicle()
# vehicle_2 = Vehicle()

vehicle_1 = Vehicle('BMW', 'X11')
# vehicle_2 = Vehicle('Tesla', 'Model 3')

# print(vehicle_1) # <__main__.Vehicle object at 0x7a82fb357e50>
# print(vehicle_1.bmw) # It is one of the most popular car brands.

# print(Vehicle.bmw) # It is one of the most popular car brands.

# print(Vehicle.speed) # AttributeError: type object 'Vehicle' has no attribute 'speed'

# print(vehicle_1.start()) # Start the engine.

# print(vehicle_1.drive()) # Drive the car.

# print(vehicle_1.fuel()) # Re-fill the tank.


# print(vehicle_1.start('remote key', 20)) # Start the engine with remote key. Check the horn level 20.

# print(vehicle_1.drive()) # Drive the car using remote key.

# print(vehicle_1.fuel()) # Re-fill the tank and make a sound at 20 dB.

# print(vehicle_1.initial('BMW', 'X6')) # I am driving BMW X6.
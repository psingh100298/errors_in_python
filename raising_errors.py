class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def add_car(self,car):
        raise NotImplementedError("We can't add cars to the garage yet.." )

ford = Garage()
ford.add_car('Fiesta')
print(len(ford))


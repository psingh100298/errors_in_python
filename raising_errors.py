class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def add_car(self,car):
        print("This method is a work in progress..")

ford = Garage()
ford.add_car('Fiesta')
print(len(ford))


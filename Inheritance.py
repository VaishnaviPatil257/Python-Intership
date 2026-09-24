class vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("i am a vehicle")
        print("mileage of vehicle is",self.mileage)
        print("cost of vehicle is",self.cost)
v1=vehicle(500,500)
v1.show_details()
class car(vehicle):
    def show_car(self):
        print("i am a car")
c1=car(200,1200)
c1.show_details()
c1.show_car()
class car(vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("i am a car")
        print("number of tyres are",self.tyres)
        print("values of horse power is",self.hp)
c1=car(20,12000,4,300)
c1.show_details()
c1.show_car_details()


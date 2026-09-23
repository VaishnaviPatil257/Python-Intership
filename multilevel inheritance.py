class ElectricCar(Car):
    def __init__(self,brand,moodel,year,base_price_per_day,seats,battery_kwh):
        super().__init__(brand,model,year,base_price_per_day,seats)
        self.battery_kwh=battery_kwh
    def rental_cost(self,days):
        cost=super().rental_cost(days)
        return cost - (5*days)
    def display_info(self):
        super().display_info()
        print(f"Battery:{self.battery_kwh} kwh | Eco-discount applied")
        car = ElectricCar("Tesla", "Model 3", 2025, 100, 5, 75)
car.display_info()
days = 4
print(f" Rental cost for {days} days: ₹{car.rental_cost(days)}")

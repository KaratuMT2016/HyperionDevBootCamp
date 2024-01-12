
class Holiday:

    def __init__(self, city_flight, num_nights, rental_days) -> None:
        self.city_flight = city_flight
        self.num_nights = num_nights
        self.rental_days = rental_days

    def __str__(self) -> str:
        return f'''
                City of Flight : {self.city_flight}
                Number of Nights : {self.num_nights}
                Number of Rental Days : {self.rental_days}
            '''
    def get_integer_num_nights(prompt):
        while True:
            try:
                num_nights = int(input(prompt))
                return num_nights
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
    def get_integer_rental_days(prompt):
        while True:
            try:
                rental_days = int(input(prompt))
                return rental_days
            except ValueError:
                print("Invalid input. Please enter a valid integer.")


city_flight_cost = {
    "Argentina": 3111,
    "India": 3912,
    "Japan": 1190,
    "South Africa": 3024,
    "United Kingdom": 6235,
    "United States": 2454,
    "London": 2343,
    "Aberdeen": 4444,
    "Manchester": 2343,
    "Abuja": 2311
}

num_nights = [0,1,2,3,4,5,6,7,8,9,10]

rental_days = [1,2,3,4,5,6,7]

def hotel_cost():
    pass

def plane_cost():
    pass

def car_rental():
    pass


def holiday_cost():
    pass


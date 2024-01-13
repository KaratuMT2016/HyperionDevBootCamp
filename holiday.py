
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
    city_flight_cost = {
            "Argentina": 3111,
            "India": 3912,
            "Japan": 1190,
            "South Africa": 3024,
            "Spain": 6235,
            "Washington DC": 2454,
            "London": 2343,
            "Aberdeen": 4444,
            "Manchester": 2343,
            "Abuja": 2311
        }

    hotel_price_list = {
            "Standar Room": 150,
            "Deluxe Room": 200,
            "Executive Room": 250,
            "Suite": 400,
            "Presidential Suite": 1000,
            "Family Room": 600,
            "Connecting Room": 700,
            "Penthouse Suite": 2000,
            "Accessible Room": 350
        }
     
    car_rental_price_list = {
            "Daily Rental": 50,
            "Weekly Rental": 200,
            "Monthly Rental": 250,
            "Weekend Rental": 400
            
        }

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

    def menu():
        menu_note = """
        This is an exciting time to emback on your journey and we have you covered for the following destinations. 
        Try us and you will be glad you did!

        Please, choose your destination from the following options:
        """
        print(menu_note)
        Holiday.destination_list()
        

    def destination_list():
        # Open the file "cities_to_visit.txt" in read mode using a with statement
        with open("cities_to_visit.txt", "r") as cities:
            # Initialize an empty list to store the cities
            city_list = []

            # Iterate through each line in the file
            for lines in cities:
                # Remove newline characters from the line
                temp = lines.strip('\n')

                # Split the line into words
                temp = temp.split()

                # Join the words into a single string separated by spaces
                joined = " ".join(temp)

                # Append the joined string to the city_list
                city_list.append(joined)

            # Iterate through each city in the list and print it on a separate line
            for city in city_list:
                print(city)
        
    def hotel_cost(self, num_nights):
        total_hotel_stay_cost = 0
        for key, value in Holiday.city_flight_cost.items():
            if key == city_flight:
                total_hotel_stay_cost = num_nights * value
        return total_hotel_stay_cost

    def plane_cost():
        pass

    def car_rental():
        pass


    def holiday_cost():
        pass



Holiday.menu()
city_flight = input("Please, enter your destionation : ").capitalize()
print()
while not city_flight == 'none':

    num_nights = Holiday.get_integer_num_nights("Please, enter the number of nights : ")
    print()

    car_rental_option = input("Do you plan on renting a car (Y/N) : ").upper()

    if car_rental_option == 'Y':
        rental_days = Holiday.get_integer_rental_days("Enter the number of days for your rental : ")
        break

holiday_instance = Holiday(city_flight, num_nights, rental_days)
result = Holiday.hotel_cost(holiday_instance, num_nights)
print(result)
print("Thank you for using our booking system. Goodbye!")
print()

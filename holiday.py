
class Holiday:
     
    def __init__(self, city_flight, hotel_room_type, num_nights, car_rental_type, rental_days) -> None:
        self.city_flight = city_flight
        self.hotel_room_type = hotel_room_type
        self.num_nights = num_nights
        self.car_rental_type = car_rental_type
        self.rental_days = rental_days

    def __str__(self) -> str:
        return f'''
                City of Flight : {self.city_flight}
                Hotel Room Type : {self.hotel_room_type}
                Number of Nights : {self.num_nights}
                Type of Car Rental : {car_rental_type}
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
            "Standard": 150,
            "Deluxe": 200,
            "Executive": 250,
            "Suite": 400,
            "Presidential": 1000,
            "Family": 600,
            "Connecting": 700,
            "Penthouse": 2000,
            "Accessible": 350
        }
     
    car_rental_price_list = {
            "Suv": 150,
            "Coupe": 50,
            "Saloon": 100,
            "Lemousine": 250
            
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

    def room_types_menu():
        room_type_note = """
        To ease your journey and enhance a good experience, we have a variety 
        of hotel reservations for you.

        Please, choose from the list of luxury hotel rooms that fits your budget:
        """
        print(room_type_note)
        Holiday.hotel_room_type_list() 

    def car_rental_menu():
        car_rental_note = """
        To further ease your journey and enhance a good experience, we have a variety 
        of car rental options.

        Please, choose a car rental that fits your budget:
        """
        print(car_rental_note)
        Holiday.car_rental_list()

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

    def hotel_room_type_list():
        # Open the file "cities_to_visit.txt" in read mode using a with statement
        with open("hotel_room_types.txt", "r") as hotel_rooms:
            # Initialize an empty list to store the cities
            hotel_room_list = []

            # Iterate through each line in the file
            for lines in hotel_rooms:
                # Remove newline characters from the line
                temp = lines.strip('\n')

                # Split the line into words
                temp = temp.split()

                # Join the words into a single string separated by spaces
                joined = " ".join(temp)

                # Append the joined string to the city_list
                hotel_room_list.append(joined)

            # Iterate through each city in the list and print it on a separate line
            for room in hotel_room_list:
                print(room)

    def car_rental_list():
        # Open the file "cities_to_visit.txt" in read mode using a with statement
        with open("car_rental_list.txt", "r") as car_rental_types:
            # Initialize an empty list to store the cities
            car_rental_type_list = []

            # Iterate through each line in the file
            for lines in car_rental_types:
                # Remove newline characters from the line
                temp = lines.strip('\n')

                # Split the line into words
                temp = temp.split()

                # Join the words into a single string separated by spaces
                joined = " ".join(temp)

                # Append the joined string to the city_list
                car_rental_type_list.append(joined)

            # Iterate through each city in the list and print it on a separate line
            for car in car_rental_type_list:
                print(car)
        
    def hotel_cost(self, num_nights):
        total_hotel_stay_cost = 0
        for key, value in Holiday.hotel_price_list.items():
            if key == hotel_room_type:
                total_hotel_stay_cost = num_nights * value
        return total_hotel_stay_cost

    def plane_cost(self):
        total_plane_cost = 0
        for key, value in Holiday.city_flight_cost.items():
            if key == city_flight:
                total_plane_cost = value
        return total_plane_cost

    def car_rental(self, rental_days):
        total_rental_cost = 0
        for key, value in Holiday.car_rental_price_list.items():
            if key == car_rental_type:
                total_rental_cost = rental_days * value
        return total_rental_cost


    def holiday_cost():
        holiday_instance = Holiday(city_flight, hotel_room_type, num_nights, car_rental_type, rental_days)
        hotel_cost = Holiday.hotel_cost(holiday_instance, num_nights)
        plane_cost = Holiday.plane_cost(holiday_instance)
        rental_cost = Holiday.car_rental(holiday_instance, rental_days)

        total_holiday_cost = hotel_cost + plane_cost + rental_cost
        print(f""" The cost of your flight to {city_flight} is {plane_cost}, the hotel cost is {hotel_cost}, and your car rental cost is {rental_cost}. Therefore, your total Holiday cost is {total_holiday_cost}
              """)



Holiday.menu()
city_flight = input("Please, enter your destination : ").capitalize()
print()
while not city_flight == 'none':
    
    Holiday.room_types_menu()
    hotel_room_type = input("Please, enter a hotel room type : ").capitalize()

    num_nights = Holiday.get_integer_num_nights("Please, enter the number of nights : ")
    print()

    car_rental_option = input("Do you plan on renting a car (Y/N) : ").upper()

    if car_rental_option == 'Y':
        Holiday.car_rental_menu()
        car_rental_type = input("Please, enter your rental type : ").capitalize()
        rental_days = Holiday.get_integer_rental_days("Enter the number of days for your rental : ")
        break
    else:
        Holiday.holiday_cost()
print("Thank you for using our booking system. Goodbye!")
print()

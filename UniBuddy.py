

# Assuming you have a function to get the current date and time
from datetime import datetime

def menu():
    menu_note = '''
The UniBuddy covers a range of topics that are commonly on the minds 
of new university students like you. My mission is providing clear and 
accessible information about some of your questions in order for you to
have a smoother transition and positive experience on campus.

To start a conversation with UniBuddy, please, enter your details below.

Enter "none" to exit the program.
                '''
    print(menu_note)


def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_age_message(name, age):
    if 16 <= age <= 18:
        return f"Welcome {name}! You're starting your academic journey at an early age of {age}. Enjoy every moment and make the most of your time on campus!"
    elif 19 <= age <= 25:
        return f"Welcome {name}! {age} is a fantastic age to explore new opportunities, make lifelong friends, and delve into your academic interests."
    elif 26 <= age <= 35:
        return f"Welcome {name}! {age} is never too late a age to pursue higher education. Embrace the learning experience and connect with fellow students."
    elif 36 <= age <= 100:
        return f"Welcome {name}! Lifelong learning knows no age limit, not even at {age}. Enjoy the diverse campus life and make the most of your academic pursuits."
    else:
        return f"Welcome {name}! Remember, {age} is just a number. Embrace the learning journey and connect with the vibrant campus community."

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to generate UniBuddy's response about the first lecture
def first_lecture_response():
    current_datetime = get_current_datetime()

    return f'''
             Your first lecture is scheduled for {current_datetime}. 
             The lecture will be in RM101 of the Main Building. 
             Make sure to arrive on time and bring any necessary materials. 
             If you have any more questions or need further assistance, feel free to ask!

             '''

def registration_response():
    return """
    Registering for classes is a crucial step in setting up your academic journey. Here's a step-by-step guide to help you through the process:

    1. **Login to the Student Portal:**
        Visit your university's student portal or online platform. You can usually find a link on the university's official website. Log in using your student credentials.

    2. **Navigate to the Registration Section:**
        Once logged in, look for the "Registration" or "Course Registration" section. This is typically located within the student dashboard or a dedicated registration portal.

    3. **Review Course Offerings:**
        Explore the available courses for the upcoming semester. Check the course catalog or schedule to see which classes are being offered.

    4. **Check Prerequisites:**
        Make sure to review any prerequisites or co-requisites for the courses you are interested in. Some classes may require completion of specific prerequisites.

    5. **Build Your Class Schedule:**
        Select the courses you want to enroll in and create your class schedule. Pay attention to class timings, locations, and any potential time conflicts.

    6. **Add Courses to Your Cart:**
        Add the selected courses to your cart before finalizing your registration.

    7. **Confirm and Submit:**
        Once you've finalized your class schedule, proceed to the registration confirmation page. Review your selected courses, ensure accuracy, and submit your registration.

    8. **Check Registration Status:**
        After submitting your registration, check your registration status to ensure everything went smoothly. Look for any registration holds or pending approvals.

    9. **Get Confirmation:**
        Look out for a confirmation email or notification indicating that your class registration is successful. This confirmation will include details about your enrolled classes.

    If you encounter any difficulties or have specific questions about the registration process, don't hesitate to reach out to your university's registrar's office or academic advisor. They are there to assist you throughout your academic journey.
    """


menu()
while True:
    try:

        user_name = input("Please enter your name : ").capitalize()
        print()
        user_age = get_integer_input("Enter your age: ")
        print()
        age_message = get_age_message(user_name, user_age)
        print(age_message)

        if not user_name.isalpha():
            print("You've not entered a username")

        else:

            print(f"Here are the different clubs and societies in the University colour-coded with red, yellow, blue, green, orange, and white:")
            
        club_response = input("Do you want to explore these clubs or do you want to proceed with your question (Y/N) : ").upper()

        if club_response == "N":

            break

        elif club_response == "Y":
            user_fav_color = input("Please enter your favourite colour : ").capitalize()

            if user_fav_color == "Red":

                print(f'''
                Dear {user_name}, I see {user_fav_color} is your favourite colour.
                Be relaxed we've got exciting activities for the {user_fav_color} club:
                ''')

                print("""
                Red Club: This club is known as the Outdoor Adventure Club.
                Activities in the club include: 
                    - Hiking 
                    - camping 
                    - Rock Climbing 
                    - Outdoor excursions
                For additonal information, please contact the Student Union Building at 10 King Street, AB24 3UE, Aberdeen
                """)
                break

            if user_fav_color == "Yellow":

                print(f'''
                Dear {user_name}, I see {user_fav_color} is your favourite colour.
                Be relaxed we've got exciting activities for the {user_fav_color} society:
                ''')

                print("""
                Yellow Society: This club is known as the Language and Cultural Exchange Society.
                Activities in the society include: 
                    - Language exchange sessions 
                    - Cultural events 
                    - International Food Festivals 
                For additonal information, please contact the Student Union Building at 10 King Street, AB24 3UE, Aberdeen
                """)
                break

            if user_fav_color == "Blue":

                print(f'''
                Dear {user_name}, I see {user_fav_color} is your favourite colour.
                Be relaxed we've got exciting activities for the {user_fav_color} club:
                ''')

                print("""
                Blue Club: This club is known as the Robotics and Engineering Club.
                Activities in the club include: 
                    - Building Robots 
                    - Participating in Engineering Competitions 
                    - Organizing Tech Workshops 
                For additonal information, please contact the Student Union Building at 10 King Street, AB24 3UE, Aberdeen
                """)
                break

            if user_fav_color == "Green":

                print(f'''
                Dear {user_name}, I see {user_fav_color} is your favourite colour.
                Be relaxed we've got exciting activities for the {user_fav_color} Society:
                ''')

                print("""
                Green Society: This club is known as the Environmental Sustainability Society.
                Activities in the club include: 
                    - Tree planting 
                    - Recycling Initiatives 
                    - Educational Events on Environmental Issues 
                For additonal information, please contact the Student Union Building at 10 King Street, AB24 3UE, Aberdeen
                """)
                break

            if user_fav_color == "Orange":

                print(f'''
                Dear {user_name}, I see {user_fav_color} is your favourite colour.
                Be relaxed we've got exciting activities for the {user_fav_color} Society:
                ''')

                print("""
                Green Club: This club is known as the Improv Comedy Club.
                Activities in the club include: 
                    - Improvisational Theater Performances 
                    - Comedy Workshops 
                    - Open Mic Nights 
                For additonal information, please contact the Student Union Building at 10 King Street, AB24 3UE, Aberdeen
                """)
                break

            if user_fav_color == "White":

                print(f'''
                Dear {user_name}, I see {user_fav_color} is your favourite colour.
                Be relaxed we've got exciting activities for the {user_fav_color} Society:
                ''')

                print("""
                White Society: This club is known as the Health and Wellbeing Society.
                Activities in the club include: 
                    - Yoga and Meditation Sessions 
                    - Mental Health Awareness Campaigns 
                    - Wellness Retreats 
                For additonal information, please contact the Student Union Building at 10 King Street, AB24 3UE, Aberdeen
                """)
                break
            else:
        
                print("You have entered a wrong option. Please, Chose \"Y\" for yes or \"N\" for no")


            if not user_fav_color.isalpha():
                print("You've not entered your favourite colour.")
                break

    except ValueError:
        print("You have not entered a number for your age. Please try again")


question_category = open("questionCategory.txt", "r")
question_category_list = [] # This is a list

for lines in question_category:
    
    temp_list = lines.strip('\n')
    temp_list = temp_list.split()

    joined = " ".join(temp_list)
    question_category_list.append(joined)

print("Here are the categories of our Frequently Asked Questions - FAQ : ")

for count, quest in enumerate(question_category_list, start=1):
    print(f"{count}. {quest}")

choice = int(input("Please enter the number of the question category you'd like to ask : "))

while not choice == 0:
    
    if choice == 1:
        response = registration_response()
        print(response)
    choice = int(input("Please enter the number question you'd like to ask : "))


faq_file = open("input.txt", "r")
faq_list = [] # This is a list

for lines in faq_file:
    
    temp = lines.strip('\n')
    temp = temp.split()

    joined = " ".join(temp)
    faq_list.append(joined)


print("Here is a list of our Frequently Asked Questions - FAQ : ")


for count, quest in enumerate(faq_list, start=1):
    print(f"{count}. {quest}")

choice = int(input("Please enter the number question you'd like to ask : "))

while not choice == "none":
    if choice == 1:
        response = registration_response()
        print(response)
    choice = int(input("Please enter the number question you'd like to ask : "))

    if choice == 2:
        
        response = first_lecture_response()
        print(response)
    choice = int(input("Please enter the number question you'd like to ask : "))



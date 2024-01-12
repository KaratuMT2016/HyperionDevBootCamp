

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

    1. Login to the Student Portal:
        Visit your university's student portal or online platform. You can usually find a link on the university's official website. Log in using your student credentials.

    2. Navigate to the Registration Section:
        Once logged in, look for the "Registration" or "Course Registration" section. This is typically located within the student dashboard or a dedicated registration portal.

    3. Review Course Offerings:
        Explore the available courses for the upcoming semester. Check the course catalog or schedule to see which classes are being offered.

    4. Check Prerequisites:
        Make sure to review any prerequisites or co-requisites for the courses you are interested in. Some classes may require completion of specific prerequisites.

    5. Build Your Class Schedule:
        Select the courses you want to enroll in and create your class schedule. Pay attention to class timings, locations, and any potential time conflicts.

    6. Add Courses to Your Cart:
        Add the selected courses to your cart before finalizing your registration.

    7. Confirm and Submit:
        Once you've finalized your class schedule, proceed to the registration confirmation page. Review your selected courses, ensure accuracy, and submit your registration.

    8. Check Registration Status:
        After submitting your registration, check your registration status to ensure everything went smoothly. Look for any registration holds or pending approvals.

    9. Get Confirmation:
        Look out for a confirmation email or notification indicating that your class registration is successful. This confirmation will include details about your enrolled classes.

    If you encounter any difficulties or have specific questions about the registration process, don't hesitate to reach out to your university's registrar's office or academic advisor. They are there to assist you throughout your academic journey.
    """


def find_course_schedule():
    return '''
              Hello! You can easily access the course schedule by visiting our university's official website. Once there, navigate to the "Academics" or "Student Resources" 
              section. You should find a link or tab specifically for "Course Schedule" or "Timetable." Clicking on that link will likely lead you to a page where you can view 
              or download the current course schedule. If you have any trouble finding it, feel free to let me know, and I'll be happy to assist you further!
              '''

def how_to_access_online_learning_platform():
    return '''
              Certainly! To access our online learning platforms, follow these steps:

            1. Login to Student Portal:
            Start by logging into your student portal on our university's official website. Use your assigned credentials (username and password) to access the portal.

            2. Navigate to E-Learning Section:
            Once logged in, look for a section related to "E-Learning," "Online Learning," or a similar term. This section is where you'll find links to the online learning platforms.

            3. Select Your Course:
            Within the E-Learning section, you may see a list of courses or a dropdown menu. Choose your specific course to access its dedicated online learning platform.

            4. Use Learning Management System (LMS):
            Most likely, our university employs a Learning Management System (LMS) like Moodle, Canvas, or Blackboard. Click on the link to the LMS associated with your course.

            5. Login to LMS:
            Enter your credentials again to log in to the Learning Management System. Once logged in, you should have access to course materials, assignments, discussions, and other relevant resources.

            6. Explore Additional Resources:
            Some courses may utilize supplementary online tools or platforms. Check the course syllabus or announcements on the LMS for information on any additional resources you may need.

            If you encounter any issues or have specific questions about a particular course, feel free to reach out to your course instructor or the IT support team for assistance. If you need further guidance, don't hesitate to ask me for help!

            '''

def resources_for_academic_support():
    return '''
            Certainly! To access our online learning platforms, follow these steps:

            1. Login to Student Portal:
            Start by logging into your student portal on our university's official website. Use your assigned credentials (username and password) to access the portal.

            2. Navigate to E-Learning Section:
            Once logged in, look for a section related to "E-Learning," "Online Learning," or a similar term. This section is where you'll find links to the online learning platforms.

            3. Select Your Course:
            Within the E-Learning section, you may see a list of courses or a dropdown menu. Choose your specific course to access its dedicated online learning platform.

            4. Use Learning Management System (LMS):
            Most likely, our university employs a Learning Management System (LMS) like Moodle, Canvas, or Blackboard. Click on the link to the LMS associated with your course.

            5. Login to LMS:
            Enter your credentials again to log in to the Learning Management System. Once logged in, you should have access to course materials, assignments, discussions, and other relevant resources.

            6. Explore Additional Resources:
            Some courses may utilize supplementary online tools or platforms. Check the course syllabus or announcements on the LMS for information on any additional resources you may need.

            If you encounter any issues or have specific questions about a particular course, feel free to reach out to your course instructor or the IT support team for assistance. If you need further guidance, don't hesitate to ask me for help!

            '''

def how_to_chose_major_courses():
    return '''
            Choosing major courses can be a significant decision, and it's important to approach it thoughtfully. Here are some steps to help guide you through the process:

            1. Understand Your Interests:
            Consider your interests, passions, and long-term career goals. What subjects excite you? Which areas do you find intriguing and enjoyable? Reflecting on your interests can help you identify potential major options.

            2. Assess Your Strengths and Skills:
            Evaluate your strengths and skills. What are you naturally good at? Your strengths can guide you towards areas where you're likely to excel and enjoy the coursework.

            3. Research Career Paths:
            Investigate potential career paths associated with different majors. Look into the job market, growth prospects, and the types of roles that align with each major. This can help you choose a major that leads to a fulfilling career.

            4. Meet with Academic Advisors:
            Schedule meetings with academic advisors or career counselors at your university. They can provide valuable insights, offer guidance on major selection, and help you understand the academic requirements of each major.

            5. Explore Course Catalogs:
            Review the course catalogs for different majors. Take note of the courses required for each major and see if they align with your interests and academic strengths. Consider the flexibility each major offers in terms of elective courses.

            6. Talk to Professors and Peers:
            Seek advice from professors and peers in the departments you are considering. They can provide firsthand insights into the coursework, industry connections, and potential research opportunities associated with different majors.

            7. Consider Your Values:
            Think about your values and how they align with the content of each major. For example, if contributing to social change is important to you, you might lean towards majors with a strong focus on social sciences or community development.

            8. Internships and Experiential Learning:
            Explore internship and experiential learning opportunities related to different majors. Practical experience can give you a real-world understanding of what a career in a particular field entails.

            9. Evaluate Degree Requirements:
            Review the degree requirements for each major, including core courses and any prerequisites. Make sure the major you choose aligns with your academic goals and timeline for graduation.

            10. Be Open to Exploration:
            Keep in mind that it's okay to be open to exploration, and you're not bound to a single major for your entire academic career. Many students change majors during their undergraduate years. Take introductory courses in different areas to get a feel for each subject before making a final decision.

            Remember that choosing a major is a personal decision, and there is no one-size-fits-all approach. Take your time, gather information, and choose a major that aligns with your interests, strengths, and future aspirations.
            '''

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

            if not user_fav_color.isalpha():
                print("You've not entered your favourite colour.")
                break


            elif user_fav_color == "Red":

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
                #break

            elif user_fav_color == "Yellow":

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
                #break

            elif user_fav_color == "Blue":

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
                #break

            elif user_fav_color == "Green":

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
                #break

            elif user_fav_color == "Orange":

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
                #break

            else: 

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
                #break
        else:
    
            print("You have entered a wrong option. Please, Chose \"Y\" for yes or \"N\" for no")
            user_fav_color = input("Please enter your favourite colour : ").capitalize()

    except ValueError:
        print("You have not entered a number for your age. Please try again")

while True:

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

    options = int(input("Please enter the number of the question category you'd like to ask : "))

    category_1_options = open("category_1_options.txt", "r")
    category_1_options_list = [] # This is a list

    for lines in category_1_options:
        
        temp_list = lines.strip('\n')
        temp_list = temp_list.split()

        joined = " ".join(temp_list)
        category_1_options_list.append(joined)

    print(f"Here are the category {options} options of our Frequently Asked Questions - FAQ : ")

    for count, option in enumerate(category_1_options_list, start=1):
        print(f"{count}. {option}")

    category_options = int(input("Please enter the option number of the option you'd like to ask : "))

    if category_options == 1:
        response = registration_response()
        print(response)
    elif category_1_options == 2:
        response = find_course_schedule()
        print(response)
    elif category_1_options == 3:
        response = how_to_access_online_learning_platform()
        print(response)
    elif category_1_options == 4:
        response = resources_for_academic_support()
        print(response)
    else:
        response = how_to_chose_major_courses()
        print(response)
    options = int(input("Please enter the number of the question you'd like to ask : "))


# faq_file = open("input.txt", "r")
# faq_list = [] # This is a list

# for lines in faq_file:
    
#     temp = lines.strip('\n')
#     temp = temp.split()

#     joined = " ".join(temp)
#     faq_list.append(joined)


# print("Here is a list of our Frequently Asked Questions - FAQ : ")


# for count, quest in enumerate(faq_list, start=1):
#     print(f"{count}. {quest}")

# choice = int(input("Please enter the number question you'd like to ask : "))

# while not choice == "none":
#     if choice == 1:
#         response = registration_response()
#         print(response)
#     choice = int(input("Please enter the number question you'd like to ask : "))

#     if choice == 2:
        
#         response = first_lecture_response()
#         print(response)
#     choice = int(input("Please enter the number question you'd like to ask : "))
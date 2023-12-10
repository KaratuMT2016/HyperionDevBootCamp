'''
• Start by creating a python file
• Name the python file award.py
• Write a comment in the file outlining the steps in writing the code
• Request time for swimming
• Request time for cycling
• Request time for runnning
• Compute total time for the triathlon
• Use the if...elif...else conditional statement
• Check which contion is TRUE based on the total time for the triathlon
• Print the TRUE statement
• End
'''
#Requesting time for the triathlon (All time are in minutes and of integer datatype)
time_swimming = int(input("Please, read in the time for swimming : "))
time_cycling = int(input("Please, read in the time for cycling : "))
time_running = int(input("Please, read in the time for running : "))

#Sum up the individual time 
total_times_for_triathlon = time_swimming + time_cycling + time_running

#Check the total time to see which condition is TRUE and print the statement
if total_times_for_triathlon <= 100:

    print(f"Your triathlon time of {total_times_for_triathlon}, qualifies you for the award of Provincial Colours ")

elif total_times_for_triathlon > 100 or total_times_for_triathlon <= 105:

    print(f"Your triathlon time of {total_times_for_triathlon}, qualifies you for the award of Provincial half Colours ")

elif total_times_for_triathlon > 105 or total_times_for_triathlon <= 110:
    
    print(f"Your triathlon time of {total_times_for_triathlon}, qualifies you for the award of Provincial Scroll ")

else:
    print(f"Your triathlon time of {total_times_for_triathlon}, does not qualify you for an award ")

# END
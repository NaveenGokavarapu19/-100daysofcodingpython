import time
import datetime


# Define function to take input as string
def take_input():
    time_required= input("Please enter the date in the dd/mm/yyyy :")
    return time_required

# Define a function to process the date to timestamp
def return_date(date):
    return time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())


time_entered = take_input()
time_stamp = return_date(time_entered)
print(" the time stamp is {} ".format(time_stamp))

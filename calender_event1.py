"""This project is about creating a calender to which user will have access through command line interface.
User can view, add, update and delete an event in the calender as his/her wish.
"""

from time import sleep, strftime
name = "Kevin"
calender = {}
def welcome():
    print("Welcome, " + name + ".")
    print("The calender is opening")
    sleep(1)
    print("Today is: " + strftime("%A %B %d, %y"))
    print("The time is: " + strftime("%H:%M:%S"))
    print("What would you like to do?")
def start_calender():
    start = True
    while(start):
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        if user_choice == "V":
            if len(calender.keys()) < 1:
                print("The calender is empty")
            else:
                print(calender)
        elif user_choice == "U":
            date = input("What date: ")
            update = input("What is the update: ")
            calender[date] = update
            print("Update is successful.")
            print(calender)
        elif user_choice == "A":
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print("Date entered is invalid.")
                try_again = input("Try again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calender[date] = event
                print("The event was successfully added to the calender.")
                print(calender)
        elif user_choice == "D":
            if len(calender.keys()) < 1:
                print("Calneder has no event.")
            else:
                event = input("What event: ")                
                del(calender[date])
                print("Event was deleted.")
                print(calender)
        elif user_choice == "X":
            start = False
        else:
            print("Invalid input")
            start = False
start_calender()
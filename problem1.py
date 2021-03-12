speed = int(input("Enter your speed: "))
speed_limit = int(input("Enter the speed limit: "))
fine = 0

if (speed >= 1 + speed_limit and speed <=20 + speed_limit):
    fine = 100
    print("Your fine is $" + str(fine))
elif (speed >= 21 + speed_limit and speed <=30 + speed_limit):
    fine = 270
    print("Your fine is $" + str(fine))
elif (speed >= 31 + speed_limit):
    fine = 570
    print("Your fine is $" + str(fine))
else:
    print("You're driving safe! You were under the speed limit")



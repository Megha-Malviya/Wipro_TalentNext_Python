#Create a python program that asks the user how far they want to travel.
# If they want to travel less than three miles tell them to ride Bicycle.
# If they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-Cycle.
# If they want to travel three hundred miles or more tell them to river Super-Car.
# Sample Output:How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination


distance = int(input("How far would you like to travel in miles? "))

if distance < 3:
    print("Ride Bicycle")
elif distance < 300:
    print("Ride Motor-cycle")
else:
    print("Drive Super-Car")
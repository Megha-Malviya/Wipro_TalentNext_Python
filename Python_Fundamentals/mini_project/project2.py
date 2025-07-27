"""Let's assume you are planning to use your Python skills to build a PBLApp for Mobile.
You decide to host your application on servers running in the cloud.
You pick a hosting provider that charges $0.51 per hour.
You will launch your service using one server and want to knowhow much it will cost to operate per day,per week,per month.
Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How many days can I operate one server with $918?"""


rate=0.51
hr=24
day=rate*hr
week=day*7
month=day*30
d=918/day
print("Rate per hour: $", rate)
print("Rate per day: $", round(day,2))
print("Rate per week: $", round(week,2))
print("Rate per month: $", round(month,2))
print(" How much days can I operate one server with $918? days: ", round(d,1))
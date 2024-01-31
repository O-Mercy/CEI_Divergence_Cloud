#2-5 Travel Time Calculator

miles_traveled = int(input("Enter miles: "))
miles_per_hour = int(input("Enter miles per hour: "))

hours = miles_traveled / miles_per_hour
minutes = miles_traveled % miles_per_hour * 60 / miles_per_hour

print("Estimated travel time")
print("Hours:", hours)
print("Minutes:", minutes)
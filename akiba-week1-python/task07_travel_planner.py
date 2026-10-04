destination = input("Enter destination: ")
distance = float(input("Enter distance in Kilometers: "))
average_speed = float(input("Enter average speed in km/h: "))

time_taken = distance / average_speed

print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Average Speed: {average_speed} km/h")
print()
print(f"Estimated Travel Time: {time_taken}")
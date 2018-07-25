cars = 100 
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# 0. The traceback function in python has no reference value for the name 'car_pool_capacity'. in the fixed output of code, line 7 defines 'carpool_capacity', NOT 'car_pool_capacity'. The traceback has to be for the exact defined variable.
# 1. The floating point in line 2, 4.0, is unnecessary. If included, any computed line of code that references line 2 and/or the variable 'space_in_a_car' will include a floating point. The computed code as it is now will output an integer.
# 2. floating point helps approximate values for equations that have remainders, or decimal values.
# 3. variables seem pretty self-explanitory
# 4. "The = (single- equal) assigns the value on the right to a variable on the left." ~ pg 42, LPTHW: Common Student Questions
# 5. The _ is a replacement character for a space (' ').
# 6. Sample variable mathematical expressions:

x = 5
y = 13
z = 8

print "x + y + z =", x + y + z 
print "x - z + y =", x - z + y
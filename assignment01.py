#Name: Example Solution
#Assignment 01

print('Task 01')
name = 'Mr. Smalley'
age = 100
favorite_show = 'Breaking Bad'
print('My name is', name)
print('I am', age, 'years old')
print('My favorite show is', favorite_show)

print('\nTask 02')
amount = 80
percent = 0.25
amount_off = amount * percent
print("The amount off is:", amount_off)

print('Optional Challenge:')
amount_paid = amount - amount_off
print("The amount paid is:", amount_paid)

print('\nTask 03')
width = 5
length = 10
area = width * length
print("The area is:", area)

print('Optional Challenge:')
perimeter = 2 * (width + length)
print("The perimeter is:", perimeter)

print('\nTask 04')
number = 17
remainder = number % 3
print("The remainder of", number, "divided by 3 is:", remainder)
times_divided = number // 3
print(number, "can be divided by 3", times_divided, "times")

print('\nTask 05')
city = 'Austin'
high_f = 95
chance_of_rain = 20
high_c = (high_f - 32) * 5 / 9
print('Weather Report for', city + ':')
print('High of ' + str(high_f) + '°F (' + str(round(high_c, 1)) + '°C) with a ' + str(chance_of_rain) + '% chance of rain.')

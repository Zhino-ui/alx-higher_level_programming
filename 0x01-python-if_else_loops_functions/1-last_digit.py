#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    dig = number % (-10)
else:
    dig = number % 10
if dig > 5:
    print("Last digit of {} is {} and is greater than 5"
            .format(number, dig))
elif dig is 0:
    print("Last digit of {} is {} nad is 0"
            .format(number, dig))
else:
    print("last digit of {} is {} and is less than 6 and not 0"
            .format(number, dig))

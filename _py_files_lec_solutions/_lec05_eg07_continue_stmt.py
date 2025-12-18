"""
Demo code for a continue statement
"""
sum = 0
number = 0

while number < 20:
    number += 1
    if number == 10 or number == 11:
        continue
    sum += number

print("The number is", number)
print("The sum is", sum)


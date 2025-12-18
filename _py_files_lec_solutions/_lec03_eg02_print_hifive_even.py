"""
Write a program that prompts the user to enter an integer. 
If the number is a multiple of 5, print HiFive. 
If the number is divisible by 2, print HiEven.

"""
number = int(input("Enter an integer: "))

if number % 5 == 0:
   print("HiFive")

if number % 2 == 0:
   print("HiEven")

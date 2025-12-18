"""
Write a program that prompts the user to enter two positive integers 
and finds their greatest common divisor. 
Solution:  
Suppose you enter two integers 4 and 2, their greatest common divisor is 2. 
Suppose you enter two integers 16 and 24, their greatest common divisor is 8. 
So, how do you find the greatest common divisor?
 Let the two input integers be n1 and n2. 
 You know number 1 is a common divisor, but it may not be the greatest common divisor. 
 So you can check whether k (for k = 2, 3, 4, and so on) is a common divisor 
 for n1 and n2, until k is greater than n1 or n2. 
"""

#Prompt the user to enter two integers
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))

gcd = 1
k = 2
while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1

print("The greatest common divisor for", 
    n1, "and", n2, "is", gcd)

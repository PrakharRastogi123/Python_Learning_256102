#Exponentiation is the raising of one number to the power of another.
#This operation is performed using two asterisks **.
#Let's use exponentiation to solve a known problem.
#You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount is doubled every day).
#Task:
#Write a program to calculate the amount that will result from the doubling to understand which choice results in a larger amount.

#soln:

a=0.01
b=1000000
if a*(2**30)>b :
    print(a*(2**30))
else:
    print(b)
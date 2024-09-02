""""
Write a Python program that asks the user for their age. If the user is 18 or older, print "You are
eligible to vote." Otherwise, print "You are not eligible to vote."
"""
age = int(input("please enter age:"))
if age > 18:
  print("you are eligible to vote")
elif age == 18:
  print("you are eligible to vote")
elif age < 18:
  print("you are not eligible to vote")



"""
Write a Python program that checks if a number entered by the user is positive, negative, or
zero, and prints the appropriate message
"""
number = float(input("please enter number:"))
if number == 1:
   print("number is positive")
elif number == -1:
    print("number is negative")
elif number < 1:
    print("number is zero")

"""
Write a Python program that asks the user to enter a number. If the number is both greater than
10 and even, print "The number is greater than 10 and even." Otherwise, print "The number
does not meet both conditions.
"""
number = float(input("please enter number"))
number = 10
if number > 10 and number % 2 == 0:
   print("the number is greater than and even")
else:
   print("the number does not meet both conditions") 


"""
Write a Python program that checks if a number entered by the user is either divisible by 3 or
divisible by 5, and prints the appropriate message.
"""
number = float(input("please enter number:12"))
if number / 3 or number / 5:
   print("the number is divisible by 3 or 5")
else:
   print("the number is not divisible by 3 or 5")



"""
Write a Python program that prints the numbers from 1 to 5 using a while loop.
"""
x = 1
while x < 6:
   print(x)
   x +=1

"""
Write a Python program that asks the user to enter numbers. Keep asking the user to enter a
number until they enter a negative number. Print the sum of all the numbers entered.

total_sum = 0
number = float(input("please enter number:"))
if number < 0:
 break
"""
"""
Write a Python program that asks the user to enter numbers. If the user enters a number greater
than 100, stop the loop using a break statement and print "Loop stopped."
"""
number = float(input("please input number:"))
while number < 6:
   print(number)
if number > 100:


   

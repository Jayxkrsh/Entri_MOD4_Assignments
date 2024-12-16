# Exercise 1
# months = ["January", "February", "March", "April", "May", "June",
#         "July", "August", "September", "October", "November", "December"]
# month_number=int(input("Enter Month Number:"))
# if 1 <= month_number <= 12:
#     print(f"Month {month_number} is {months[month_number -1]}")
# else:
#     print("Error: Please enter a number between 1-12")

# Exercise 2
# age = int(input("Enter your age:"))
# ticket_cost = 6
# if age < 16 :
#     print("Your ticket cost is: $",ticket_cost/2)
# elif age >= 60:
#     print("Your ticket cost: $",ticket_cost/3)
# else:
#     print("Your ticket cost is: $",ticket_cost)

# Exercise 3
# Weight = float(input("Enter your body weight in Kilograms:"))
# Height = float(input("Enter your height in meters:"))
#
# BMI = round(Weight/( Height ** 2),2)
#
# if BMI < 18.5:
#     print("Underweight")
# elif 18.5 <= BMI < 25:
#     print("Normal")
# elif 25 <= BMI < 30:
#     print("Overweight")
# else:
#     print("Obese")
# print("BMI:",BMI)

# Exercise 4
# num1 = float(input("Enter a number:"))
# num2 = float(input("Enter a number:"))
# num3 = float(input("Enter a number:"))
#
# Greatest = max(num1,num2,num3)
#
# print(f"The greatest number is:{Greatest}")

# Exercise 5
# num = int(input("Enter a number:"))
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else :
#     factorial=1
#     for i in range (1,num+1):
#         factorial*=i
# print(f"Factorial of {num} is : {factorial}")

# Exercise 6
# number = int(input("Enter a number to reverse: "))
# reversed_number = 0
#
# while number != 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number //= 10
# print(f"The reversed number is:{reversed_number}")

# Exercise 7
# num=int(input("Enter a number:"))
# for i in range(11):
#     print(num,"*",i,"=",num*i

# Exercise 8
# while True:
#     user_input = input(':')
#     if user_input.lower() == 'done':
#         print('Done')
#         break
#     print(user_input)

# Exercise 9
# for i in range(1, 11):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Exercise 10
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print()

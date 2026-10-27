# Question 1
print ("Question 1")

x = 3
y = 2

x += 3
y *= 2

result = x/y 

print (result)

# Question  2
print ("Question 2")

a = 67
b = 20
c = 45

if a > b:
    print ("a is greater than b")

if b % 2 == 0:
    print ("b is even")

if c <= a:
    print ("c is less than/equal to a")

final_condition = (a > b) or ((c <= a) and (b % 2 == 0))

print (final_condition)

# Question 3
print ("Question 3")

score = int (input("Enter your score (0 - 100): "))

if score >= 90:
    print ("A")

elif score >= 80:
    print ("B")

elif score >= 70:
    print ("C")

elif score >= 60:
    print ("D")

elif score < 60:
    print ("F")

# Question 4
print ("Question 4")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operation"

print(result)
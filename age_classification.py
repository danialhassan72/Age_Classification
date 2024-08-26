#age classification

name = "Muhammad Danial Hassan Khan "
age = 26
height = 6
is_student = True

# how to print the values and types
print("Name:", name,"| Type:",type(name))
print("age:", age,"| Type:",type(age))
print("height:", height,"| Type:",type(height))
print("is_student:",is_student,"| Type:",type(is_student))

# performing arithematic operations on user input numbers

#using function to get a valid number from the user

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

        num1 = get_number("enter the first number:")
        num2 = get_number("enter the second number:")

 #basic arithematic expression

        addition = num1 + num2
        subtraction = num2 - num2
        multiplication = num1 * num2

        if num2 != 0:
           division = num1/num2
        else:
           division = "undefined (division by zero)"


        print(f"addition: {num1} + {num2} ={addition}")
        print(f"Subtraction: {num1} - {num2} ={subtraction}")
        print(f"Multiplication: {num1} * {num2} ={multiplication}")
        print(f"Division: {num1} / {num2} ={division}")

# Task3: categories divided to users

#function to get a valid age from the user

def get_age(prompt):
    while True:
        try:
            age = int(input(prompt))
            if age < 0:
                print("age not into negative: please enter valid age.")
            else:
                return age
        except ValueError:
            print("invalid input. please enter a numeric value")

# prompting the user age into categories
if 0<= age <= 12:
    age_group = "child"
elif 13 <= age <= 19:
    age_group = "Teenager"
elif 20 <= age <= 64:
    age_group = "adult"
elif age >= 65:
    age_group = "senior"
else:
    age_group = "Invalid age range"

print(f"you are classified as : {age_group}")

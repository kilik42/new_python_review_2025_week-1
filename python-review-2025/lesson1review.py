#Part one: For each line of code below, write what type of variable is being stored (string, integer, or float). Write your answer as a comment next to each line of code.

first_name = "Bro" # for example: this is a string
food = "pizza" # this is a string
email = "Bro123@fake.com" # this is a string
age = 25
quantity = 3
price = 10.99
gpa = 3.2
distance = 5.5

#Part 2 – Predict the Output

#Without running the code, predict what each line will print:
print(f"Hello {first_name}") # for example: Hello Bro
print(f"You like {food}") # for example: You like pizza
print(f"Your email is: {email}") # Your email is: Bro123@fake.com
print(f"You are {age} years old")   # You are 25 years old
print(f"You are buying {quantity} items")
print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} km")


# Part 3 – Fix the Errors

# The following code has two mistakes.
# Find and fix them so it runs correctly.

name = "Bro"
food = "pizza"
print(f"Hello {name}")
print(f"You like {food}")

# Missing quotes and wrong variable name
favorite_food = "pizza"
print(f"You like {favorite_food}")

# Wrong f-string format
age = 17
print(f"You are {age} years old")

# Mismatched parentheses
price = 12.99
print(f"The total price is ${price}")
      

# Variable name spelled incorrectly
name = "Bro"
print(f"Hello {name}")

# Using + instead of commas
name = "Bro"
print("Hello " + name)

# Mixing single and double quotes incorrectly
email = "Bro123@fake.com"
print(f"Your email is: {email}")

# Forgot to include the f before the string
age = 21
print(f"You are {age} years old")

# Trying to use a number as a variable
cool = "yes"
print(f"Am I cool? {cool}")
# rule#1 Variable names cannot start with a number
# rule#2 Variable names cannot contain spaces
# example of incorrect variable space name
    # 1st place = "winner"  # incorrect
    # first place = "winner"  # incorrect
    # firstplace = "winner"  # correct
    # first_place = "winner"  # correct
    # firstPlace = "winner"  # correct
# rule #3 Variable names cannot use special characters
#  like !, @, #, $, %, etc.
# example of incorrect variable special character name
    # best@player = "Alice"  # incorrect 
    # best#player = "Alice"  # incorrect
    # best!player = "Alice"  # incorrect
# rule #4 Variable names cannot be the 
# same as reserved keywords in Python 
# like class, def, return, etc.  

# Missing curly braces
quantity = 3
print(f"You are buying {quantity} items")

# Using a reserved keyword
class1 = "ECS"
print(f"You are in {class1} class")

# Part 4 – Create Your Own

# Write a short Python program that:

# Creates at least three variables (a string, an integer, and a float)

# Prints a formatted message using f-strings that combines all three.
#  Example:
movie = "Inception"
rating = 9.5
year = 2010
print(f"My favorite movie is {movie}, released in {year}, rated {rating}/10!")

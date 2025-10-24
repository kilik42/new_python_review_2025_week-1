# Goal: show how input works, type conversion, and basic math output.


print("Welcome! We'll do some math.\n")
# input function always returns a string
# input function allows us to prompt the user for information

name = input("What's your name? ")
print(f"Hello, {name}!")
#ask for a birthday
birthday = input("When is your birthday? (MM/DD) ")
print(f"Awesome! I'll remember that your birthday is on {birthday}.")
#ask for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#print this out in a f-string
print(f"Great, {name}! You entered {num1} and {num2}.")
print(num1 + num2)  # This will concatenate the strings
# Get two numbers from the user and ask for their name to personalize the experience
















# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings
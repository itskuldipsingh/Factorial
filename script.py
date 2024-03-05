# Prompt the user to enter a number for which we will calculate the factorial
a = int(input("Enter factorial number: "))

# Initialize the counter variable 'b' and the result variable 'c'
b = 1
c = 1

# Start a while loop that continues as long as 'b' is less than or equal to 'a'
while b <= a:
    # In each iteration of the loop, multiply 'c' by 'b'
    c *= b
    # Then increment 'b' by 1
    b += 1 

# After the loop finishes, print the result. The f-string formats the output nicely.
print(f"{a}! = {c}")

# PROBLEM 1
# Create a variable that holds the value of your first name.

first_name = 'Spencer'

# PROBLEM 2
# Create a variable that holds the value of your favorite number.

fav_num = 8

# PROBLEM 3
# Create a variable that holds a boolean value representing if your hair is brown.

hair_brwn = 'true'

# PROBLEM 4
# Print your first name, by printing the variable created in problem 1.

print(first_name)

# PROBLEM 5
#  Create a variable called `loves_code` and set it equal to true. 
#  Check to see if `loves_code` is equal to true or false. 
#  If it is true, print "I love to code!"
#  If it is not, print "Coding has it's challenges."

loves_code = 'true'

if loves_code == 'true':
    print('I love to code!')
else:
    print("Coding has it's chanllenges")

# PROBLEM 6
# Create an array called `colors` and set it equal to a list of at least five colors.

colors = ['green', 'brown', 'tan', 'burnt orange', 'blue']

# Problem 7
# Using bracket syntax, print out the last item in your colors array.

# print(colors[4])

# For problems 8-9, use the following line of code:
numbers = [1,2,3,4,5,6,7,8,9,10]

# Problem 8
# Use a for-in loop to iterate over the `numbers` array and print each number.

for num in numbers:
    # print(num)

# Problem 9
# Create an empty array called `even_numbers`.
# Use a for-in loop to iterate over the `numbers` array, and if a number is even, add  it to the `even_numbers` array.

 even_numbers = []

for evnum in numbers:
    if (evnum % 2) == 0:
        even_numbers.append(evnum)

print(even_numbers)

# Problem 10
# Do not edit the code below.
score = 74
# Do not edit the code above.

# Determine if the letter grade of the given variable 'score'. If the variable is a 90 or above, console-log an 'A', between 80 and 89, console-log a 'B', between 70 and 79, 'C', between 60 and 69, 'D', and anything below 60 should console-log an 'F'.

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
elif score < 60:
    print('F')

# Problem 11
# Create a variable called 'changeMyMind' and set it equal to true. 
# Check to see if changeMyMind is set to true or false, if it is true, change the status to false, if it is false, change the status to true.

change_my_mind = 'true'
if change_my_mind == 'true':
    change_my_mind = 'false'
    print(change_my_mind)
elif change_my_mind == 'false':
    change_my_mind = 'true'
    print(change_my_mind)

# ADVANCED

# For problems 12-15, use the following line of code:
friends = ['Joe', 'Sally', 'Camilo', 'Perry', 'Susan']

# Problem 12
# Research to find the Python method that allows you to add an element to the end of the array (similar to push() in JavaScript), then add a name to the end of the `friends` array.

friends.append("Spencer")
print(friends)

# Problem 13
# Print out the total amount of elements in the `friends` array. The Python method you are looking for is similar to the JavaScript property `.length`.

print(len(friends))

# Problem 14
# Add a name into the third position in the array (index 2). Make sure you are not overwriting the value that is already there.

friends.insert(2, "Jake")
print(friends)

# Problem 15
# Remove the last item in the array (try to think about how you can do this dynamically, meaning, if the array contents were to change, your code would still work).

friends.pop()
print(friends)
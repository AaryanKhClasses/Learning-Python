'Used: https://docs.python.org/3/tutorial/controlflow.html'

# If Stataments
# If statements are the most popular statement types in Python or any other progarmming langauge!
x = int(input('Please enter an integer: ')) # This will make that when the file is ran, it will ask the question "Please enter an integer: " in the command prompt and then will store the input as the variable "x"
if x == 1: # This will run if the inputted integer is 1
    print('The integer you inputted was 1!') # This will be printed out if you input "1" in the command prompt!
elif x < 1: # The "elif" statement will be run if the first if(or an elif) statement returns "false" meaning you inputted an integer is less than "1"
    print('The integer you inputted was less than one!') # This will be printed if you input an integer less than "1" in the command prompt!
elif x > 1: # This "elif" statement will run if both the previous statements returns "false". That is, the inputted integer was not "1" nor lesser than "1"
    print('The integer you inputted was greater than one!') # This will be printed if you input an integer more than "1" in the command prompt

# For Statements
# The Python's "for" statement iterates over the item of any sequence (a list of a string), in the order that they appear in the sequence!
list = ['python', 'javascript', 'java']
for item in list: # for <any variable> in a "list" or a "string"
    # print(item, len(item)) # This will print every element in the list and the length of the corresponding element in the list (in a sequence)
    print(item, len(item), end=', ') # This will print out the same thing as above, but instead of having a new line for each element, it will print a ", " string after every for item element
    
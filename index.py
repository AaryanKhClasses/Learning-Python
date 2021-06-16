'Used: https://docs.python.org/3/tutorial/index.html'

# print() prints the given args(literal or a var)
print('Hello World')

# Comments
a = 1 # this is a comment and a comment starts with a "#" symbol!
b = "# this isnt a comment as it is inside of quotes!" # but this is a comment as it is not inside of quotes!

# Variables
# In the above example of comments we typed "a = somthing" and "b = something as well". Here "a" and "b" are called variables.
print(a, b) # this will print out the values of "a" and "b". 

# Numbers | You can use Python as a calculator too!
2 + 2 # This will give a result of "4" when printed!

# Python Operators
# Basic Python Operators
2 + 2 # The "+" operator "adds" the two number values!
2 - 2 # The "-" operator "subtracts" the two number values!
2 * 2 # The "*" operator "multiplies" the two number values!
2 / 2 # The "/" operator "divides" the two number values!
# The division in python will always return a "float" value! (See Float Below)

# What is an INT & a FLOAT
int = 3 # An integer is called as an int | Ex., `2, 6, 10`, etc.
float = 3.0 # A Float is a fractional value of a number | Ex., `5.6, 2.99, 3.0`, etc.

# Advanced Python Operators
5 / 2 # "Classic" Division retuns a float value (fraction) 
# This will return "2.5"

5 // 2 # The "//" operator "divides" the two number values and removes the "fractional" part! This is also known as "Floor" division!
# This will return "2"

5 % 2 # The "%" operator "divides" the two number values and returns the "remainder"!
# This will return "1"

5 ** 2 # The "**" operator is used for "exponents" where the first number is the "base" and the second is the "index"
# This will retrun "25"

# The "=" Operator
# The "=" operator is used for assigning variables!

# NameError
# A "Name"Error is will be thrown is a value of a variable is not defined!
# variable # This will give a NameError as the value of "variable" is not defined!

# Strings
# Strings are basically texts! You can assign a variable to be a "string" variable by putting double or single quotes
"This is a string with double quotes" # A string with double quotes!
'This is a string with single quotes' # A string with single quotes!
'Don\'t' # A "\" sign is used to escape a string!
"Don't" # Alternatively you can use two different types of quotes to avoid using the "\" sign escape!

# NewLines
newline = "This is a line\nThis is a new line!" # Use the "\n" sign in a string to make a new line!
print(newline)

# Raw String lines
# If you don't want to have the "\" sign to be interpreted with special characters, you can use a "raw" string!
rawStr = r'C:\some\name' # This will print as "c:\some\name" instead of making a new line (NOTE: Theres an "r" before the actual string!)
print(rawStr)

# Multiple Lines String
# Strings can have a span of multiple lines too!
multiple = r"""This is the first line,
This is the second line
and this is the third line with any \n's""" # This will make so the string will be in multiple lines without any \n's!
print(multiple)

# Concatenating Strings
# You can concatenate more than one strings into one strings with the help of the "+" operator
str1 = 'This is the first string, '
str2 = 'and this is the second string!'
print(str1 + str2) # This will print out the first and then the second string!

# You can also concatenate more than one string by typing more than one string literals next to each other
print('Hello ' 'World') # This will print out "Hello World" (NOTE: You have to include a " " in one of the two strings for a new word!)

# Repeating Strings
print(3 * 'Hello World ') # This will print out "Hello World " 3 times

# Concatenating Strings & Variables
py = 'Py'
# print(py 'Thon') # This wont work as "py" is a variable
print(py + 'thon') # This will print "Python" as the variable and the literal are concatenated with a "+" operator!

# Indexing Strings
# String literals are indexed from the index "0" (the first character of the string)
word = 'Python'
print(word[0]) # This will print the 0th index of the word (P)
print(word[-6]) # This will print the 6th index from the right! (P)
# As "-0" is same as "0", negative indexes starts from "-1"
print(word[0:2]) # This will print the 0th index (P) to the 1st index (y) (NOTE: The last index in the "(index1:index2)" series will excluded so, the "index2" will be "index2 - 1")
print(word[2:6]) # This will print the 2nd index (t) to the 5th index (n) (NOTE: Only the "last" index will be excludes, the "first" index does NOT exclude)
print(word[:2]) # This will print the 0th index (P) to the 1st index (y) (NOTE: If the 1st index is "0", then the function can also be written as [:i] instead of [0:i])
# This also works for the first index
print(word[:1] + word[1:]) # NOTE: This will return "word" | In short: (s[:i] + s[i:]) will return s

# IndexError
# print(word[99]) # This will give an "IndexError" as the string "word" doesnt have 99 indexes!

# Length of a string!
print(len('hello this has a length of 41 characters!')) # This will return "41" as the length of the string is 41!

'Next Up: https://docs.python.org/3/tutorial/introduction.html#lists'
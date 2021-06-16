'Used: https://docs.python.org/3/tutorial/introduction.html#lists'

# Lists
# Python has a number of "compound" data types, and the most versatile one is a "list"
# It can be written as a list of "comma seperated values (items)" between "square brackets []"
# Items in a list can be of different types (string, int, float, etc.)
list = [1, 8.0, "this is a string list item"] # List with different item types!
print(list) # This will print out "[1, 8.0, 'this is a string list item']"

# Indexing Lists
sqlist = [1, 4, 9, 16, 25]
print(sqlist[0]) # This will print out the 0th index from the list (1)
print(sqlist[-3]) # This will print out the 3rd index from the right (9) (NOTE: -0 is similar as 0, so negative indexes starts from -1)
print(sqlist[0:3]) # This will print out a new list from slicing the "sqlist" list! (1, 4, 9) (NOTE: Similar to the "String Indexing & Slicing", index1 will be includes & index2 will be exluded)

# Concatenating Lists
sqlist2 = [36, 49, 64, 81, 100]
print(sqlist + sqlist2) # Python lists support concatenation of two lists and will return a single list and the arrangement of the elements will depend on the order of the list to be concatenated!
# Thus, this will retrun [1, 4, 9, 16, 25, 36, 49, 81, 100]

# Changing List Elements
# Unlike Strings, you can change the elements of a list
list[1] = 8 # This will get the element of the 1st index of the list variable "list" and will change the element from "8.0" to "8"
print(list) # This will return the new list after changing the first index "8.0" to "8"

# Appending List elements to a list
# You can add elements in a list after the last element with the help of the "append()" method/function!
list.append('This is an appended element') # This will add the string "This is an appanded element" after the element ""
print(list) # This will print out the list variable "list" after adding the appended element at the end

# Length(Number) of elements of a list
# Similar to string, you can calculate the length(number) of elements of a list too with the help of the len() function!
print(len(list)) # This will return 4 as there are 4 elements in the list variable "list"
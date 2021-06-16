'Used: https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming'
'Fibonacci Series: https://en.wikipedia.org/wiki/Fibonacci_number'

a, b = 0, 1
while a < 1000: # The "while" loop will be executed as long as the "a < 1000" condition remains true
    print(a, end=', ') # The "end=', '" will make that instead of the "newline", a ", " string will be printed after every number is executed while a is less than 1000 
    a, b = b, a + b # This will make that a will be re-defined to be as "b" and b be re0defined to be as a sum of "a + b"
# This will print out the fibonacci series from 0 to 1000
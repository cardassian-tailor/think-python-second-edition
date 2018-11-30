'''

Exercise 1  

Write a function named right_justify that takes a string named s as a parameter and prints the 
string with enough leading spaces so that the last letter of the string is in column 70 of the display.

>>> right_justify('monty')
                                                                 monty

Hint: Use string concatenation and repetition. Also, Python provides a built-in function 
called len that returns the length of a string, so the value of len('monty') is 5.


I found this to be a little to ambiguous. I guess they wanted you to fumble around with 
how wide your terminal window is and guestimate the appropriate amount of spaces 
to have the text right justified ... but the excercise was way to non-specific for me. 
I'd assume the best way to solve this would be by getting the precise column count of the current 
working terminal window with shutils get_terminal_size() or via string formating .format() Here is my
 solution:  
'''

import shutil 
def right_justify(x):
	columns = shutil.get_terminal_size().columns
	if columns > 70+len(x):
		string = ((' '*(70-len(x))+x))
		testlen = len(string)
		last_letter = string[-1:]
		print(' '*(70-len(x))+x)
		print("Total length is: %s." %testlen)
		print("location of last letter, {},  of your input is: {}".format(last_letter, (string.find(last_letter, 69))+1))
	else:
		print("Failed")
x = input("input your word..  ")
right_justify(x)

#  https://docs.python.org/3/library/string.html#formatstrings
#  


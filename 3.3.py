'''
Exercise 3  

Note: This exercise should be done using only the statements and other features we have learned so far.

    Write a function that draws a grid like the following:

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +

    Hint: to print more than one value on a line, you can print a comma-separated sequence of values:

    print('+', '-')

    By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:

    print('+', end=' ')
    print('-')

    The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.
    Write a function that draws a similar grid with four rows and four columns.

    '''
plus = '+'; bar = '-'; side = '|'; space = ' '
header = plus + (bar *4) + plus + (bar*4) + plus 
sides = side + (space*4) + side + (space*4) + side 


def two_by_four():
	print(header + "\n"+((sides+"\n")*4) + header + "\n"+((sides+"\n")*4) + header)

def four_by_four():
	top = '+----+----+----+----+' + '\n'; sides = '|    |    |    |    |' + '\n'
	print(((top + sides*4)*2) + top + (sides*4 + top)+ (sides*4 + top))


'''

In [55]: two_by_four()
+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+

In [56]: four_by_four()
+----+----+----+----+
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
+----+----+----+----+
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
+----+----+----+----+
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
+----+----+----+----+
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |
+----+----+----+----+


In [57]:

'''
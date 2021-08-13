# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:50:21 2020

@author: FarjanAziz
"""

#Task1 - Store your own version of the message "Hello World" in a variable, and print it.
message="Hello Spyder World"
print(message)

#Task2 - 
#Store a message in a variable, and then print that message.
#Store a new message in the same variable, and then print that new message.
message="Hello Spyder World"
print(message)
message="Hello Spyder World again!"
print(message)

#Task3 - Find a quote that you like. Store the quote in a variable, with an appropriate introduction such as "Ken Thompson once said, 'One of my most productive days was throwing away 1000 lines of code'". Print the quote.
quote='Harry F. Banks once said, "Do today what should be done. Your tomorrow may never come."'
print(quote)

#Task4 - Store your first name, in lowercase, in a variable. Using that one variable, print your name in lowercase, Titlecase, and UPPERCASE.
name="farjan"
print(name.lower())
print(name.title())
print(name.upper())

#Task5 - Store your first name and last name in separate variables, and then combine them to print out your full name.
first_name="Farjan"
last_name="Aziz"
print(first_name+" "+last_name)

#Task6 - 
#Choose a person you look up to. Store their first and last names in separate variables.
# Use concatenation to make a sentence about this person, and store that sentence in a variable. Print.
first_name="Lonny"
last_name="Breaux"
sentence="is a great artist."
print(first_name+" "+last_name+" "+sentence)

first_name="Lonny"
last_name="Breaux"
sentence=first_name+" "+last_name+ " is a great artist."
print(sentence)

#Task7 - 
#Store your first name in a variable, but include at least two kinds of whitespace on each side of your name
#Print your name as it is stored.
#Print your name with whitespace stripped from the left side, then from the right side, then from both sides.
name="  farjan  "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# Arithmetic
# Write a program that prints out the results of at least one calculation for each of the basic operations: addition, subtraction, multiplication, division, and exponents.

print(10+2)
print(10-2)
print(10*2)
print(10/2)

# Order of Operaions
# Find a calculation whose result depends on the order of operations.
# Print the result of this calculation using the standard order of operations.
# Use parentheses to force a nonstandard order of operations.
# Print the result of this calculation.

print(10+2/6)
print((10+2)/6)

# Long Decimals
# On paper, 0.1+0.2=0.3. But you have seen that in Python, 0.1+0.2=0.30000000000000004.
# Find at least one other calculation that results in a long decimal like this.

print(0.1+0.2)
print(0.11+0.12)

# Neat Arithmetic
# Store the results of at least 5 different calculations in separate variables. Make sure you use each operation at least once.
# Print a series of informative statements, such as "The result of the calculation 5+7 is 12."

var1=(10+2)
var2=(10-2)
var3=(10*2)
var4=(10/2)
var5=(10+2/2)
result='The result of the calculation'

print(result+' '+'10+2'+' '+'is'+ ' '+ str(var1)+'.')
print(result+' '+'10-2'+' '+'is'+ ' '+ str(var2)+'.')
print(result+' '+'10*2'+' '+'is'+ ' '+ str(var3)+'.')
print(result+' '+'10/2'+' '+'is'+ ' '+ str(var4)+'.')
print(result+' '+'10+2/2'+' '+'is'+ ' '+ str(var5)+'.')

# Neat Order of Operations
# Take your work for "Order of Operations" above.
# Instead of just printing the results, print an informative summary of the results. Show each calculation that is being done and the result of that calculation. Explain how you modified the result using parentheses.

#((10+2)/6)
var1=(10+2)
var2=((10+2)/6)
first_calculation='First Order of Operation of (10+2)/6 is (10+2) because of the inner parenthesis around it. (10+2)='
second_calculation='Second Order of Operation of (10+2)/6) is the sum of (10+2) divided by 6. 12/6='
explanation='If we did not add the equation in the paranthesis before dividing, we would get a different incorrect answer. PEMDAS needs to be followed always. Paranthesis, Exponents, Multiplcation, Division, Addition, Subtraction'
print(first_calculation+str(var1))
print(second_calculation+str(var2))
print(explanation)

# Long Decimals - Pattern
# On paper, 0.1+0.2=0.3. But you have seen that in Python, 0.1+0.2=0.30000000000000004.
# Find a number of other calculations that result in a long decimal like this. Try to find a pattern in what kinds of numbers will result in long decimals.

#Binary integers sometimes results in long calculations. 
print(0.1+0.2)
print(0.11+0.12)
print(0.111+0.122)
print(0.1111+0.1221)
print(0.1212+0.2121)
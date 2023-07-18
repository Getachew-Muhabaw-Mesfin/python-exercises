#Section
num=0x1f #0-f
num2=0o45 #0-7
c=9.34e34
readnum =23_465_890

""" 
1. Literals are notations for representing some fixed values in code. Python has various types of literals - for example, a literal can be a number (numeric literals, e.g., 123), or a string (string literals, e.g., "I am a literal.").

2. The binary system is a system of numbers that employs 2 as the base. Therefore, a binary number is made up of 0s and 1s only, e.g., 1010 is 10 in decimal.

Octal and hexadecimal numeration systems, similarly, employ 8 and 16 as their bases respectively. The hexadecimal system uses the decimal numbers and six extra letters.
3. Integers (or simply ints) are one of the numerical types supported by Python. They are numbers written without a fractional component, e.g., 256, or -1 (negative integers).

4. Floating-point numbers (or simply floats) are another one of the numerical types supported by Python. They are numbers that contain (or are able to contain) a fractional component, e.g., 1.27.

5. To encode an apostrophe or a quote inside a string, you can either use the escape character, e.g., 'I\'m happy.', or open and close the string using an opposite set of symbols to the ones you wish to encode, e.g., "I'm happy." to encode an apostrophe, and 'He said "Python", not "typhoon"' to encode a (double) quote.

6. Boolean values are the two constant objects True and False used to represent truth values (in numeric contexts 1 is True, while 0 is False.

#########################
Remember: Data and operators when connected together form expressions. The simplest expression is a literal itself.
"""
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)


print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)



""" 
Remember: It's possible to formulate the following rules based on this result:

when both ** arguments are integers, the result is an integer, too;
when at least one ** argument is a float, the result is a float, too.
This is an important distinction to remember.

"""



"""
You should see that there is an exception to the rule.

The result produced by the division operator is always a float, regardless of whether or not the result seems to be a float at first glance: 1 / 2, or if it looks like a pure integer: 2 / 1.

Is this a problem? Yes, it is. It happens sometimes that you really need a division that provides an integer value, not a float.
"""
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)


"""
A // (double slash) sign is an integer division operator. It differs from the standard / operator in two details:

its result lacks the fractional part ‒ it's absent (for integers), or is always equal to zero (for floats); this means that the results are always rounded;
it conforms to the integer vs. float rule.
Run the example below and see the results:
"""
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print


#IMPORTATN Note Here

print(6 // 4) #1
print(6. // 4)#1.0
#The result of integer division is always rounded to the nearest integer value that is less than the real (not rounded) result.

#This is very important: rounding always goes to the lesser integer.
print(-6 // 4)#-2
print(6. // -4)#-2.0
print (-6//-4) #1
print (-6//-4.) #1.0

print(14%4) #As you can see, the result is two. This is why:

# 14 // 4 gives 3 → this is the integer quotient;
# 3 * 4 gives 12 → as a result of quotient and divisor multiplication;
# 14 - 12 gives 2 → this is the remainder.

print(12%4.5) #3.0
# 3.0 – not 3 but 3.0. The rule still works:

# 12 // 4.5 gives 2.0,
# 2.0 * 4.5 gives 9.0,
# 12 - 9.0 gives 3.0.
print(9 % 6 % 2) #1 form Left to right 
print(2 ** 2 ** 3) #256 from Right to left 2 ** 3 → 8; 2 ** 8 → 256
print(-3 ** 2) #-9
print(-2 ** 3)#-8
print(-(3 ** 2))#-9

"""
Key takeaways
1. An expression is a combination of values (or variables, operators, calls to functions ‒ you will learn about them soon) which evaluates to a certain value, e.g., 1 + 2.

2. Operators are special symbols or keywords which are able to operate on the values and perform (mathematical) operations, e.g., the * operator multiplies two values: x * y.

3. Arithmetic operators in Python: + (addition), - (subtraction), * (multiplication), / (classic division ‒ always returns a float), % (modulus ‒ divides left operand by right operand and returns the remainder of the operation, e.g., 5 % 2 = 1), ** (exponentiation ‒ left operand raised to the power of right operand, e.g., 2 ** 3 = 2 * 2 * 2 = 8), // (floor/integer division ‒ returns a number resulting from division, but rounded down to the nearest whole number, e.g., 3 // 2.0 = 1.0)

4. A unary operator is an operator with only one operand, e.g., -1, or +3.

5. A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.

6. Some operators act before others - the hierarchy of priorities:

the ** operator (exponentiation) has the highest priority;
then the unary + and - (note: a unary operator to the right of the exponentiation operator binds more strongly, for example 4 ** -1 equals 0.25)
then: *, /, and %,
and finally, the lowest priority: binary + and -.
7. Subexpressions in parentheses are always calculated first, e.g., 15 - 1 * (5 * (1 + 2)) = 0.

8. The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.



"""
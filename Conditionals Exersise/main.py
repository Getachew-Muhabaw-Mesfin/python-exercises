# x = 10
 
# if x < 5: # condition one
#     print("x is greater than 5")  # Executed if condition one is True.
 
#     if x < 10: # condition two
#         print("x is less than 10")  # Executed if condition two is True.
     
#     if x == 10: # condition three
#         print("x is equal to 10")  # Executed if condition three is True.
x = 10
 
if x == 10: # True
    print("x == 10")
 
if x > 15: # False
    print("x > 15")
 
elif x > 1: # True stope here 
    print("x > 10")
 
elif x > 5: # True
    print("x > 5")
 
else:
    print("else will not be executed")
    
"""
####### Noted
 If the condition for if is False, the program checks the conditions of the subsequent elif blocks
 - the first elif block that is True is executed. 
 If all the conditions are False, the else block will be executed.
"""
x = 1
y = 1.0
z = "1"
 
if x == y:
    print("one")
if y == int(z): #print and stope
    print("two")
elif x == y:
    print("three")
else:
    print("four")
    
"""
3.1.14 SECTION QUIZ
Question 1: What is the output of the following snippet?

x = 5
y = 10
z = 8
 
print(x > y)
print(y > z)
 
 
Hide
False
True
Question 2: What is the output of the following snippet?

x, y, z = 5, 10, 8
 
print(x > z)
print((y - 5) == x)
 
 
Hide
False
True
Question 3: What is the output of the following snippet?

x, y, z = 5, 10, 8
x, y, z = z, y, x
 
print(x > z)
print((y - 5) == x)
 
 
Hide
True
False
Question 4: What is the output of the following snippet?

x = 10
 
if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")
 
 
Hide
True
True
else
Question 5: What is the output of the following snippet?

x = "1"
 
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")
 
 
Hide
four
five
Question 6: What is the output of the following snippet?

x = 1
y = 1.0
z = "1"
 
if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")
 
 
Hide
one
two

"""
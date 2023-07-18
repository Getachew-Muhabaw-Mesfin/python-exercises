list_1 = [1]
list_2 = list_1
list_1[0] = 2
print("This is normal list",list_2)
"""You could say that:

the name of an ordinary variable is the name of its content;
the name of a list is the name of a memory location where the list is stored.
Read these two lines once more ‒ the difference is essential for understanding what we are going to talk about next.

The assignment: list_2 = list_1 copies the name of the array, not its contents. In effect, the two names (list_1 and list_2) identify the same location in the computer memory. Modifying one of them affects the other, and vice versa.

How do you cope with that?
"""
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print("Slice list",list_2) # 1

"""
Its output is [1].

This inconspicuous part of the code described as [:] is able to produce a brand new list.

One of the most general forms of the slice looks as follows:

my_list[start:end]
As you can see, it resembles indexing, but the colon inside makes a big difference.

A slice of this form makes a new (target) list, taking elements from the source list ‒ the elements of the indices from start to end - 1.

Note: not to end but to end - 1. An element with an index equal to end is the first element which does not take part in the slicing.

Using negative values for both start and end is possible (just like in indexing) 
"""
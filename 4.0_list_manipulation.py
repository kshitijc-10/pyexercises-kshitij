"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""
number_1 = 1
number_2 = 2
number_3 = 3
number_4 = 4
number_5 = 5
number_6 = 6

print(number_1)
print(number_2)
print(number_3)
print(number_4)
print(number_5)
print(number_6)

list = [1,2,3,4,5,6]
print(list)
print(list[3])

list.sort()
print("sorted list:", list)

sorted_list = list.pop()
print("sorted list:", sorted_list)

# 1. In: To create a list of numbers, sort it, remove the last number and print the sorted lis.
# 2. Process: creat a list, use the sort function, use the pop function then the print function.
# 3. Out: the sorted list is printed with the last number removed.
# 4. What my list is about, and what I computed from it: I created a list of numbers and sorted it, then removed the last number. The last number is interesting because it is the maximum number in the list.


# Your code below

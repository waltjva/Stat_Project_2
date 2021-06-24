# Table 1

# name	grade
# Jon	95
# Mike	84
# Jaime	99
 

# 1. (1 PT) Given the Table 1 data, create a dictionary called gradebook where the keys contain the names, and the values contain the associated grades. Print the dictionary.

gradebook = {"Jon":95, "Mike":84, "Jaime":99}

# 2. (1 PT) Index into gradebook to print Mike's grade.

print(gradebook["Mike"])
# 84

# 3. (1 PT) Attempt to index into gradebook to print Jeff's grade. Show the result.

# try:
#     print(gradebook["Jeff"])
# except:
#     print("error")
print(gradebook["Jeff"])

#   File "/Users/colemanwalterj/Documents/OneDrive/UVA MS Data Science/Programming for DS/HW 1 Data Tasks and Types.py", line 23, in <module>
#     print(gradebook["Jeff"])

# KeyError: 'Jeff'

# Questions 4-7c use Table 2.

# Table 2

# name	touchdowns
# Alex	2
# Patrick	4
# Tom	1
# Joe	3
# Alex	1

# 4. (1 PT) Build a list from the names in Table 2 and print it.

names = ["Alex", "Patrick", "Tom", "Joe", "Alex"]
print(names)


# 5. (1 PT) Sort the list in ascending order and print it.

print(sorted(names))
# ['Alex', 'Alex', 'Joe', 'Patrick', 'Tom']

# 6. (1 PT) Build a set from the names in Table 2 and print it.

names_ = {"Alex", "Patrick", "Tom", "Joe", "Alex"}
print(names_)
# {'Joe', 'Patrick', 'Tom', 'Alex'}

# 7a. (1 PT) Build a list from the touchdowns, calling it td, and print it.

td = [2, 4, 1, 3, 1]

# Parts 7b, 7c can be most easily accomplished with a list comprehension.
# We will discuss these further later, but for now, please read this brief article about them:

# https://www.w3schools.com/python/python_lists_comprehension.asp

# 7b. (2 PTS) Use the modulo operator (%) to store in a list only the odd values from td. Print this new list.

odd_td = [x for x in td if x % 2 == 1]
print(odd_td)
# [1, 3, 1]

# 7c. (1 PTS) Store in a list only the values from td which are greater than 1. Print this new list.
great_one = [x for x in td if x > 1]
print(great_one)
# [2, 4, 3]

import numpy as np

# In 1D :-
    # same as list using indexing
    # zero based indexing (starts from zero)
    # arrayname[index]

# y=np.array([1,2,3,4,5])
# print(y[2])

# to access the last element we can use arrayname[len(y) - 1] 
# but we can also use negative indexing 
# -1 is the index of the last element
# -2 is the index of the second last element



# question :- print the numbers of the array using the negative indexing
# y=np.array([1,2,3,4,5])
# for i in range (-len(y),0,1):
#     print(y[i])

# now print in reverse ordetr :-
# y=np.array([1,2,3,4,5])
# for i in range (-1,-len(y)-1,-1):
#     print(y[i])




# what if we want to print sub array ?
    # array slicing (same as list slicing):-

# y=np.array([1,2,3,4,5])
# print(y[1:4])       # way to print a sub array
# x=y[1:4:1]            # creating a sub array

# [start,end,step size]
# start is included and end is not included
# step size by default is 1 and if we dont write it then it wont show any errors
# and if we leave start or end place empty then it will take start as 0 and end as len(array) as default



# question :- generate an array using the arange function from 1 to 100 and print all the numbers with stepsize 3

# x=np.arange(1,101)
# print(x[1:101:3])

# reverse the list (using the slicing):-
# y=np.array([1,2,3,4,5])
# y=y[::-1]       # when stepsize is -1 then default of start and end are interchanged
# print(y)        # prints [5,4,3,2,1]









# 2D :-
    # THE rows and colums start from base 0
#     # the first element is [0,0] and last one is [(len-1),(len-1)]
# y = np.arange(1,13).reshape(3,4)
# print(y[0])     # way to access the rows 
# print(y[1][2])   # way to access the  arrayname[row][element index(column)]    this will access the second column of the first row



# to find number of rows :-
# print(len(arrayname))

# to find number of columns :-
# print(len(arrayname[0])



# Question:- print all elements of the matrix :-


# x=np.arange(1,13).reshape(3,4)

# for i in range(0,len(x)):
#     for j in range(0,len(x[0])):
#         print(x[i][j])



import numpy as np

# ---------------------------------------------------------
# SLICING OF 2D ARRAY
# ---------------------------------------------------------


# Create a 2D array using reshape
y = np.arange(1, 13).reshape(3, 4)
# print("Original Matrix:\n", y)



# ---------------------------------------------------------
# ACCESSING ROWS
# ---------------------------------------------------------

# Method 1: Direct indexing (gets the entire first row)
# print(y[0])             


# Method 2: Explicit slicing (preferred for readability)
# print(y[0, :])           # row 0, all columns


# You can also write:
# print(y[0][:])           # row 0, all columns


# Access specific columns from a row
# print(y[0, 0:3])         # row 0, columns 0 to 2




# ---------------------------------------------------------
# ACCESSING COLUMNS
# ---------------------------------------------------------


# To extract a single column, use :
# print(y[:, 0])           # all rows, column 0




# ---------------------------------------------------------
# SUB-MATRIX SLICING
# ---------------------------------------------------------

# Example: Extract rows 0–1 and columns 1–3
# print(y[0:2, 1:4])



# what if we need a 1st and 2nd column of all rows:-
# print(y[:,0:3])


# so basically we write [x:y , a:b]
# and in x and y we give the index of rows we need 
# and in a and b we give the index of columns we need
# and leaving it like [:,:] will just give you the matrix 
# whenever we write : it mean the whole row or column


# print  7, 8,
#       11,12

# print(y[1:3,2:4])
# or simply
# print(y[1:,2:])




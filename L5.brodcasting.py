import numpy as np

arr = np.arange(1,13)
brr = np.arange(13,25)


# scaler operations
# print(arr + 10)     # add 10 to every element
# print(arr * 10)     # multiplying every element by 10
# print(arr + brr)    # adding two arrays



# in 2D :- 

a = np.arange(1,13).reshape(3,4)
b=np.array([10,20,30,40])

# print(a + 100)      # add 100 to each element of the matrix

# print(a+b)
        # this will add b to a
        # like 10 will be added to every 1st column of each row
        # and 20 will be added to all second columns and so on


# you need to know that all the normal matrix rules are applied here
# like you cant add a (4,3) matrix to a (6,7) matrix and so on





# these rules are called as """BRODCASTING""" rules 
# brodcasting in np is a powerful mechanism that allows arithmetic operations on arrays of different shapes and sizes
# its kind of same as the multiplication rules you learnt in school

# operations will occure if one of the two conditions is match 

        # at least one dimension should be 1 also the other one should match
        # either number of rows or number of columns of one of them should be 1 
        # like (3,1) + (3,4) is correct ,, (1,5)+(10,5) is also correct
        # or they are of same shape


# a = np.arange(1,10).reshape(3,3)
# b = np.arange(11,20).reshape(3,3)

# print(a+b)              # both have same dimensions so addition works
# print(a*b)              # both have same dimensions so multiplication works



# x = np.arange(1,13).reshape(3,4)
# y = np.array([1,2,3])
# print(x.shape,y.shape)          # y is 1D so cant add

# y=y.reshape(3,1)

# print(x+y)
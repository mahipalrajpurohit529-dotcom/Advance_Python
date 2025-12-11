# numpy is a fundamentle library in python for scientific calculations 
# numpy stands for numerical python
# efficient on multi-dimensional arrays
# it is a collection of high level mathemetical functions
# efficient for large data
# high performance

import numpy as np

# a=np.array([1,22,3,4])
# print(type(a))

# 2d array by 2d list :-
# b=np.array([[1,2,3],[4,5,6]])
# print(type(b))     

#3d array using 3d list :-
# c=np.array([[[1,2,3]]])
# print(type(c))

# creating matrix :-

# print(np.zeros((4,5)))      # this will create a matrix of 4 rows and 5 columns)
# x=np.zeros((4,5))

# print(x.ndim)           # gives you the dimension of the array

# print(np.ones((5,8)))           # these will be floats when printed
# print(np.ones((4,5),dtype=int))         # way to print the matrix in int format


# there is another function called eye() that prints identity matrix(the matrix whose diagnal elements are 1 and every other element is 0)

# print(np.eye(3))




# we have made matrices with lists 
# how to do it without lists :-
# arange function :- it returns an array in that range 

# print(np.arange(1,11))      # BUT IT will be in 1d 

# way to change dimension :-(using reshape() function)

# y=np.arange(1,13).reshape(3,4)      #1,13 creates an array then reshape turns it into a matrix of 3,4
# print(y)

# but for reshape to work the elements in range must always be eauals to the elements required to make that matrix
# always take the number of elements in range (say 12) then the digits in the reshape should be factors of 12 
#  or in other word their multiplication should be equals to the elements created by range 

# also consider that if stepsize of range is changed the number of elemets created by range changes accordingly  




# there is a function called linespace that gives a number of elements in a range (which also we provide )
# including start and end 
# 
# for example 10 to 20 with 5 elements 
# it will give us 10, 12.5, 15, 17.5, 20 

# print(np.linspace(10,20,5))         # same as range but (start ,end ,number of elements we want )

# also remember it devides equally the given range 




# we can also add every elemnt of a list by an int

# a = np.linspace(10,20,12).reshape(3,4)
# b= np.linspace(30,40,12).reshape(3,4)


# print(a)
# print(a+10)     # ez sum

# print(a+b)          # adding two arrays ezz

# we can perform any arithemetic opperation on it, not just adding


# 20 to 100 create an matrix of size (20,4)

# print(np.arange(20,100).reshape(20,4))









# 1D array :-

# create an array of 1 to 100 numbers

# num=[x for x in range(1,101)]
# print(num)
# b=np.array(num)
# print(b,type(b))
# print(b.ndim)           # .ndim used for checking the dimension of the array



# 2D array :-

#  [1,2,3,4]    # row 1st
#  [4,5,6,7]    # row 2nd
#  [7,8,9,0]    # row 3rd
#cl 1 2 3 4


# checking the shape(rows and column) :-

# li1=[[1,2,3],[4,5,6],[7,8,9]]
# x=np.array(li1)
# print(x.shape)          # shows shape(3,3) or rows by column
# print(x.ndim)           # shows dimension

# total number of elements(rows*columns) :-
# print(x.size)





# there is a function called ones and one called zeroes that can make a matrix for you with each element = 1,0
# the zeroes and ones are defaulty in float 
# if you want you can change it 
# a = np.ones((4,4),dtype=int)   # this will create a matrix of size 4,4 with ones(int)


# make a matrix of 5*5,orint shape dimension and size 


# y=np.ones((5,5))            # when using ones or zeroes be carefull to use two paranthesis (())
# print(y.shape)
# print(y.size)
# print(y.ndim)
# print(y)


# notice how we are creating a list and then turn it to a array 
# this is slow and kills the whole point of arrays being fast 
# so we use arange function

# y = np.arange(1,101)        # this will directly create an array 
# print(y)
# print(y.ndim)       #this is 1d

# so what if we wanna change it to 2d or 3d?
# we do it by using reshape function

# y=y.reshape(10,10)      # in reshape we pass rows,column we want 
#                         # also remember that rows*column should always be equals to the total number of elements 
# print(y)



#assignment :-
#   what is matrix ,why use it and what is the use of its operations into the machine learning
#   what are matrix operations


# y = np.linspace(10,20,6).reshape(3,2)
# print(y)




# learnin assignment :-
    # slicing on the matrices 
    # vactorisation
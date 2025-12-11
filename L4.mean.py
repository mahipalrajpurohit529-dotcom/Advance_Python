import numpy as np


# mean :-

li = [x for x in range (0,101)]     # a big list 
# print(np.mean(li))      # way to find mean of li list with ease

# because normal method would take a lot of time 






# median :-
    # median is the mid value of the array
    # fisrtly the array is sorted in accending order 
    # then 
    # if number of elements is odd then     
            # median = {(n+1)/2}th element
    # if the number of elements is even then :-
            # median is {(n/2)th + [(n/2)+1]th }/2

# where n is the number of elements 
# print(np.median(li))        
        # no. of elements =>101
        # so median = {(101 + 1)/2}th
        # ==> 102/2
        # ==> 51th element
        # ==> 50  (because first element was zero)


# mode :- 
    # it gives you the element that occured the most times in the array
    








# flatten method :- 
    # used to convert a whole matrix into a single array 
    # opposite of reshape 

# x = np.arange(1,13).reshape(3,4)        # this creates a 2D array
# x=x.flatten()       # turns it into array
# print(x)




# generate a matrix using random module and then find last 2 column
# 2d elemenbts --> mean --> flatten --> mean

# ans 1 :- 
np.random.seed(34)
a = np.random.randint(0,15,12).reshape(3,4)
# print(a[:,2:])


# ans 2 :-

mat = a 
# print(np.mean(mat))

# print(mat.flatten().mean())






# ravel :- 

    # it is same as flatten 
    # but flatten creates a copy and changes made to the copy do not affect the original matrix
    # whereas the ravel points to the same memory address as the original array 
    # and the changes made will be applied to both the variables/copies

li=np.arange(1,13).reshape(3,4)
print(li)
ab=li.ravel()       #syntax
# remember that ravel also flattens the matrix

print(ab)
print(li)

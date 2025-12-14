import numpy as np


# stacking :-
    # we put multiple arrays together 
    # horizontally or vertically (your choice)
    # use np.vstack([array1,array2,...]) or np.hstack([...])
    # this stacking is just like 2d array


# a = np.array([1,2,3])
# b = np.array([4,5,6])
# c = np.array([7,8,9])
# x = np.vstack([a,b,c])
# print(x)



# q. take an array ranging between 10 to 35 ,those who are 18 and below become child and others become adult

# a = np.arange(10,36)
# b = np.where(a>18,'adult','child')
# print(a,b)









# horizontle stacking :- 

    # we keep adding and stacking the arrays horizontally
    # its more like macking a single big 1d array


# a = np.array([1,2,3])
# b = np.array([4,5,6])
# c = np.array([7,8,9])

# x = np.hstack([a,b,c])          
# print(x)



# but what if we had 2d array ? how would hstack work there ?
        # in that case both the arrays must have same number of row 
        # and it would just be like adding all the columns of the second array at the end of the first one 


a = np.arange(1,13).reshape(3,4)
b = np.arange(21,24).reshape(3,1)
x = np.hstack([a,b])
print(x)

# notice how number of rows must be same for hstack 
# similerly the number of colums must be same for vstack
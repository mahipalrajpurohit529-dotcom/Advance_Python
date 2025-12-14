import numpy as np



# 1st :- randint


# it selects a intiger at random in the givem range 
# it returns an array
# start is inclusive and end is exclusive 
# we can also select the number of elements or ints we need 

# syntax :- np.random.randint( start , end , number of element needed )
# remember that end is not included 
# also it choose a number n times at random 
# that means that the array may or may not have same ints at diff positions 

# y = np.random.randint(1,10,5)       # between 1 and 10 selects 5 ints at random
# print(y)





# what if we want to make it so so that it choose one random int and then stick to it for all runs 
# rather than selecting new array every time 

# # we use seed ()

# np.random.seed(43)          # syntax 
#                             # the 43 is just a random number you can put any int there
# x=np.random.randint(0,10,5)
# print(x)








# 3rd :- rand():-
# 

# rand creates an array of random floats between 0 and 1
# we pass the number of elements we want as the argument in it 


# z=np.random.rand(40)        # creates an array with 40 random floats between 0 and 1
# print(z)








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
# print(li)
ab=li.ravel()       #syntax
# remember that ravel also flattens the matrix

# print(ab)
# print(li)








# fancy indexing :-


# arr = np.random.randint(1,11,10)

# we want 1st ,4th and 5th element in a new array
# normally we would make a new empty list 
# then we run for i in [1,4,5]
# then append them  to it 
# then put it in array() finction


# arr1=[]
# for x in [1,4,5]:
#     arr1.append(arr[x])
# arr1=np.array(arr1)

# but this is a long code and slow
# so we use fancy indexing that lets us create a sub array from an array

# fancy indexing is a technique in programming in numpy that allows us to select
# multiple elements from an array at once and put it in a new sub array


# arr1=arr[[1,4,5]]       # one line code 
# print(arr1)         

# here we only give the indices of the array that we want to use to make the sub array
# also remember that we give it in list format











# copies :-

# there is another method called arrayname.view() that creates a copy
# actually it copies the reference of the og array# so any changes made will reflect in the og array

# arr = np.arange(1,11)   # creating array
# print("og array before change :: ",arr)
# arr2 =arr.view()    # creating view/copy
# arr2[0]=100         # changing elements in the copy

# print("og array after change :: ",arr)
# print("copied aarray ::",arr2)




# but view copy the reference 
# what if we want a copy that doesnt affect the og array
# we use .copy() functions 


# arr = np.arange(1,11)   # creating array
# print("og array before change :: ",arr)
# arr2 =arr.copy()    # creating view/copy
# arr2[1]=20         # changing elements in the copy

# print("og array after change :: ",arr)          # OG array is retained 
# print("copied aarry ::",arr2)










# we have another function called where ()
# this is used for conditional selection  and replacement of elements of numpy array

a=np.arange(1,11)   
x=np.where(a>4)     # makes an array of indexes of a which are greater that 4
print(x)

# x is an array of indices 
# all the indices present in x are the indices of elements of a that are greater than 4




# we can also change them :-
y=np.where(a>4,'high','low')          # change the value of all satisfying the condition as high and remaing to low
print(y)








import numpy as np 

# Q1 . Create a 1D NumPy array containing numbers from 5 to 50 with a step of 5.

x = np.arange(5,51,5)
print(x)



# Q2 . Create a 2D array of shape (4, 3) filled with ones.

x = np.ones((4,3))
print(x)




# Q3 . Create an array of 6 equally spaced values between 0 and 1.

x = np.linspace(0,1,6)
print(x)




# Q4. Create a 3×3 identity matrix.

x = np.identity(3)
print(x)




# Q5 .Find the shape, size, number of dimensions, and data type of a given array.

x = np.arange(1,13).reshape(3,4)
print(f"number of dimension == > {x.ndim}  ::  data type => {x.dtype}  ::  size ==> {x.size}  ::  shape ==> {x.shape}")





# Q6. Convert the Python list [10, 20, 30, 40, 50] into a NumPy array.

list = [10, 20, 30, 40, 50]
x = np.array([10, 20, 30, 40, 50])
print(type(x))





# Q7.  Reshape a 1D array of 16 elements into a 4×4 matrix.

x = np.arange(1,17)
x = x.reshape(4,4)
print(x)




# Q8.  Flatten a 2D array into 1D using both flatten() and ravel(). Observe the difference

x = np.arange(1,13).reshape(3,4)
y = x.flatten()
z = x.ravel()

print(y,z)





# Q9. Access the middle element of a 1D array.

x = np.arange(1,22)
print(x[(len(x)//2)])






# Q10. Reverse a NumPy array without using loops.

x = np.arange(1,13)
x = x[::-1]
print(x)






# Q11. Extract all even-indexed elements from a NumPy array.

x = np.arange(1,13)
y = x[::2]
print(y)






# Q12. Extract the last column from a 2D array.

x = np.arange(1,13).reshape(3,4)
print(x[:,3:4])





# Q13. Slice a 1D array to get alternate elements starting from index 1.

x = np.arange(1,13)
y = x[1::2]
print(y)







# Q14. Extract a 2×2 sub-matrix from a 3×3 matrix.

x = np.arange(1,10).reshape(3,3)
y = x [0:2,0:2]
print(y)






# Q15. Print all elements except the first and last element of an array.

x = np.arange(1,13)
print(x[1:(len(x)-1)])






# Q16. Select all elements greater than 25 from a NumPy array.

x = np.arange(10,50)
y = np.where(x>25)
print(y)






# Q17. Replace all negative values in an array with 0.

x = np.arange(-10,20)
y = np.where(x<0,0,x)
print(y)







# Q18. Extract only the elements divisible by 3.

x = np.arange(0,23)
y = np.where(x%3==0)
print(y)







# Q19. Count how many elements are greater than the mean of the array.

x = np.arange(1,101)
y = x.mean()
z = np.conj(np.where(x>y))
print(z)








# Q20. Find the indices of elements where the value is equal to 50.

x = np.arange(30,60)
print(np.where(x==50))







# Q21. Add two NumPy arrays element-wise.

x = np.arange(1,13).reshape(2,6)
y = np.arange(21,27).reshape(1,6)
print(x+y)






# Q22. Perform matrix multiplication of two compatible matrices.

x = np.arange(1,16).reshape(5,3)
y = np.arange(101,104).reshape(1,3)
print(x*y)






# Q23. Add a scalar value 10 to every element of a NumPy array.

x = np.arange(40,55).reshape(5,3)
print(x+100)






# Q24. Add a 1D array of shape (3,) to a 2D array of shape (2, 3) using broadcasting.

x = np.arange(1,7).reshape(2,3)
y = np.array([100,1000,10000])

y = y.reshape(1,3)

print(x+y)

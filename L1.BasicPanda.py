# PANDAS 
    # it is a library which is used to manupilate the data and analyse it 
    # pandas is built on the top of numpy library

import pandas as pd 
import numpy as np


# to read csv(comma separated values)
# syntax ==> pd.read_csv(path of the file)
# pd.read_csv()


# pandas have 2 types of data types :-
    # 1.series 
    # 2.dataframe

# Series :-
        # series is a primary panda data structure that is built on top of NUmpy arrays 
        # a panda series is a one dimensional labeled array that offers additional features like explicit indecing 
        # and integrated missing data handeling , making it ideal for data analysis

# x = pd.Series(np.array([1,2,3,4]))  # created a series with the help of numpy array
# print(x)

# we can change the indexng system 
# like we can change indexing from 0,1,2, to a,b,c
# but we have to pass it like :-

# x=pd.Series(np.array([1,2,3,4]),index=['a','b','c','d'])
# print(x)

    # and also the number of index given should be exactly equals to the elements in the array





# creating a series with help of a list :-

li=[1,2,3,4]
li_idx = ['a','b','c','d']
y = pd.Series(li,index=li_idx)
# print(y)




# creating a series with help of a dictionary :-

    # when we create a series with the help of dictionary, 
    # the key becomes index and value will become value

d ={'a':10,
    'b':20,
    'c':30,
    'd':40
}

d=pd.Series(d)
# print(pd.Series(d))


# print(d.values)
    # .values return the values in the form of numpy array

# print(d.index)
    # .index returns the indices of the series 

# print(d.dtype)
    # .dtype returns the datatype






# we can do vactorised operations here on these series too :-
s1 = pd.Series([1,2,3,4])
s2 = pd.Series([10,20,30,40])

# print(s1+s2)    # adding two series
# print(s1+1)     # adding 1 to each element of s1
# print(s1**2)    # printing sq of all elements of s1









# indexing :-

sr =pd.Series(np.arange(1,13))   # CREATING A SERIES 

# print(sr[sr>5])     # returns every element greater than 5
# print(sr[sr%2==0])  # returns even numbers

        # so basically we can apply the arithematic logics here



    





# DATA FRAMES :-

    # it is basically a data type in pandas
    # it is a two dimensional table like data structure used for data manipulation in python

    # here data is in the form of tables
    # the rows are labeled observations (also called index)
    # columns are labeled variables that can hold different data types 

# creating data frames with dictionary :-

details = {
    'name':['RAHUL','AMAN','NAMAN'],
    'subject':['maths','english','ssc'],
    'marks':[50,60,34],
    'address':['JAIPUR','DELHI','MP']
}

x = pd.DataFrame(details)
# print(x)

        # remember that all the values of the dictionary we made 
        # or array(if we had made that) must be same

        # we can use index= to change the names of the rows 

x = pd.DataFrame(details,index=['1st','2nd','3rd'])
# print(x)



# making dataframes with  list :-

details = [
    ['Rahul','Maths',50,'Jaipur'],
    ['AMAN','English',70,'Delhi'],
    ['Naman','Science',83,'Madhyapradesh']
]

y = pd.DataFrame(details)
# print(y)          # notice that we do not have the name of the columns
                    # but instead just the indices in their place
                    # to give names to the column we use column keyword


z = pd.DataFrame(details,columns=['NAME','SUBJECT','MARKS','PLACE'])
# print(z)


import pandas as pd
import numpy as np


# df = pd.read_csv(r"C:\Users\asus\Downloads\people-100.csv")

# # print(df.head())    # gives you starting 5 rows by default
# # print(df.head(10))  # gives you starting 10 roews 

# # print(df.sample())          # sample gives you one raw at random
# # print(df.sample(10))        # gives you 10 random rows

# # print(df.tail())            # gives you last five rows 
# # print(df.tail(10))          # gives you last 10 rows



# # the data is mainly of two types :-
#         # numerical :- contains numbers like phone no. , age ,etc
#         # catagorical :-= contains text like gender,name,email,date


# # df.info()           # gives you the data type of each column

# df2 = pd.read_csv(r"C:\Users\asus\Downloads\annual-enterprise-survey-2024-financial-year-provisional.csv")
# # df2.info()


# df3= pd.read_csv(r"C:\Users\asus\Downloads\finance.csv")
# # df3.info()
# df3.describe()          # is used to show five point summary of the data 
#                         # it shows the statistical properties of the data on the numerical columns
#                         # minimum-->0th percentile , 25th percentile ,50th percentile,75th percentile,max --> 100th percentile 
#                         # we also have count that shows the count of the column
#                         # we also have mean and std daviation

# df3.isna.sum()         # it returns the total number of null values from the data frame along with their column names
# df3.isna()             # returns true or false by checking weather the row entry is null or not              




# # to find the position of the null we use 
# df['columnname'].isna().sum()

# # to change the null postions :-
# df.fillna(0,inplace=True)                       # this will replace all the nulls with 0
#                                                 # the inplace=true will apply these changes to the original table/dataframe



# df['category'].unique()
# to find the all categories of the dataframe we use .unique() method 
# it returns an array of categories


# df['category'].value_counts()
# to find the total number of values count of the each category of the categorical column we use .value_counts() method


# numerical_data = df.select_dtypes(include='float')
# df.select_dtypes(exclude='float')

# for selecting the cat column we use 
# df.select_dtype (include='float') -> df.select_dtype(include='data type')

# to filter put some type of data we use : -

# numdata = df.select_dtypes(include='float')             #  this will select the floats and then asign them to numdata
# data2 = df.select_dtypes(exclude='floats')              # this will select everything except the floats
 
















import seaborn as sns 
df= sns.load_dataset('tips')




# print(df['time'].unique())      # gives you unique values
# print(df['time'].value_counts())        # gives you the count of all the entris in the time column

# print(df)
# df.drop('day',axis=1)        # this will drop the day column 
# print(df)                                    # axis 1 is for column and axis 0 is for row
                                    # these changes are not applied to the og table 
                                    # for that to happen we write :-
# print(df.drop('day',axis=1,inplace=True))                               
#print(df)


# we can also choose to drop multiple columns is one go :--

# df.drop(['size','sex'],axis=1,inplace=True)
# print(df)



# to drop rows we do the same but we use axis=0


# there is another way to do this :-
# we can simply write :-
# df.drop(columns='day',inplace=True)     #  it is same as df.drop('day',axis=1,inplace=True)
# and we can also use this way for other methods like deleting the columns and multiple ones 
# also remember that we use index= when choosing the rows 


# numdf=df.select_dtypes(exclude='category')
# print(numdf)



# way to get mean median mode :-

size = df['size']           # way to select a column

# print(size.mean())
# print(size.median())
# print(size.mode())








fd1 = {
    'a':[10,20,30],
    'b':['A','B','C']
}

fd2={
    'a':[40,50,60],
    'b':['X','Y','Z']
}

df1= pd.DataFrame(fd1)
df2=pd.DataFrame(fd2)

print(pd.concat([df1,df2],axis=0))      # way to add two dataframes vertically
print(pd.concat([df1,df2],axis=1))      # way to add two dataframes horizontally 
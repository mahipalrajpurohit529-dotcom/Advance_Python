import numpy as np
import pandas as pd



# data = {
#     'Name':['Aman','Rohan','Sohan','Mohan'],
#     'Subject':['Maths','Science','English','Hindi'],
#     'Marks':[90,85,88,92],
#     'Address':['Delhi','Mumbai','Kolkata','Chennai'],
#     'Maths':[50,30,66,100],
#     'English':[66,47,88,99],
#     'Science':[70,80,46,98]
# }

# df = pd.DataFrame(data)

# df['Total'] = df['Maths'] + df['English'] + df['Science']
# df['Average'] = (df['Total']/3)



# def check_pass (marks):     # defining a function
#     if(marks > 190):
#         return 'pass'
#     else:
#         return 'fail'
    

# df['Result'] = df['Total'].map(check_pass)              # way to apply a function on a column


# def check_solo_pass (marks):
#     if(marks > 40):
#         return 'pass'
#     else:
#         return 'fail'


# df['Math_result'] = df['Maths'].map(check_solo_pass)

# print(df)







# Q. check if a person is adult or child


# data = {
#     'Name' :['Mahi','Raj','Hommie'],
#     'Age' : [12,34,110]
# }

# df = pd.DataFrame(data)

# def ager (x):
#     if(x > 18):
#         return 'Adult'
#     else :
#         return 'Child'
    
# df['AdultHood'] = df['Age'].map(ager)
# df['AdultHood'] = df['Age'].map(lambda x :  "Adult" if(x>18)  else  "child")        # same as above but using lambda
# print(df)





details = {
    'Name':['Aman','Rohan','Sohan','Mohan'],
    'Subject':['Maths','Science','English','Hindi'],
    'Marks':[90,85,88,92],
    'Address':['Delhi','Mumbai','Kolkata','Chennai'],
    'Maths':[50,30,66,100],
    'English':[66,47,88,99],
    'Science':[70,80,46,98]
}

df = pd.DataFrame(details)

def total(data):
    return df['Maths'] + df['English'] + df['Science']

df['details'] = df.apply(total,axis=0)
print(df)

print(df['Maths'].max())
print(df['English'].max())
print(df['Science'].max())

print(df.iloc[:3,:2])
print(df.isna().sum())
print(df.dropna())


df['NAAM'] = df['Maths'/5]


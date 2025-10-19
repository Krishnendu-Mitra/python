"""**Computer Pandas**

This is a lib -> Numpy

Data structure :
1. Series -> 1D
2. Dataframe -> 2D

How to import pandas

pip install pandas

import pandas as pd
"""

!pip install pandas

import pandas as pd

li = [1,2,3,4]
li

# arr = [1, 2, 3, 4]

a = pd.Series([1.2, 2.5, 3.2 , 4, 5.3, 0.1])
print(a)
print(type(a))

b = pd.Series(['a', 'b', 'c', 'd'], index=[1,2,3,4])
print(b)

# Data Frame
user = pd.DataFrame({
    "name": ["Shaivasis", "Deepro", "Sunny", "Kumaresh"],
    "age": [19,20, 55,93],
    "salary": [20000, 20000, 1000, 500000]
    })

user

# read a csv file 
db = pd.read_csv("/content/property_level.csv")
db

# top 2 rows
db.head(2)

# last 7 rows
db.tail(7)

# description of that data frame
db.describe()

# meta data ofthat data frame
db.info()

db.head(3)

# read single col
db["id"]

# read multiple col
db[["id","kitchen","location"]] #col

# read single row
db.iloc[2]

db.head(4)

ab = pd.read_csv('/content/props.csv')
ab

"""
How to recover NaN data cell:
1. Loss data using drop
2. Replace data 
"""
# Loss
ab.dropna()

# Replace
ab.fillna(0)

# condition
ab[ab['location'] == 'Kolkata']

# new col introduce
ab["gst"] = [0 for i in range(len(ab))]
ab

len(ab)

# col value change
def func(price):
  return (price * 0.18) + price

ab["gst"] = ab["price"].apply(func)
ab

type(ab)
# Numpy -> Series -> DataFrame

"""**Normalization**

Student Table -> name,roll, class, age,gender,address

Marks Table -> roll, name, marks, year, class
"""

student_table = pd.DataFrame({
    "name": ["Shaivasis", "Deepro", "Sunny", "Kumaresh"],
    "age": [19,20, 55,93],
    "class": [8, 6, 7, 8],
    "roll": [1,2,3,4]
    })
student_table

# Attribute -> col
# Record -> row

marks_table = pd.DataFrame({
    "name": ["Shaivasis", "Deepro", "Sunny", "Kumaresh", "Manish"],
    "class": [8, 6, 7, 8, 4],
    "roll": [1,2,3,4, 5],
    "marks": [98, 99, 100, 24, 38]
    })
marks_table

# add table one by one
pd.concat([student_table, marks_table])

# add side by side on basis of linker
pd.merge(student_table, marks_table)


# These are some data visualizations from the titanic dataset on Kaggle
# Link and explanation of columns: https://www.kaggle.com/c/titanic

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib as mpl
import seaborn as sb


# We read our data first and look at the columns
titanic = pd.read_csv('train.csv')
titanic.head(5)

# We can also get some summary statistics from our numeric data
titanic.describe()
titanic.info()

# The sex category is pretty important and we would like to
# include it in our analysis, so we visualize it and make it numeric
# We can assign 0 to males and 1 to females
sb.factorplot('Sex', data=titanic, kind='count', palette='summer')
titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 1

# We can also fill the NAs in the age column with the median
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())

# We have some NAs in the Embarked column (the city from which people embarked)
# There are three cities: C = Cherbourg; Q = Queenstown; S = Southampton
# We first find what the unique values in this column are
# and we fill the NAs with the most frequent value
print(titanic['Embarked'].unique())
titanic['Embarked'].value_counts()

# This returns this: 'S': 644, 'C': 168, 'Q': 77
# If we would like to compute how many NAs we have as well
# we would have to create a Counter instance of the column
# The primary embarkation port was Southampton so we fill the NAs
# and then we make the column numeric
titanic['Embarked'] = titanic['Embarked'].fillna('S')
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 2

# How many females and males were in the 3 classes?
sb.factorplot('Pclass', data=titanic,hue='Sex', kind='count',palette='winter')

# We can modify our columns and create new ones as well in order to gain
# a better insight into our data. We will create a new column called 'Person'
# that will have the variables male, female and child
# We create a function to use it as the argument for the APPLY method
# This function takes the two columns AGE and SEX as arguments
# and if the number in the age column is less than 16, it returns the
# name CHILD in the PERSON column, else it just returns MALE/ FEMALE
def male_fem_child(passenger):
    age, sex = passenger
    if age<16:
        return 'child'
    else:
        return sex

titanic['Person'] = titanic[['Age', 'Sex']].apply(male_fem_child, axis = 1)

# So how many males, females and children were in the 3 classes?
sb.factorplot('Pclass',data=titanic,hue='Person', kind='count', color='orange')

# We can also create a histogram with the age distribution
titanic['Age'].hist(bins=50)



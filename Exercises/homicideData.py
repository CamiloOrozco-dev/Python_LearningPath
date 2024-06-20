import pandas as pd 

df = pd.read_csv('Files/homicide.csv')
basUrl = "https://www.kaggle.com/datasets/murderaccountability/homicide-reports?resource=download&select=database.csv"
# Explore the DataFrame's structure and content
print("Shape (rows, columns):", df.shape)
print("Total elements:", df.size)
print("Column names:", df.columns)
print("Index labels (may be row numbers):", df.index)
print("Data types of each column:", df.dtypes)

# top 5 cities with the most agencies
print(df.nlargest(5, 'Agency Code')) 
# States most affected by crimes perpetrated by women 

# States most affected by crimes perpetrated by man

# Determine the exact number of cirmens made per Asian/Pacific Islander female. 

# Expected number of Hispanics who have been killed by strangulation

# Determine the most dangerous type of relationship, which commits shotgun homicides.

# Which is the sex that has committed the most homicides with poison?

# How many black murderers did the FBI catch? 

#What is the total number of homicides from 1995 to 2000 perpetrated by black men by suffocation? 

#Determinar los homicidios de la policia de la policia municipal de la ciudad de new york que hayan sido perpetuados por ex-wife y ademas que su arma haya sido la extrangulacion 
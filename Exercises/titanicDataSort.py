import pandas as pd

df = pd.read_csv('Files/titanic.csv')

# Explore the DataFrame's structure and content
print("Shape (rows, columns):", df.shape)
print("Total elements:", df.size)
print("Column names:", df.columns)
print("Index labels (may be row numbers):", df.index)
print("Data types of each column:", df.dtypes)

# Get a glimpse of the first 10 rows
print("\nFirst 10 rows (head):")
print(df.head(10))

# Examine the last 10 rows
print("\nLast 10 rows (tail):")
print(df.tail(10))

# Access a specific row (zero-based indexing)
print("\nRow at index 147:", df.iloc[147])

# Filter rows based on a condition (odd PassengerId

print("\nRows with odd PassengerId:")
print(df[df['PassengerId'] % 2 == 1])

# Filter, select columns, and sort by Name for first-class passengers
print("\nFirst-class passengers sorted by Name (ascending):")
print(df[df['Pclass'] == 1][['Pclass', 'Name']].sort_values(by='Name'))

#Filter passengers who died and survivors.

#All passengers existed in data 
total_passengers = df.shape[0]

print("\nPercent of passengers who died")
p_died = df[df['Survived'] == 1].shape[0]
print(f"{(p_died / total_passengers )* 100:.2f}%" )

print("\nPercent of passengers who survived")
p_survived = df[df['Survived'] == 0].shape[0]
print(f"{(p_survived / total_passengers)*100:.2f}%") 

# Get the porcent who survived by each class

print("People who survived by each class")
print(df.groupby('Pclass')['Survived'].mean()*100) 

#Delete passenger with unknown age
print("\nDelete passenger with unknown age")

print("\nGet the percent of age by each class")
print(df.groupby('Pclass')['Age'].mean())

#Group females avarage Age porcent by class
print("Avarage Age percent of females by each class")
print(df [df['Sex'] == 'female'].groupby('Pclass')['Age'].mean())
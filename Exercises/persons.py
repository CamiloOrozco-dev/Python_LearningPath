# Generate Odd Numbers

import numpy as np

odd_numbers = np.arange(21, 71, 2)  # Create an array of odd numbers
print(odd_numbers)

# Filter Numbers Greater Than 35

import numpy as np

array = np.random.randint(10, 51, 20)
people_over_35 = array[array > 35]
print("Original array:", array)
print("Numbers greater than 35:", people_over_35)

# Filter Animals with Short Names

animals = ["Lion", "Tiger", "Bear", "Elephant", "Wolf"]

for animal in animals:
    if len(animal) < 4:
        print(animal)

# Filter Matrix Columns Based on Column Sum

matrix = np.random.randint(1, 10, size=(4, 4))
print(matrix)
filtered_columns = matrix[:, matrix.sum(axis=0) > 12]
print("Filtered columns:", filtered_columns)

# Select Specific Values from an Array

filter_positions = [2, 4, 6, 9, 11]
filter_values = array[filter_positions]
print("Values at positions 2, 4, 6, 9, and 11:", filter_positions)

# Filter People Based on Gender

persons = [
    ["Bob", "married", "male"],
    ["Bruno", "single", "male"],
    ["Alice", "married", "female"],
    ["Charlie", "single", "male"],
    ["Sheila", "single", "female"],
    ["Emily", "married", "female"],
    ["David", "single", "male"],
    ["Fiona", "married", "female"],
    ["Petter", "married", "male"],
    ["Anna", "single", "female"],
    ["Jack", "single", "male"],
    ["Isabella", "married", "female"],
    ["Henry", "married", "male"],
    ["Sarha", "single", "female"],
]

for persons in persons:
    if persons[2] == "female":
        print(persons)

for persons in persons:
    if persons[2] == "male":
        print(persons)

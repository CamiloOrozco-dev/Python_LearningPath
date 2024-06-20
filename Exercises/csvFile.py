import pandas as pd
import random 
import faker
import numpy as np

# Create a Faker instance for English data
fake = faker.Faker('en_EN')

# Function to generate random data for a single person
def generate_person_data():
    """Generates random data for a person, including name, surname, age, course, and grade.

    Returns:
        dict: A dictionary containing the generated data for a person.
    """
    name = fake.first_name()
    surname = fake.last_name()
    age = random.randint(15, 50)  # Use faker.randint for random integer within range
    course = random.choice(['Python', 'DotNet', 'Kafka', 'Aws', 'Jenkins', 'SQL'])
    grade = round(random.uniform(0, 5), 2)  # Round to two decimal places

    return {'Name': name + ' ' + surname, 'Age': age, 'Course': course, 'Grade': grade}

# Generate data for 200 people
data = [generate_person_data() for _ in range(200)]

# Create the DataFrame
df = pd.DataFrame(data)

# 1. Find the highest score among students 
avarage_ages =  np.mean(df['Age'])

# Print the DataFrame (optional)
print(df.to_string())
print ('The avarage age is ', avarage_ages)

# Save the DataFrame to a CSV file
file_path = 'DataPythonFile.csv'
df.to_csv(file_path, index=False)  # Don't include index column in the CSV

# 1.Calculate the avarage age
avarage_ages =  np.mean(df['Age'])
print ('The avarage age is ', avarage_ages)

# 2. Find youngers persons in table 
youngers = df[df['Age'] == df['Age'].min()][['Name','Age']]

print ('The most younger is', youngers)

# Find the oldest persons on table  
oldest = df[df['Age'] == df ['Age'].max()][['Name','Age']]

print ('The most oldesr is', oldest)

#3. the highest score among students 
higest_scores = df.sort_values('Score', ascending=False)
higest_scores.head(10)


#4. The number of people per course 

studens_per_Course_countof = df['Course'].value_counts() 
print ('The count of the studens per course is that : ', studens_per_Course_countof )
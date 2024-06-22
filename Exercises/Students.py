import pandas as pd
import random
import faker
import numpy as np

fake = faker.Faker("en_EN")


# Function to generate random data for a single person
def generate_person_data():
    name = fake.first_name()
    surname = fake.last_name()
    age = random.randint(15, 50)
    course = random.choice(["Python", "DotNet", "Kafka", "Aws", "Jenkins", "SQL"])
    grade = round(random.uniform(0, 5), 2)

    return {"Name": name + " " + surname, "Age": age, "Course": course, "Grade": grade}


# Generate data for 200 people
data = [generate_person_data() for _ in range(200)]

# Create the DataFrame
df = pd.DataFrame(data)

# 1. Find the highest score among students
avarege_ages = np.mean(df["Age"])

# Print the DataFrame (optional)
print(df.to_string())
print("The avarege age is ", avarege_ages)

# Save the DataFrame to a CSV file
file_path = "DataPythonFile.csv"
df.to_csv(file_path, index=False)

# 1.Calculate the avarege age
avarege_ages = np.mean(df["Age"])
print("The avarege age is ", avarege_ages)

# 2. Find youngers persons in table
youngers = df[df["Age"] == df["Age"].min()][["Name", "Age"]]

print("The most younger is", youngers)

# Find the oldest persons on table
oldest = df[df["Age"] == df["Age"].max()][["Name", "Age"]]

print("The most oldest is", oldest)

# 3. the highest score among students
highest_scores = df.sort_values("Score", ascending=False)
highest_scores.head(10)

# 4. The number of people per course

students_per_Course_countof = df["Course"].value_counts()
print("The count of the students per course is that : ", students_per_Course_countof)

# 5. Calculate the average score for each course
average_score_per_course = df.groupby("Course")["Grade"].mean()

# 5. Find the course with the lowest average score
course_with_lowest_average_score = average_score_per_course.idxmin()
lowest_average_score = average_score_per_course.min()

# 5. Print the course with the lowest average score and its average score
print("Course with lowest average score:", course_with_lowest_average_score)
print("Lowest average score:", lowest_average_score)

# 6. Find the course with the highest average score
course_with_highest_average_score = average_score_per_course.idxmax()
highest_average_score = average_score_per_course.max()

# 6. Print the course with the highest average score and its average score
print("Course with highest average score:", course_with_highest_average_score)
print("Highest average score:", highest_average_score)


# 7. Course with the lowest average score
course_with_lowest_average_score = average_score_per_course.idxmin()
lowest_average_score = average_score_per_course.min()
print(
    "Course with the lowest average score:",
    course_with_lowest_average_score,
    "(",
    lowest_average_score,
    ")",
)

# 8. Course with the highest average score
course_with_highest_average_score = average_score_per_course.idxmax()
highest_average_score = average_score_per_course.max()
print(
    "Course with the highest average score:",
    course_with_highest_average_score,
    "(",
    highest_average_score,
    ")",
)

# 9. Overall average score
average_score = df["Grade"].mean()
print("The overall average score:", average_score)

# 10. Number of students who passed
passed_students = df[df["Grade"] >= 3].shape[0]
print("Number of students who passed:", passed_students)

# 11. Number of students who failed
failed_students = df[df["Grade"] < 3].shape[0]
print("Number of students who failed:", failed_students)

# 12. Students in the age range of 15 to 40
age_range_students = df[(df["Age"] >= 15) & (df["Age"] <= 40)]
print("Students between the ages of 15 and 40:")
print(age_range_students)

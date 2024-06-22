import pandas as pd

# Lost file
df = pd.read_csv("")

# 1. Identify the youngest and oldest employees based on age
youngest_employee = df.loc[df["Edad"].idxmin()]
oldest_employee = df.loc[df["Edad"].idxmax()]

print("Youngest Employee:")
print(youngest_employee)

print("\nOldest Employee:")
print(oldest_employee)

# 2. Find the employees with the highest and lowest salaries
highest_paid_employee = df.loc[
    [df["Salary"].idxmax()], ["Name", "LastName", "Salary"]
]  # Get the row with the maximum salary
lowest_paid_employee = df.loc[
    [df["Salary"].idxmin()], ["Name", "LastName", "Salary"]
]  # Get the row with the minimum salary

print("\nHighest Paid Employee:")
print(highest_paid_employee)

print("\nLowest Paid Employee:")
print(lowest_paid_employee)

# 3. Filter and display employees with the job title accountant
accountants = df.loc[df["Position"] == "accountant "]
print("\nAccountants:")
print(accountants[["Name", "LastName", "Position"]])

# 4. Calculate the average salary across all records
average_salary = df["Salary"].mean()
print("\nAverage Salary of All Employees:", average_salary)

# 5. Calculate the total monthly payroll
total_employees = len(df)
monthly_payroll = average_salary * total_employees
print("\nTotal Monthly Payroll:", monthly_payroll)

# 6. Identify the top 10 highest salaries
sorted_salaries = df.sort_values(
    by="Salary", ascending=False
)  # Sort by salary in descending order
top_10_salaries = sorted_salaries.head(10)

print("\nTop 10 Highest Salaries:")
print(top_10_salaries[["Name", "LastName", "Salary"]])

# 7. Identify employees with duplicate last names (excluding duplicates based on other columns)
duplicate_last_names = df[df.duplicated(["LastName"], keep=False)]
print("\nEmployees with Duplicate Last Names:")
print(duplicate_last_names[["Name", "LastName", "Position"]])

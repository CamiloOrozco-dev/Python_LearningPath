import pandas as pd

df = pd.read_csv("/assert/files/homicide.csv")
# basUrl = "https://www.kaggle.com/datasets/murderaccountability/homicide-reports?resource=download&select=database.csv"

# Explore the DataFrame's structure and content
print("Shape (rows, columns):", df.shape)
print("Total elements:", df.size)
print("Column names:", df.columns)
print("Index labels (may be row numbers):", df.index)
print("Data types of each column:", df.dtypes)

# top 5 cities with the most agencies
city_agency_count = df.groupby("City")["Agency Code"].count().reset_index()
top_5_cities = city_agency_count.nlargest(5, "Agency Code")

print("Top 5 Cities with Most Agencies:")
print(top_5_cities)


# States most affected by crimes perpetrated by women

female_perpetrators = df[df["Perpetrator Sex"] == "Female"]
state_crime_count_female = (
    female_perpetrators.groupby("State")["Record ID"].count().reset_index()
)
top_states_female_crimes = state_crime_count_female.nlargest(5, "Record ID")

print("Top 5 States with Most Crimes Perpetrated by Women:")
print(top_states_female_crimes)

# States most affected by crimes perpetrated by man
male_perpetrators = df[df["Perpetrator Sex"] == "Male"]
state_crime_count_male = (
    male_perpetrators.groupby("State")["Record ID"].count().reset_index()
)
top_states_male_crimes = state_crime_count_male.nlargest(5, "Record ID")

print("Top 5 States with Most Crimes Perpetrated by Men:")
print(top_states_male_crimes)


# Determine the exact number of cirmens made per Asian/Pacific Islander female.
asian_pacific_islander_females = df[
    (df["Perpetrator Race"] == "Asian/Pacific Islander")
    & (df["Perpetrator Sex"] == "Female")
]
asian_pacific_islander_female_crimes = asian_pacific_islander_females.shape[0]

print(
    "Number of Crimes Committed by Asian/Pacific Islander Females:",
    asian_pacific_islander_female_crimes,
)

# Expected number of Hispanics who have been killed by strangulation
shotgun_homicides = df[df["Weapon"] == "Shotgun"]
relationship_shotgun_homicides = (
    shotgun_homicides.groupby("Relationship")["Record ID"].count().reset_index()
)

# Choose a suitable metric (e.g., homicide rate per relationship) based on your analysis goals.
# Here's an example using the total number of homicides within each relationship relative to the overall data:

total_homicides = df.shape[0]
relationship_shotgun_homicides["Homicide Rate"] = (
    relationship_shotgun_homicides["Record ID"] / total_homicides
) * 100

most_dangerous_relationship_shotgun = relationship_shotgun_homicides.nlargest(
    1, "Homicide Rate"
)

print("Most Dangerous Relationship for Shotgun Homicides (by Homicide Rate):")
print(most_dangerous_relationship_shotgun)

# Determine the most dangerous type of relationship, which commits shotgun homicides.

poison_homicides = df[df["Weapon"] == "Poison"]
sex_poison_homicides = (
    poison_homicides.groupby("Perpetrator Sex")["Record ID"].count().reset_index()
)
most_poison_homicides_sex = sex_poison_homicides.nlargest(1, "Record ID")

print("Sex that Committed the Most Homicides with Poison:")
print(most_poison_homicides_sex)

# Which is the sex that has committed the most homicides with poison?

black_murders_by_posion = df[
    (df["Perpetrator Race"] == "Black") & (df["Weapon"] == "Posion")
]
black_murders_by_posion_count = black_murders_by_posion.shape[0]

print("Number of Black Murderers Caught by Position:", black_murders_by_posion_count)

# How many black murderers did the FBI catch?

black_murders_fbi_caught = df[
    (df["Perpetrator Race"] == "Black") & (df["Record Source" == "FBI"])
]
print("Number of Black Murderers Caught by FBI:", black_murders_fbi_caught)


# What is the total number of homicides from 1995 to 2000 perpetrated by black men by suffocation?

black_men_suffocation_homicides = df[
    (df["Perpetrator Race"] == "Black")
    & (df["Perpetrator Sex"] == "Male")
    & (df["Weapon"] == "Suffocation")
    & ((df["Year"] >= 1995) & (df["Year"] <= 2000))
]
black_men_suffocation_homicides_count = black_men_suffocation_homicides.shape[0]

print(
    "Total Homicides from 1995-2000 by Black Men by Suffocation:",
    black_men_suffocation_homicides_count,
)

# What is the total number of homicides from 1995 to 2000 perpetrated by black men by suffocation?

male_perpetrators = df[df["Perpetrator Sex"] == "Male"]
state_crime_count_male = (
    male_perpetrators.groupby("State")["Record ID"].count().reset_index()
)
top_states_male_crimes = state_crime_count_male.nlargest(5, "Record ID")

print("Top 5 States with Most Crimes Perpetrated by Men:")
print(top_states_male_crimes)

# Determine new york city municipal police homicides that have been perpetrated by ex-wives and also that their weapon has been the strangulation.
asian_pacific_islander_females = df[
    (df["Perpetrator Race"] == "Asian/Pacific Islander")
    & (df["Perpetrator Sex"] == "Female")
]
asian_pacific_islander_female_crimes = asian_pacific_islander_females.shape[0]

print(
    "Number of Crimes Committed by Asian/Pacific Islander Females:",
    asian_pacific_islander_female_crimes,
)

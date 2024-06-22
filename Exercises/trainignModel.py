import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

baseUrl = "https://www.kaggle.com/datasets/javagarm/fifa-19-complete-player-dataset"
# Load the data and handle encoding
try:
    df = pd.read_csv("/content/kl.csv", index_col=0, encoding="ISO-8859-1")
except FileNotFoundError:
    print("Error: File '/content/kl.csv' not found. Please check the file path.")
    exit()

# Select features and target variable
features = [
    "Age",
    "Overall",
    "Special",
    "International Reputation",
    "Weak Foot",
    "Skill Moves",
    "Jersey Number",
    "Penalties",
    "Composure",
    "Marking",
    "StandingTackle",
    "SlidingTackle",
    "GKDiving",
    "GKHandling",
    "GKKicking",
    "GKPositioning",
    "GKReflexes",
]
X = df[features]
y = df["Potential"]

# Check for missing values
print(f"Missing values in 'Age': {df['Age'].isnull().any()}")
print(f"Missing values in 'Potential': {df['Potential'].isnull().any()}")

# Explore the relationship between Age and Potential
plt.figure(figsize=(10, 6))  # Set plot size for better visualization
plt.subplot(121)  # Create a subplot for the histogram
plt.hist2d(data=df, x="Age", y="Potential")
plt.xlabel("Age")
plt.ylabel("Potential")
plt.colorbar()
plt.subplot(122)  # Create a subplot for the scatter plot
plt.scatter(data=df, x="Age", y="Potential")
plt.xlabel("Age")
plt.ylabel("Potential")
plt.tight_layout()  # Adjust spacing between subplots
plt.show()

# Handle missing values (optional)
if df["Age"].isnull().any():
    # Impute missing values with the mean of each column (alternative methods exist)
    imputer = SimpleImputer(strategy="mean")
    X_imputed = imputer.fit_transform(X)
    # Use the imputed data for further analysis (if needed)
else:
    # No missing values detected, use original data
    X_imputed = X

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2)

# Train a Random Forest Regressor model
rf_regressor = RandomForestRegressor()
rf_regressor.fit(X_train, y_train)

# Make predictions
y_pred = rf_regressor.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = rf_regressor.score(X_test, y_test)

print("Random Forest Mean Squared Error (with imputation): ", mse)
print("Random Forest R2 Score (with imputation): ", r2)

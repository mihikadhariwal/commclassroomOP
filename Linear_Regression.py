import pandas as pd
import numpy as np
import faker
from faker import Faker
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Initialize Faker
fake = Faker()
# Generate synthetic data
data = []
for _ in range(100000):
    experience = fake.random_int(min=0, max=40)
    designation = experience * 2000 + fake.random_int(min=-1000, max=1000)
    salary = experience * 3000 + fake.random_int(min=-2000, max=2000)
    publications = experience * 5 + fake.random_int(min=-3, max=3)
    book_chapters = experience * 2 + fake.random_int(min=-2, max=2)
    consultancy_work = experience * 1000 + fake.random_int(min=-500, max=500)
    fund_received = experience * 5000 + fake.random_int(min=-3000, max=3000)
    professional_membership = experience * 50 + fake.random_int(min=-20, max=20)

    data.append([experience, designation, salary, publications, book_chapters, consultancy_work, fund_received, professional_membership])

# Convert data to DataFrame
columns = ['Experience', 'Designation', 'Salary', 'Publications', 'Book_Chapters', 'Consultancy_Work', 'Fund_Received', 'Professional_Membership']
df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV
df.to_csv('faculty_data.csv', index=False)

# Function to read CSV file and load into list
def read_csv_to_list(file_path):
    data = pd.read_csv(file_path)
    return data.values.tolist()

# Read CSV file and load into list
faculty_data = read_csv_to_list('faculty_data.csv')

# Convert the list into DataFrame
faculty_df = pd.DataFrame(faculty_data, columns=columns)

# Find correlation among the fields in the faculty dataset
correlation = faculty_df.corr()

print("Correlation Matrix:")
print(correlation)

# Perform linear regression analysis
X = faculty_df['Experience'].values.reshape(-1, 1)
y = faculty_df['Designation'].values

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict values
predicted_values = model.predict(X)

# Plot predicted values
plt.scatter(X, y, color='blue')
plt.plot(X, predicted_values, color='red')
plt.title('Linear Regression - Experience vs Designation')
plt.xlabel('Experience')
plt.ylabel('Designation')
plt.show()


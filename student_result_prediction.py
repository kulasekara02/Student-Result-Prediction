import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Example data (replace this with real data later)
# Columns: ['Attendance', 'Assignment_Score', 'Quiz_Score', 'Past_Performance', 'Result']
data = {
    'Attendance': [85, 75, 60, 90, 70, 55, 95, 80, 50, 65],
    'Assignment_Score': [80, 70, 60, 90, 75, 50, 95, 85, 45, 60],
    'Quiz_Score': [75, 65, 55, 85, 70, 45, 90, 80, 40, 55],
    'Past_Performance': [88, 78, 68, 92, 76, 54, 97, 84, 49, 62],
    'Result': [1, 1, 0, 1, 1, 0, 1, 1, 0, 0]  # 1 = Pass, 0 = Fail
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target variable
X = df[['Attendance', 'Assignment_Score', 'Quiz_Score', 'Past_Performance']]
y = df['Result']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict for a new student
new_student = np.array([[80, 75, 70, 85]])  # Example: [Attendance, Assignment_Score, Quiz_Score, Past_Performance]
prediction = model.predict(new_student)
result = "Pass" if prediction[0] == 1 else "Fail"
print(f"Prediction for the new student: {result}")


# Import necessary libraries
from sklearn.datasets import load_iris  # For loading the Iris dataset
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.ensemble import RandomForestClassifier  # Random Forest model
from sklearn.metrics import accuracy_score  # For evaluating the model
import joblib  # For saving the trained model

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features: Sepal length, Sepal width, Petal length, Petal width
y = iris.target  # Target: Flower species (0: Setosa, 1: Versicolor, 2: Virginica)

# Split the dataset into training and testing sets
# 80% of the data is used for training, and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier
# Random Forest is a robust ensemble learning method
model = RandomForestClassifier(n_estimators=100, random_state=42)  # 100 trees in the forest
model.fit(X_train, y_train)  # Train the model with the training data

# Evaluate the model's performance
y_pred = model.predict(X_test)  # Predict the test set results
accuracy = accuracy_score(y_test, y_pred)  # Calculate the accuracy of predictions
print(f"Model Accuracy: {accuracy * 100:.2f}%")  # Display the accuracy

# Export the trained model to a joblib file
# joblib format efficiently stores complex objects like machine learning models
joblib.dump(model, "iris_model1.joblib")
print("Model exported as iris_model.joblib")

# Code ends here

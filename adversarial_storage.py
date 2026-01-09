# Adversarial Storage and Management Index Regression Modeling

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Sample data generation
def generate_data(num_samples):
    X = np.random.rand(num_samples, 1) * 10  # Features
    y = 2.5 * X + np.random.randn(num_samples, 1) * 2  # Target with noise
    return X, y

# Data preparation
X, y = generate_data(100)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Visualization
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.title('Adversarial Storage and Management Index Regression')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("train.csv")

print("First 5 rows:\n", df.head())

# Select useful columns
df = df[['GrLivArea', 'BedroomAbvGr', 'Neighborhood', 'SalePrice']]

# Drop missing values
df = df.dropna()

# Features & target
X = df[['GrLivArea', 'BedroomAbvGr', 'Neighborhood']]
y = df['SalePrice']

# Preprocessing
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['Neighborhood'])
], remainder='passthrough')

# Model pipeline
model = Pipeline([
    ('preprocessing', preprocessor),
    ('regression', LinearRegression())
])

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("\nR2 Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

# Test prediction
sample = pd.DataFrame({
    'GrLivArea': [1500],
    'BedroomAbvGr': [3],
    'Neighborhood': ['NAmes']
})

pred = model.predict(sample)
print("\nPredicted Price:", pred[0])
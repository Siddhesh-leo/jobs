import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('IRIS.csv')


X = df.drop(columns=['species']) 
y = df['species'] 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

results_df = X_test.copy()
results_df['Actual_Species'] = y_test
results_df['Predicted_Species'] = predictions

results_df['Correct_Prediction?'] = results_df['Actual_Species'] == results_df['Predicted_Species']


print(results_df.to_string())
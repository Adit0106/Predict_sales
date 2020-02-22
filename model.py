import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

df = pd.read_csv('sales.csv')
df['rate'].fillna(0, inplace=True)
df['sales_in_first_month'].fillna(df['sales_in_first_month'].mean(), inplace=True)
df['sales_in_second_month'].fillna(df['sales_in_second_month'].mean(), inplace=True)

X = df.iloc[:, :3]
y = df.iloc[:, -1]

model = LinearRegression()
model.fit(X, y)
pickle.dump(model, open('model.pkl', 'wb'))

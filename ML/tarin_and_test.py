import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("py_first_ripo/ML/carprices_test.csv")
# print(df)
plt.scatter(df["Mileage"], df["Sell Price($)"])
# plt.show()

plt.scatter(df["Age(yrs)"], df["Sell Price($)"])
# plt.show()

x = df[["Mileage", "Age(yrs)"]]
y = df["Sell Price($)"]

# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression()

model.fit(x_train, y_train)

pred = model.predict(pd.DataFrame(x_test))
print(pred)

print(y_test)

print(model.score(x_test, y_test))

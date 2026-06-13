import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("py_first_ripo/ML/homeprices_dummy.csv")
# print(df)

dummies = pd.get_dummies(df.town)
# print(dummies)

merged = pd.concat([df, dummies], axis="columns")
# print(merged)

final = merged.drop(["town", "west windsor"], axis="columns")
# print(final)

model = LinearRegression()

x = final.drop("price", axis="columns")
# print(x)

y = final.price
# print(y)

model.fit(x, y)

# both are same but diff method
# pred = model.predict([[2800, 0, 1]])
# print(pred)

pred1 = model.predict(
    pd.DataFrame({"area": [2800], "monroe township": [0], "robinsville": [1]})
)
print(pred1)

# pred2 = model.predict([[3400, 0, 0]])
# print(pred2)

# pred3 = model.predict([[3400, 0, 1]])
# print(pred3)

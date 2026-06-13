import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("py_first_ripo/ML/carprices.csv")
# print(df)

dummis = pd.get_dummies(df["Car Model"])
# print(dummis)

merged = pd.concat([df, dummis], axis="columns")
# print(merged)

final = merged.drop(["Car Model", "Mercedez Benz C class"], axis="columns")
# print(final)

model = LinearRegression()

x = final.drop("Sell Price($)", axis="columns")
# print(x)

y = final["Sell Price($)"]
# print(y)

model.fit(x, y)

# that both are correct
pred1 = model.predict(
    pd.DataFrame({"Mileage": [45000], "Age(yrs)": [4], "Audi A5": [0], "BMW X5": [0]})
)
print(pred1)

pred2 = model.predict(pd.DataFrame([[86000, 7, 0, 1]]))
print(pred2)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("py_first_ripo/ML/canada_per_capita_income.csv")
# print(df.head(5))
reg = linear_model.LinearRegression()
reg.fit(df[["year"]], df["per capita income (US$)"])
prediction = reg.predict(pd.DataFrame({"year": [2012]}))
print(f"the prediction is {prediction}")

# %matplotlib inline
plt.xlabel("year")
plt.ylabel("per capita income (US$)")
plt.scatter(df["year"], df["per capita income (US$)"], color="red", marker="+")
plt.plot(df.year, reg.predict(df[["year"]]), color="blue")
plt.show()


print(reg.coef_)
print(reg.intercept_)

print(828.46507522 * 2012 + -1632210.7578554575)

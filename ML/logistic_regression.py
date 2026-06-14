import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("py_first_ripo/ML/insurance_data.csv")
# print(df)


plt.scatter(df.age, df.bought_insurance, marker="+", color="red")
# plt.show()

x_train, x_test, y_train, y_test = train_test_split(
    df[["age"]], df.bought_insurance, test_size=0.1
)
print(x_test)
# print(x_train)

modle = LogisticRegression()
modle.fit(x_train, y_train)

pred = modle.predict(x_test)
print(pred)

print(modle.score(x_test, y_test))

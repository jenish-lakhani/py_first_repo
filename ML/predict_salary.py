import pandas as pd
import numpy as np
from sklearn import linear_model
from word2number import w2n
import math

df = pd.read_csv("py_first_ripo/ML/hiring.csv")
# print(df)

mean = math.floor(df["test_score(out of 10)"].mean())
print(mean)
df["test_score(out of 10)"] = df["test_score(out of 10)"].fillna(mean)
# print(df)

df["experience"] = df["experience"].fillna("zero")
# print(df)

df["experience"] = df["experience"].apply(w2n.word_to_num)
# print(df)

reg = linear_model.LinearRegression()
reg.fit(
    df[["experience", "test_score(out of 10)", "interview_score(out of 10)"]],
    df["salary($)"],
)


predict_salary1 = reg.predict(
    pd.DataFrame(
        {
            "experience": [2],
            "test_score(out of 10)": [9],
            "interview_score(out of 10)": [6],
        },
    )
)

predict_salary2 = reg.predict(
    pd.DataFrame(
        {
            "experience": [12],
            "test_score(out of 10)": [10],
            "interview_score(out of 10)": [10],
        }
    )
)

print(math.floor(predict_salary1[0]))
print(math.floor(predict_salary2[0]))

# print(reg.coef_)
# print(reg.intercept_)
# print(2812.95487627 * 7 + 1845.70596798 * 9 + 2205.24017467 * 6 + 17737.263464337688)

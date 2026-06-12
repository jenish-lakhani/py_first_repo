import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle

df = pd.read_csv("py_first_ripo/ML/homeprices.csv")
# print(df)

model = linear_model.LinearRegression()
model.fit(df[["area"]], df.price)

coef = model.coef_
intercept = model.intercept_

# print(coef)
# print(intercept)

# both are correct ignore the warning
# print(modle.predict([[3300]]))
print(model.predict(pd.DataFrame({"area": [3300]})))

with open("py_first_ripo/ML/model_pickle", "wb") as f:
    pickle.dump(model, f)

with open("py_first_ripo/ML/model_pickle", "rb") as f:
    mp = pickle.load(f)

print(mp.predict(pd.DataFrame({"area": [5000]})))


# the both are same but jo tamari pase file ma large numpy array hoy data hoy to joblib better 6 ena mate
import joblib

joblib.dump(model, "py_first_ripo/ML/model_joblib")
mj = joblib.load("py_first_ripo/ML/model_joblib")
print(mj.predict(pd.DataFrame({"area": [5000]})))

import numpy as np
import pandas as pd
import math
from sklearn.linear_model import LinearRegression


def predict_using_sklean():
    df = pd.read_csv("py_first_ripo/ML/test_scores.csv")
    r = LinearRegression()
    r.fit(df[["math"]], df.cs)
    return r.coef_, r.intercept_


def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.02
    cost_previous = 0

    for i in range(iterations):
        y_pred = m_curr * x + b_curr
        cost = (1 / n) * sum([val**2 for val in (y - y_pred)])
        md = -(2 / n) * sum(x * (y - y_pred))
        bd = -(2 / n) * sum(y - y_pred)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        print(f"m {m_curr} , b {b_curr} , cost {cost}")
    return m_curr, b_curr


if __name__ == "__main__":
    df = pd.read_csv("py_first_ripo/ML/test_scores.csv")
    x = np.array(df.math)
    y = np.array(df.cs)

    m, b = gradient_descent(x, y)
    print("Using gradient descent function: Coef {} Intercept {}".format(m, b))

    m_sklearn, b_sklearn = predict_using_sklean()
    print("Using sklearn: Coef {} Intercept {}".format(m_sklearn, b_sklearn))

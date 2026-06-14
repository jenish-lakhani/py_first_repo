#  avoid all the error the code will work

import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

digits = load_digits()

# print(digits.data[0])

plt.gray()
for i in range(5):
    plt.matshow(digits.images[i])
# plt.show()

# print(digits.target[0])

x_train, x_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.2
)

# print(len(x_train))

model = LogisticRegression()
model.fit(x_train, y_train)

# print(model.score(x_test, y_test))

plt.matshow(digits.images[67])
# plt.show()
# print(digits.target[67])

pred = model.predict([digits.data[67]])
# print(pred)

y_predicted = model.predict(x_test)
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_predicted)
# print(cm)


import seaborn as sn

plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True)
plt.xlabel("Predicted")
plt.ylabel("Truth")
plt.show()

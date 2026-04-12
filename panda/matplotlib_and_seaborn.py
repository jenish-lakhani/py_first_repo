import pandas as pd

df_salse = pd.read_excel(
    "C:/Python_AI/py_first_ripo/panda/chapter_3_assets/8_matplotlib_seaborn/linechart.xlsx"
)

# print(df_salse.head())
# print(df_salse)

from matplotlib import pyplot as plt

# ****************** chart plot *******************

#  aanathi chart banse plt show thi te dekhase
# print(plt.plot(df_salse["Quarter"], df_salse["Fridge"], color="green", label="Fridge"))
# width ane height set karse
# print(plt.figure(figsize=(12, 4)))
# aama color red hase
# print(plt.plot(df_salse["Quarter"], df_salse["Dishwasher"], color="red", label="Dishwasher"))
# print(plt.plot(df_salse["Quarter"],df_salse["Washing Machine"],color="yellow",label="fridge",))

# title ma batvse
# print(plt.title("Product Sales"))
# x ax any y ax pr aa batavse
# print(plt.ylabel("revenue(min $)"))
# print(plt.xlabel("financial quarter"))

# aanathi top right khuna ma legend aai jase jenathi khabr pade ke aa line koni 6
# print(plt.legend())
# print(plt.show())

# ****************** circle chart ****************

total_salse = df_salse[["Fridge", "Dishwasher", "Washing Machine"]].sum()
# print karse total salse
# print(total_salse)

print(total_salse.index)

# banne same j 6 burt type ni error aavtiti ne etle biji rit elakhyu
# print(plt.pie(total_salse, labels=total_salse.index))
# print(plt.pie(total_salse, labels=list(total_salse.index)))

# aa autopct thi circle ma 5 ma batavse
# print(plt.pie(total_salse, labels=list(total_salse.index), autopct="%1.1f%%"))

# aanathi explode thi value pramane 1 li 6 te thoduk durthai jase vartul thi
# print(plt.pie(total_salse,labels=list(total_salse.index),autopct="%1.1f%%",explode=(0.1, 0, 0)))

# shadow thi shadow aavse circle ma
# print(plt.pie(total_salse,labels=list(total_salse.index),autopct="%1.1f%%",explode=(0.1, 0, 0),shadow=True,))

# aa startangle etle 140 degree na angle thii chalu thase circle
# print(plt.pie(total_salse,labels=list(total_salse.index),autopct="%1.1f%%",explode=(0.1, 0, 0),shadow=True,startangle=140,))

# print(plt.show())


# ********* bar chart ***************

# aanthi bar chart aavse
# print(df_salse.plot(kind="bar", x="Quarter"))

# aanathi x bar vali value 45 degree vali jase
# print(plt.xticks(rotation=45))

# quarter ne set karyu 6 index ma
df_salse_2 = df_salse.set_index("Quarter")
# print(df_salse_2)

# aakhi row ne access kari sakiye print kari shakiye
# print(df_salse_2.loc["Q1 2022"])


# print(plt.show())


# ********** histogram **************

df_score = pd.read_excel(
    "C:/Python_AI/py_first_ripo/panda/chapter_3_assets/8_matplotlib_seaborn/histograms.xlsx"
)
# print(df_score)

# aanathi histogram show thsae
# print(plt.hist(df_score["Exam_Score"]))

import seaborn as sns

# banne same j 6  seaborn use karvathi border doreli aai jase
# print(sns.histplot(df_score["Exam_Score"]))
# print(sns.histplot(data=df_score, x="Exam_Score"))

# kde thi line doreli aai jase chart ma
# print(sns.histplot(data=df_score, x="Exam_Score", kde=True))

# print(plt.xlabel("Score"))
# print(plt.ylabel("count"))
# print(plt.title("Exam Scores"))

# same uper ni jem j 6 aa biji rit 6
# print(sns.histplot(data=df_score, x="Exam_Score", kde=True))
# print(plt.show())


# **************** scatter plut **************

df = pd.read_excel(
    "C:/Python_AI/py_first_ripo/panda/chapter_3_assets/8_matplotlib_seaborn/scatter_plot.xlsx"
)
# print(df)

print(sns.scatterplot(data=df, x="area_square_ft", y="price"))
print(plt.show())

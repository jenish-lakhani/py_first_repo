import pandas as pd

df = pd.read_csv("C:/Python_AI/py_first_ripo/panda/chapter_3_assets/1_intro/movies.csv")
# print(df)

# ketli rows ane column 6 ebatavse
# print(df.shape)

# column name print karse
# print(df.columns)

# banne ma same j output aavse , ketli industry 6 e batavse name
# print(df.industry.unique())
# print(df["industry"].unique())

# aa language batavse kai 6 ketli 6
# print(df.language.unique())

# count batavse kai 6 ketli 6
# print(df.industry.value_counts())
# print(df.language.value_counts())

# khali  aatlij columnn batavse
# df_new = df[["title", "imdb_rating", "industry"]]
# print(df_new)

# aa release year 2000 ane 2010 vachhe ketli movie 6 batavse
# print(df[(df.release_year >= 2000) & (df.release_year <= 2010)])

# aama studio marvel hase e badhi moovie batavsse
# print(df[df.studio == "Marvel Studios"])

# aa badha numaric statics batavse min,max,mean,std etc
# print(df.describe())

# info batavse
# print(df.info())

# aa max rating valu ane min rating valu banne movie print karse
# print(
#     df[
#         (df.imdb_rating == df.imdb_rating.max())
#         | (df.imdb_rating == df.imdb_rating.min())
#     ]
# )

# aa navi column banavse age namni ane ema 2026 - release_year kari n value print karse
# df["age"] = df["release_year"].apply(lambda x: 2026 - x)
# print(df["age"])
# print(df)

# aa be column maline eknavi column banavse  revenue mathi budgete bad karse ane profit ni navi column banse
# df["profit"] = df.apply(lambda x: x["revenue"] - x["budget"], axis=1)
# print(df)

# index batavse ketli 6 start, stop, step
# print(df.index)

# aa title ne index banavse , ane inplace true karvu pade toj original data ma change thase nkr nai thai
df.set_index("title", inplace=True)
# print(df)

# aa aakhi row print karse pather vali , loc etle e ek location or lable based index 6
# print(df.loc["Pather Panchali"])

# iloc index based location 6
# print(df.iloc[2:6])

# aanathi index ma karela ferfar reset thai jase
df.reset_index(inplace=True)
print(df)

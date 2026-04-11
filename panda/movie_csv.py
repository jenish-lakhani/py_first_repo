import pandas as pd

df = pd.read_csv("C:/Python_AI/py_first_ripo/panda/movies.csv")
# print(df)

# aanathi aagal ni 6 line j print thase
# print(df.head(6))

# aanathi pachhal ni 3 line print thase
# print(df.tail(3))

# randomely 4 line print karse
# print(df.sample(4))

# 2 thi 5 sudhi print kar se
# print(df[2:6])

# shape batavse ketli row 6 ane ketli column
# print(df.shape)

# imdb_rating column print karse
# print(df.imdb_rating)

# min value print karse
# print(df.imdb_rating.min())

# max value print karse
# print(df.imdb_rating.max())

# avg value print karse
# print(df.imdb_rating.mean())

# bollywood movies print karse
# print(df[df.industry == "Bollywood"])

# hollywood movies print karse
# print(df[df.industry == "Hollywood"])

df_b = df[df.industry == "Bollywood"]
df_h = df[df.industry == "Hollywood"]

# aa bollywood movies ni min max ane avg print karse
# print(df_b.imdb_rating.min())
# print(df_b.imdb_rating.max())
# print(df_b.imdb_rating.mean())

# aa hollywood movies ni min max ane avg print karse
# print(df_h.imdb_rating.min())
# print(df_h.imdb_rating.max())
# print(df_h.imdb_rating.mean())

# aa badhii movie ni min max ane avg print karse
print(
    "all movev: min = ",
    df.imdb_rating.min(),
    "max = ",
    df.imdb_rating.max(),
    "avg = ",
    df.imdb_rating.mean(),
)

# aa badhi bollywood movie ni min max ane avg print karse
print(
    "bollywood movie min = ",
    df_b.imdb_rating.min(),
    "max = ",
    df_b.imdb_rating.max(),
    "avg = ",
    df_b.imdb_rating.mean(),
)

# aa badhi hollywood movie ni min max ane avg print karse
print(
    "hollywood movie min = ",
    df_h.imdb_rating.min(),
    "max = ",
    df_h.imdb_rating.max(),
    "avg = ",
    df_h.imdb_rating.mean(),
)

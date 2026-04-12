import pandas as pd

df = pd.read_csv(
    "C:/Python_AI/py_first_ripo/panda/chapter_3_assets/6_group_by/weather_by_cities.csv"
)
# print(df)

# new york vali city aavse badhi
# print(df[df.city == "new york"])

# max temperature new york city aavse
# print(df[df.city == "new york"].temperature.max())

# city wise group banavi dese
g = df.groupby("city")
# for city, data in g:
#     print("city:", city)
#     print("data:", data)#.temperature.max())

# print mumbai city valu group
# print(g.get_group("mumbai"))

# indivisual min ane max and mean badha group mathui batavse
# print(g.max())
# print(g.min())
# print(g.mean())

# badha statics batavse
# print(g.describe())

# sizebatavse
# print(g.size())


# group karine aapse 80-90 vachhe ane evi rite bija badha
def grouper(df, idx, col):
    if 80 <= df[col].loc[idx] <= 90:
        return "80-90"
    elif 50 <= df[col].loc[idx] <= 60:
        return "50-60"
    else:
        return "others"


g = df.groupby(lambda idx: grouper(df, idx, "temperature"))

for key, d in g:
    print("key : ", key)
    print("data :", d)

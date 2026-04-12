import pandas as pd

india_weather = pd.DataFrame(
    {
        "city": ["mumbai", "delhi", "banglore"],
        "temperature": [32, 45, 30],
        "humidity": [80, 60, 78],
    }
)

us_weather = pd.DataFrame(
    {
        "city": ["new york", "chicago", "orlando"],
        "temperature": [21, 14, 35],
        "humidity": [68, 65, 75],
    }
)
# print(india_weather)
# print(us_weather)

# aanathi concat thase banne ane ignore index thi aa table ni index ignore karse ane pote j sarkhi index aapi dese
df = pd.concat([india_weather, us_weather], ignore_index=True)
# print(df)

#  kaey batavse indai ane us banne na table ni aagal
df = pd.concat([india_weather, us_weather], keys=["india", "us"])
# print(df)

#  aanathi khaliindia ni j city aavse
# print(df.loc["india"])

temperature_df = pd.DataFrame(
    {
        "city": ["mumbai", "delhi", "banglore"],
        "temperature": [32, 45, 30],
    },
    index=[0, 1, 2],
)
windspeed_df = pd.DataFrame(
    {
        "city": ["delhi", "mumbai"],
        "windspeed": [
            6,
            7,
        ],
    },
    index=[1, 0],
)
# print(temperature_df)
# print(windspeed_df)

# merge kari dese banne ne
# df1 = pd.concat([temperature_df, windspeed_df], axis=1)
# print(df1)

df1 = city_temp = pd.DataFrame(
    {"city": ["mumbai", "delhi", "banglore"], "temperature": [32, 45, 37]}
)
df2 = city_humidity = pd.DataFrame(
    {"city": ["delhi", "mumbai", "surat"], "humidity": [68, 65, 69]}
)

# city pramane merge kari dese data ne
# df3 = pd.merge(df1, df2, on="city")
# print(df3)

# inner join
df3 = pd.merge(df1, df2, on="city", how="inner")
# left join
df4 = pd.merge(df1, df2, on="city", how="left")
# right join
df5 = pd.merge(df1, df2, on="city", how="right")
# outer join means all
df6 = pd.merge(df1, df2, on="city", how="outer")
print(df3)
print(df4)
print(df5)
print(df6)

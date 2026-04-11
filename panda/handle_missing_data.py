import pandas as pd

df = pd.read_csv(
    "C:/Python_AI/py_first_ripo/panda/chapter_3_assets/4_handling_missing_data_fillna_dropna_interpolate/weather_data.csv",
    # parse_dates etle day column ne datetime ma convert thai jase ene proper date tarike lese
    parse_dates=["day"],
)
# print(df)

# print(type(df.day[0]))

# day ne index tarike lese
df.set_index("day", inplace=True)
# print(df)

df.fillna(
    {
        "temperature": df.temperature.mean(),
        "windspeed": df.windspeed.mean(),
        "event": "no event",
    },
    inplace=True,
)
# print(df)

# aanathi andajo lagavi ne null value fill kari dese
# pan aama aa chalyu nathi error aave 6
# df.interpolate()
# print(df)

# thresh ema valueaapvani ke aapne ketle nan,null value joie 6
# df.dropna(thresh=2)
# print(df)

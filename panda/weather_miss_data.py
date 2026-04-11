import pandas as pd
import numpy as np

df = pd.read_csv(
    "C:/Python_AI/py_first_ripo/panda/chapter_3_assets/5_handling_missing_data_replace/weather_data.csv"
)
# print(df)

# aanathi -99999 ne 0 ma convert thai jase
# df.replace(-99999, 0, inplace=True)
# print(df)

# aanathi banne value ni jagyaye nan aavi jase
# df.replace([-99999, -88888], np.nan, inplace=True)
# print(df)


# aama je column ma aapeli value hase te nan ma feri jase
# df.replace(
#     {
#       "temperature": -99999,
#       "windspeed": [-99999, -88888],
#       "event": "no event"},
#     np.nan,
#     inplace=True,
# )
# print(df)


# aanathi pn value change thai jase nan ma
# df.replace(
#     {
#         -99999: np.nan,
#         -88888: np.nan,
#         "no event": "Sunny",
#     },
#     inplace=True,
# )
# print(df)


df = pd.DataFrame(
    {
        "score": ["poor", "average", "good", "exceptional"],
        "student": ["rob", "maya", "parthiv", "tom"],
    }
)

# aa score ne 1,2,3,4 ma fervi dese etle ke poor ete 1 score ,average etle 2 evi rite
df.replace(["poor", "average", "good", "exceptional"], [1, 2, 3, 4], inplace=True)
print(df)

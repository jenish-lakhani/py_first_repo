import pandas as pd

df_movies = pd.read_excel(
    "C:/Python_AI/py_first_ripo/panda/chapter_3_assets/3_read_write_to_excel/movies_db.xlsx"
)
# print(df_movies)


# aa func thi jya jya $ ane dollars lakhel hase tya usd thai jase
# converters func no use karyo 6 aama
def stand_currency(curr):
    if curr == "$$" or curr == "Dollars":
        return "USD"
    return curr


df_financials = pd.read_excel(
    "C:/Python_AI/py_first_ripo/panda/chapter_3_assets/3_read_write_to_excel/movies_db.xlsx",
    sheet_name="financials",
    converters={"currency": stand_currency},
)

# print(df_financials)

df_merged = pd.merge(df_movies, df_financials, on="movie_id")
# print(df_merged)

# merged kari dese banne ne
df_merged.to_excel(
    "C:/Python_AI/py_first_ripo/panda/chapter_3_assets/3_read_write_to_excel/movies_db_final.xlsx",
    sheet_name="merged",
    index=False,
)
# print(df_merged)


df_stocks = pd.DataFrame(
    {
        "tickers": ["GOOGL", "WMT", "MSFT"],
        "price": [845, 64, 64],
        "pe": [30.37, 14.26, 30.97],
        "eps": [27.82, 4.61, 2.12],
    }
)

# print(df_stocks)


df_weather = pd.DataFrame(
    {
        "day": ["1/1/2017", "1/2/2017", "1/3/2017"],
        "temperature": [32, 35, 28],
        "event": ["Rain", "Sunny", "Snow"],
    }
)

# print(df_weather)

# aanathi navi xslr file banse
with pd.ExcelWriter("stocks_weather.xlsx") as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")

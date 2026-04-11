import pandas as pd

# aa skiprows thi 1 row skip kari dw se
# header nakki kare ke kai line ne header banavvi ane name= kari ne column na name fervvi shakie chhie
df = pd.read_csv(
    "C:/Python_AI/py_first_ripo/panda/chapter_3_assets/3_read_write_to_excel/stock_data.csv",
    skiprows=1,
    header=1,
    names=["stock_symbol", "eps", "revenue", "price", "people"],
    # aanathi khali peli 2 j row batavse
    # nrows=2,
    # banne rite lakhi sakay
    # na_values={"eps": ["not available"], "revenue": ["-1"]},
    na_values=["not available", "-1", "n.a"],
)
# print(df)

df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["eps"] = pd.to_numeric(df["eps"], errors="coerce")
df["pe"] = df["price"] / df["eps"]
# print(df)

# aanathi te original ma add thai jase
df.to_csv("pe.csv", index=False)
print(df)

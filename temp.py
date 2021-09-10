import pandas as pd

pd.set_option('display.max_columns', 25)
df = pd.read_pickle("assets/df_personal.pkl")

print(df.head(20))
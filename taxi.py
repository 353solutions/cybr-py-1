#%% 
import pandas as pd


# df is short for DataFrame
df = pd.read_parquet('yellow_tripdata_2020-03.parquet')

print(f'len: {len(df):,}')

# 43MB on disk, 457MB in memory
print(df.memory_usage().sum() / 1_000_000)

# %%
df.describe()
# %%
df.columns
# %%
df['passenger_count']  # Column access, pd.Series
# %%
df.dtypes  # dtype -> data type
# %%
%timeit 2 ** 1000
# %%
n = df['VendorID'][1] 
# %%
%timeit n ** 1000  # np.int64(0), machine level
# %%
df.loc[0]  # Row access, slower than column access
# %%
cart = ['milk', 'bread', 'butter', 'lemon']
cart[1:3]

#%%
df['VendorID'][:10]
# %%
df[:5]  # rows

# %%
df.sample(5)

# %% Boolean Indexing

s = pd.Series([1, 2, 3, 4, 5, 6, 7])
s > 3

# %%
mask = s > 3
s[mask]

# %%
s[s > 3]

# [n for n in s if n > 3]

# %%
s[(s > 3) & (s < 6)]

# %%
s[(s < 3) | (s > 5)]
# %%
s[~(s>5)]
# %%
s[s < 6]
# %%
# Combining masks:
# - and: &
# - or : |
# - not: ~
# Must has () around conditions

# %% Exercise: How many rides have more than a single passenger?

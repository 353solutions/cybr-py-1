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

# %% Exercise: How many rides have more than a single 
# passenger?
col = df['passenger_count']
mask = col > 1
num_multi_rides = len(col[mask])
print(f'more than 1 passenger: {num_multi_rides:,}')
# %%
len(
      # col                      # mask
    df['passenger_count'][df['passenger_count'] > 1]
)

# %%
df['passenger_count'].max()
# %%
df['passenger_count'].min()
# %%
df['passenger_count'].describe()
# describe count is all the non-Nan values
# %%
len(df['passenger_count'])  # With NaN
# %%
df['passenger_count'].count()  # Without NaN

# %%
import numpy as np

s = pd.Series([1, np.nan, 2])
print(s)

# %%
s.fillna(s.mean())  # fillna return a new series

# %%
s.fillna(s.mean(), inplace=True)
s

# See also ffill

# %% Calculate the average speed

s1 = pd.Series([1,2,3])
s2 = pd.Series([10,20,30])
s1 + s2
# %%
s1 + 7  # broadcasting

# %%
duration = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
duration.describe()

# %%

t = df['tpep_dropoff_datetime'][0]
# %%
df['tpep_dropoff_datetime'].min() # 2008-12-31...
# %%
# GIGO: Garbage In, Garbage Out

# This will fail
# df['tpep_dropoff_datetime'].year

# To access specific non-numeric attributes use:
# - dt for Timestamp (e.g. df['date'].dt.year)
# - str for string methods (e.g. df['name'].str.lower)
# - cat for categorical data
# %%
df['tpep_dropoff_datetime'].dt.year.unique()

# %%
mask = (
    (df['tpep_dropoff_datetime'].dt.year == 2020) &
    (df['tpep_pickup_datetime'].dt.year == 2020) &
    (df['tpep_dropoff_datetime'] > df['tpep_pickup_datetime'])
)
df2020 = df[mask]
len(df2020)

# %%
duration = df2020['tpep_dropoff_datetime'] - df2020['tpep_pickup_datetime']
duration.describe()

# You can add a column to the dataframe
# df['duration'] = df['tpep_dropoff_dateteime'] - df['tpep_pickup_datetime']
# %%
duration_hours = duration / pd.Timedelta('1h')
# df2020['trip_distance'] / duration  # error, need unit
speeds = df2020['trip_distance'] / duration_hours
speeds.median()

# %%
d = duration[0]
d / pd.Timedelta('1h')
# %% Exercise: Time wasted
# We say that time wasted is the duration of a ride
# multiplied by number of passengers
# What is the maximal wasted time?
(duration * df2020['passenger_count']).max()
# %%
df2020.loc[duration.idxmax()]
# %%

df['VendorID'].unique()


# %%
vendor_names = {
    1: 'Creative',
    2: 'Curb',
    5: 'Helix', # 7 in the schema?
    6: 'Myle',
}
df['vendor_name'] = df['VendorID'].map(vendor_names)
df['vendor_name'][:10]
# %%
df['VendorID'].memory_usage(deep=True) / 1_000_000  # 24

# %%
df['vendor_name'].memory_usage(deep=True) / 1_000_000  # 163

# %% Categorical data: small number of values that repeat (age, gender ...)
df['vendor'] = df['vendor_name'].astype('category')
df['vendor'][:10]


# %%

df['vendor'].memory_usage(deep=True) / 1_000_000  # 3
# %%
df.memory_usage(deep=True).sum() / 1_000_000
# %%
len(df[df['vendor'] == 'Creative'])
# %%
df['vendor'].value_counts()

# %%
df['VendorID'].value_counts()

# %%
df.nunique()  # How many unique values per column
# %%

# group by:
# - sort rows in group (bucket) by criteria (column name or a series of values)
# - run aggregation on each group

# This is like df['vendor'].value_counts()
df.groupby('vendor')['total_amount'].count()

# %%
df.groupby('vendor')['total_amount'].sum()

# %%

df.groupby('vendor')['total_amount'].agg(['min', 'max', 'median'])

# %% Exercise: Which date (e.g. 2020-03-04) has the most rides?
# Use tpep_pickup_datetime as time of ride

# flow style: Place in () and split to lines
rides_by_date = (
    df.groupby(df['tpep_pickup_datetime'].dt.floor('d'))
    ['vendor']
    .count()
)
# out.index  # dates
rides_by_date.idxmax()
# %% Non-range indices
scores = pd.Series(
    [100, 80, 70],
    index=['Rick', 'Summer', 'Morty']
)
scores

# %%
scores[0]  # warning, won't work in future

# %%
scores.loc['Summer']  # Finds matching label


# %%
scores['Summer']
# %%
scores.iloc[0]  # By offset from start

# %%

scores = pd.Series(
    [100, 80, 70, 2000],
    index=['Rick', 'Summer', 'Morty', 'Rick']
)
scores.loc['Rick']
# %%

mask = (
    (rides_by_date.index.year == 2020) &
    (rides_by_date.index.month == 3)

)
rides_03_2020 = rides_by_date[mask]
rides_03_2020.plot()

# %%
%pip install matplotlib
# %%

ax = rides_03_2020.plot()
ax.set_title('March 2020 rides')
ax.set_xlabel('Day of month')
ax.set_ylabel('# of rides')
# %%

ax = rides_03_2020.plot.bar()
# %%
clean = df[
    (df['trip_distance'] > 0) &
    (df['trip_distance'] < 20)
]
clean['trip_distance'].plot.box()
# %% Exercise: Draw a bar plot
# x axis is number of passengers
# y axis is tip in percent from total (median)
df['tip_pct'] = df['tip_amount'] / df['total_amount'] * 100

(
    df.groupby('passenger_count')
    ['tip_pct']
    .median()
    .plot.bar(rot=0)
) ;
# %%
%pip install plotly
# %%
import plotly.express as px

# %%

tip_pct = (
    df.groupby('passenger_count')
    ['tip_pct']
    .median()
)
px.bar(tip_pct)
# %% What is the median number of rides per week day?
# Two steps:
# - Group by date
# - Group by day

df['date'] = df['tpep_pickup_datetime'].dt.floor('d')
# df['weekday'] = df['tpep_pickup_datetime'].dt.day_name()
df['weekday'] = df['tpep_pickup_datetime'].dt.weekday
dfm20 = df[
    (df['date'].dt.year == 2020) &
    (df['date'].dt.month == 3)

]

# by_date = dfm20.groupby(['date', 'weekday'])['VendorID'].count()
# by_date.index  # multi index, by_date is a series

by_date = dfm20.groupby(['date', 'weekday'], as_index=False)['VendorID'].count()
# by_date is a dataframe
daily = by_date.groupby('weekday')['VendorID'].median()
ax = daily.plot.bar(rot=0)
ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
ax.set_ylabel('number of rides')
ax.set_title('median weekday rides');

# %%

wdf = pd.read_csv(
    'data/NYC_Weather_2016_2022.csv.gz',
    parse_dates=['time'],
)
wdf.describe()

# %%
wdf.dtypes  # without parse_dates, time is object (str)

# %%

df_weather = pd.merge(
    df, wdf,
    how='left',
    left_on='date',
    right_on='time',
)

df_weather.sample(10)

# %%
df_weather[['tip_pct', 'temperature_2m (°C)']].corr()

# %%
# speed tip: don't concat dfs
# instead append them to list and then concat all
from pathlib import Path

dfs = []
for file_name in Path('data').glob('*.parquet'):
    df = pd.read_parquet(file_name)
    dfs.append(df)
df = pd.concat(dfs, ignore_index=True)
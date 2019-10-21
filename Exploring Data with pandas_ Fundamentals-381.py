## 1. Introduction to the Data ##

import pandas as pd

f500_head = f500.head(10)
f500.info()


## 2. Vectorized Operations ##

rank_change = f500["previous_rank"] - f500["rank"]

## 3. Series Data Exploration Methods ##

rank_change =  f500["previous_rank"] - f500["rank"]
rank_change_max = rank_change.max()
rank_change_min = rank_change.min()

## 4. Series Describe Method ##

rank_desc = f500["rank"].describe()
prev_rank_desc = f500["previous_rank"].describe()



## 5. Method Chaining ##

zero_previous_rank = f500["previous_rank"].value_counts().loc[0]

## 6. Dataframe Exploration Methods ##

f500.info()
max_f500 = f500.max(numeric_only = True)
print(max_f500)

## 7. Dataframe Describe Method ##

f500_desc = f500.describe()
print(f500_desc)

## 8. Assignment with pandas ##

f500.loc["Dow Chemical", "ceo"] = "Jim Fitterling"

## 9. Using Boolean Indexing with pandas Objects ##

motor_bool = f500["industry"] == "Motor Vehicles and Parts"
print(motor_bool)
motor_countries = f500.loc[motor_bool,"country"]


## 10. Using Boolean Arrays to Assign Values ##

import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()

## 11. Creating New Columns ##

f500["rank_change"] = f500["previous_rank"] - f500["rank"]
rank_change_desc = f500["rank_change"].describe()
print(rank_change_desc)

## 12. Challenge: Top Performers by Country ##

#print(f500["hq_location"].head(5))
#var = f500["hq_location"].str.split(", ")
#print(var[0][0])
#f500["hq country"] = var[1]
industry_usa = (f500.loc[f500["country"] == 'USA', "industry"]).value_counts().head(2)
print("2 most common US Industries:\n", industry_usa)
sector_china = f500.loc[f500["country"] == 'China', "sector"].value_counts().head(3)
print("3 most common Chinese sectors:\n",sector_china)

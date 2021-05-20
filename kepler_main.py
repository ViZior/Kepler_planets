# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:13:27 2021

@author: Viktor
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

planets_df = pd.read_csv('cumulative_2021_03_05.csv', comment='#')

print(planets_df.shape) # Number of entries and columns


# Checking on some basic info like datatype and number of missing values
info_df = pd.DataFrame({'Datatype': planets_df.dtypes,
                        'Missing_val': planets_df.isnull().sum(),
                        'Unique_vals': planets_df.nunique()})
print(info_df)



# Data cleaning
#-----------------------------------------------------------------------------------------

# The uncertainty of the equilibrium temperature is always missing. I remove
# these columns since they are anyhow not helpful for evaluating the "goodness"
# of a candidate

# The kepler_name and the kepoi_name columns are not based on physics or
# any observational patterns, so it is also not relevant. Hence, it is also removed.

# The column koi_disposition is the disposition according to the Exoplanets
# Archive. Since I will use Kepler data, this column can also be removed

planets_df.drop(['koi_teq_err1', 'koi_teq_err2', 'kepler_name', 'kepoi_name', 'koi_disposition'],
                axis=1, inplace=True)

print(planets_df.shape) # Number of entries and columns

# Checking on some basic info like datatype and number of missing values
info_df = pd.DataFrame({'Datatype': planets_df.dtypes,
                        'Missing_val': planets_df.isnull().sum()})
print(info_df)



# Our target is koi_pdisposition which is the disposition using Kepler data
# Here I check the values it has and their distribution.

print(planets_df.koi_pdisposition.unique())
plt.bar(x=planets_df.koi_pdisposition.unique(),
        height=planets_df.koi_pdisposition.value_counts())
plt.show()



# A lot of columns still have missing values. Since the dataset is large I
# test how many entries are left if I simply remove the rows with missing values
print(planets_df.dropna().shape)



# Since there are 7803 of 9564 left, I remove the rows with missing values.
# I also plot the distribution of the target variable to see if the removal
# creates imbalances
planets_df = planets_df.dropna()
plt.bar(x=planets_df.koi_pdisposition.unique(),
        height=planets_df.koi_pdisposition.value_counts())
plt.show()


# The column koi_tce_delivname is dropped since it only has one value.
# It provides therefore no additional info.
planets_df.drop(['koi_tce_delivname'], axis=1, inplace=True)


# Checking on some basic info like datatype and number of missing values.
# There should be no missing values and no columns with only one unique value now.
info_df = pd.DataFrame({'Datatype': planets_df.dtypes,
                        'Missing_vals': planets_df.isnull().sum(),
                        'Unique_vals': planets_df.nunique()})

print(info_df)

print(planets_df.shape)
#-----------------------------------------------------------------------------------------

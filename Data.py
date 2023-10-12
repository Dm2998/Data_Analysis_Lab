# 1. Import pandas and numpy, and read in the Building permits csv file and set it to a DataFrame called "permits".
import pandas as pd
import numpy as np

permits = pd.read_csv("Building_Permits.csv")



# 2. Check the head of the first 10 rows in the DataFrame.
print(permits.head(10))

# 3. Change the Datatype of the following columns into appropriate datatype:
permits["Permit Type"] = permits["Permit Type"].astype("category")
permits["Permit Creation Date"] = pd.to_datetime(permits["Permit Creation Date"])
permits["Issued Date"] = pd.to_datetime(permits["Issued Date"])

# 4. How many total missing values in each column
print(permits.isnull().sum())

# 5. Print out the percentage of the missing values in the dataset.

print(permits.isnull().mean() * 100)

# 6. How many missing values in the columns "Street Number Suffix" and "Zipcode" ?
print("Missing values in Street Number Suffix:", permits["Street Number Suffix"].isnull().sum())
print("Missing values in Zipcode:", permits["Zipcode"].isnull().sum())

# 7. Create new dataFrame named “permits_dropped” that has all the column with empty values.

permits_dropped = permits.dropna(axis=1, how="all")

# 8. Calculate all number of the dropped columns.

print("Number of dropped columns:", len(permits.columns) - len(permits_dropped.columns))

# 9. Replacing all missing value in Street Number Suffix with “0”.

permits["Street Number Suffix"].fillna("0", inplace=True)

# 10. what is the existing use of the units with the following permits No: M805907 and M839987.

print(permits[permits["Permit Number"].isin(["M805907", "M839987"])]["Existing Use"])

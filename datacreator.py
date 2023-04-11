import pandas as pd
import numpy as np


# make a dataframe N, empty rows
def make_df(N):
    col_names = []
    for i in range(N):
        col_name = input(f"Enter Column name {i+1}: ")
        col_names.append(col_name)

    df = pd.DataFrame(columns=col_names)

       
    return df

def add_row(df):
    
    row = []

    for col_name in list(df.columns):
        val = float(input(f"Enter value for {col_name}: "))
        assert val <= 1 and val >= 0
        row.append(val)

    df.loc[len(df)] = row

    return df

# df = make_df(2)
# df.loc[0] = [1,2]
# print(df)
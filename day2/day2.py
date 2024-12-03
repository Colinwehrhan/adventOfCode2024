#import data into data frame

import pandas as pd

file_path = "C:\\Users\\ColinWehrhan\\Documents\\adventOfCode2024\\day2\\input.txt"

import pandas as pd

#df = pd.read_csv(file_path, sep='\s+', header=None, dtype=object)

with open(file_path, 'r') as file:
    data = [list(map(int, line.split())) for line in file]

df = pd.DataFrame(data)

df_t = df.T

for column in df_t.columns:
    if not (
        ((df_t[column].diff().iloc[1:] >= 0) | (df_t[column].diff().iloc[1:] <= 0))  
        & (df_t[column].diff().iloc[1:].abs() <= 2)
    ).all():
        df_t = df_t.drop(column, axis=1)

count = df.shape[1]

print(count)







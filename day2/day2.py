import pandas as pd

file_path = "C:\\Users\\ColinWehrhan\\Documents\\adventOfCode2024\\day2\\input.txt"

with open(file_path, 'r') as file:
    data = [list(map(int, line.split())) for line in file]

df = pd.DataFrame(data)

df_t = df.T

print("Original Transposed DataFrame:")
print(df_t)

# Loop through columns and drop any that are increasing by more than 3 and check if they are increasing/decreasing
for column in df_t.columns:
    diffs = df_t[column].diff().iloc[1:]
    
    if not (diffs.abs() <= 3).all() or not (diffs.is_monotonic_increasing or diffs.is_monotonic_decreasing):
        df_t = df_t.drop(column, axis=1)

print(df_t)

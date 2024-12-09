import pandas as pd

file_path = "C:\\Users\\ColinWehrhan\\Documents\\adventOfCode2024\\day2\\input.txt"
#file_path = "C:\\Users\\ColinWehrhan\\Documents\\adventOfCode2024\\day2\\test.txt"
with open(file_path, 'r') as file:
    data = [list(map(int, line.split())) for line in file]

df = pd.DataFrame(data)

df_t = df.T

print("Original Transposed DataFrame:")
print(df_t)

# Loop through columns and drop any that are increasing by more than 3 and check if they are increasing/decreasing
for column in df_t.columns:
    col_data = df_t[column].dropna()
    diffs = col_data.diff().iloc[1:]


    if not (diffs.abs() <= 3).all() or not (col_data.is_monotonic_increasing or col_data.is_monotonic_decreasing) or (diffs ==0).any():
        df_t = df_t.drop(column, axis=1)


print(df_t)
row, col = df_t.shape
print("Safe rows:", col)
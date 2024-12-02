import pandas as pd

file_path = "C:\\Users\\ColinWehrhan\\Documents\\adventOfCode2024\\day1\\adventOfCodeInput.txt"


df = pd.read_csv(file_path, delim_whitespace=True, header=None)

df.columns = ['Column1', 'Column2']


print(df.iloc[0])

df['Column1'] = df['Column1'].sort_values(ascending=False).values
df['Column2'] = df['Column2'].sort_values(ascending=False).values


df['Difference'] = abs(df['Column1'] - df['Column2'])

sum_difference = df['Difference'].sum()

print(sum_difference)

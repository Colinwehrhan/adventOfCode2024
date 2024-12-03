import pandas as pd

file_path = "C:\\Users\\ColinWehrhan\\Documents\\adventOfCode2024\\day1\\adventOfCodeInput.txt"


df = pd.read_csv(file_path, delim_whitespace=True, header=None)

df.columns = ['left_list', 'right_list']


print(df.iloc[0])

df['left_list'] = df['left_list'].sort_values(ascending=False).values
df['right_list'] = df['right_list'].sort_values(ascending=False).values


df['Difference'] = abs(df['left_list'] - df['right_list'])

sum_difference = df['Difference'].sum()

print(sum_difference)


#part 2
counts = []

for value in df['left_list']:
    count = (df['right_list']== value).sum()
    counts.append(count*value)

total = sum(counts)
print(total)
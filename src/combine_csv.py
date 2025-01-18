import pandas as pd
files = ['cardex with values1.csv', 'cardex with values2.csv','cardex with values3.csv', 'cardex with values4.csv']
df = pd.DataFrame()
for file in files:
    data = pd.read_csv(file)
    df = pd.concat([df, data], axis=0, ignore_index= True)
df.to_csv('merged_files.csv', index=False)
print(data.head())
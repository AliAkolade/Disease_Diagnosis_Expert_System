import pandas as pd

df = pd.read_csv('Bonus Salus.csv')

column = list(df)

for i in column:
    file = open('Symptoms/'+str(i)+'.txt', 'a')
    for row in df[i]:
        file.write(row+'\n')
    file.close()

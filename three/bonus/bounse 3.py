import pandas as pd
x = pd.read_csv(r'C:\Users\LENOVO\Downloads\ir\section\tasks\dataset of bonus\home prediction\train_csv.csv')
#print(x)
#print(x.head(5))
print('the number of null rows is :', x.isnull().sum().sum())
x.dropna(inplace=True)
print('the number of null rows is :', x.isnull().sum().sum())
import pandas as pd

df = pd.read_csv('data/AsusLaptops.csv')

print(df.head(5))
print("=================")

print(df.info())
print("=================")

df['Warrenty_Trim'] = df['Warrenty'].str.strip('Y')  # 移除Y字串

df['Warrenty_Year'] = df['Warrenty_Trim'].astype('int')  # 轉型為int整數

assert df['Warrenty_Year'].dtype == 'int'  # 驗證欄位資料型態

print(df['Warrenty_Year'].sum())  # 執行結果99
print("=================")

print(df['Category'].describe())
print("=================")

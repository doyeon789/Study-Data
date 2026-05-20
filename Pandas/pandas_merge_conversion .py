import pandas as pd

# 데이터 병합
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2'] })

df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2'] })

df3 = pd.concat([df1, df2], axis=0) # 행 병합
df4 = pd.concat([df1, df2], axis=1) # 열 병합

print(df1)
print('\n')
print(df2)
print('\n')
print(df3)
print('\n')
print(df4)
print('\n')

print('-'*50)

# Inner Merge
df1 = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'A': ['A0', 'A1', 'A2','A3'],
                    'B': ['B0', 'B1', 'B2','B3'] })


df2 = pd.DataFrame({'key':['K0','K1','K2'],
                    'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2'] })

df_merge = pd.merge(df1, df2, on='key', how='inner')

print(df1)
print('\n')
print(df2)
print('\n')
print(df_merge)

print('-'*50)

# Outer Merge
df_merge = pd.merge(df1, df2, on='key', how='outer')

print(df1)
print('\n')
print(df2)
print('\n')
print(df_merge)
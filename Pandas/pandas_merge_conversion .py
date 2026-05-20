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


df1 = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'A': ['A0', 'A1', 'A2','A3'],
                    'B': ['B0', 'B1', 'B2','B3'] })


df2 = pd.DataFrame({'key':['K0','K1','K2'],
                    'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2'] })

inner_merge = pd.merge(df1, df2, on='key', how='inner')

# Inner Merge
print(df1)
print('\n')
print(df2)
print('\n')
print(inner_merge)

print('-'*50)

# Outer Merge
outer_merge = pd.merge(df1, df2, on='key', how='outer')

print(df1)
print('\n')
print(df2)
print('\n')
print(outer_merge)

print('-'*50)

# Left Merge
left_merge = pd.merge(df1, df2, on='key', how='left')

print(df1)
print('\n')
print(df2)
print('\n')
print(left_merge)

print('-'*50)

# Right Merge
right_merge = pd.merge(df1, df2, on='key', how='right')

print(df1)
print('\n')
print(df2)
print('\n')
print(right_merge)

print('-'*50)

df1 = pd.DataFrame({
    'A': ['A0','A1','A2'],
    'B': ['B0','B1','B2'],
}, index = ['K0','K1','K2'])

df2 = pd.DataFrame({
    'C': ['C0','C1','C2'],
    'D': ['D0','D1','D2'],
}, index = ['K0','K2','K3'])

join_merge = df1.join(df2, how='left')

print(df1)
print('\n')
print(df2)
print('\n')
print(join_merge)

print('-'*50)

sales = pd.DataFrame({
    'customer_id':[1,2,3,4],
    'product_id':[101,102,103,104],
    'quantity':[5,2,3,1]
})

customers = pd.DataFrame({
    'customer_id':[1,2,3,5],
    'name':['Alice','Bob','Charlie','David'],
    'city':['Seoul','Busan','Daegu','Incheon']
})

# 인덱스 customer_id로 설정
ssales = sales.set_index('customer_id')
customers = customers.set_index('customer_id')

# Left join
joined_data = sales.join(customers, how='left')

print(sales)
print('\n')
print(customers)
print('\n')
print(join_merge)

print('-'*50)

df1 = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'A': ['A0', 'A1', 'A2','A3'],
                    'B': ['B0', 'B1', 'B2','B3'] })


df2 = pd.DataFrame({'key':['K0','K1','K2'],
                    'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2'] })

# 열 제거 
df_merged = pd.merge(df1, df2, on='key', how='inner', suffixes=('_left', '_right'))

print(df1)
print('\n')
print(df2)
print('\n')
print(df_merged)

print('-'*50)

# 불필요한 열 제거
df_merged = pd.merge(df1, df2, on='key', how='inner')
df_merged = df_merged.drop('B', axis=1)

print(df1)
print('\n')
print(df2)
print('\n')
print(df_merged)

print('-'*50)

df1 = pd.DataFrame({'key1':['K0','K1','K2','K3'],
                    'key2':['K4','K5','K6','K7'],
                    'A': ['A0', 'A1', 'A2','A3'],
                    'B': ['B0', 'B1', 'B2','B3'] })


df2 = pd.DataFrame({'key1':['K0','K1','K2'],
                    'key2':['K4','K5','K6'],
                    'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2'] })

# 여러 열 기준 병합
df_merged = pd.merge(df1, df2, on=['key1','key2'],how='inner')

print(df1)
print('\n')
print(df2)
print('\n')
print(df_merged)
# 1. []
# 컬럼 단일 선택 df['col'] -> Series 반환
# 컬럼 여러개 선태 df[['col1','col2']] -> DataFrame 반환
# Boolean Indexing과 함께 사용 가능: df[df['col'] > 10] 

# 2. loc[]/ iloc[]
# loc : 행열 이름으로 접근
# iloc : 정수 위치 기반 인덱싱( 숫자 인덱스 사용 )

# 3. Boolean Indexing
# 조건에 따른 필터링

import pandas as pd

data = pd.read_csv('Pandas/data/titanic.csv')

# [] 연산자 내에 한 개의 컬러만 입력하면 Series 객체르 반환 
series = data['Name']
print(type(series))
print('8')

# [] 연산자 내에 한 개의 컬럼을 리스트로 입력하면 DataFrame 반환
one_col_df = data[['Name']]
print(type(one_col_df))

print('-'*50)

# 인덱스 3번 행의 "Pclas"열 데이터 출력
value = data.loc[3, "Pclass"]
print(value)

# 인덱스 3번 행에서 "Name"과 "Age"선택
subset = data.loc[3, ['Name', 'Age']]
print(subset)

# 인덱스 3~7번 행에서 'Name','Age', 'Embarked' 선택
subset = data.loc[3:7, ['Name', 'Age', 'Embarked']]
print(subset)

print('-'*50)

# iloc[행_위치, 열_위치] -> 0부터 시작하는 위치 기반 인덱싱
value_i = data.iloc[5, 1]
print(value_i)

# 0번쨰 행에서 1~3번째 열 선택 -> Series 반환
subset_i = data.iloc [0, [1,2,3]]
print(subset_i)

# 0~2번 행에서1~3번쨰 열 선택 -> DataFrame
subset_i = data.iloc[0:3, 1:4]
print(subset_i)

print('-'*50)

# 35살 이상의 나이를 가진 승객 추출
data_boolean = data[data['Age'] >= 35]
print(data_boolean.head())

# 'Pclass' 값이 2또는 3인 승객만 선택
class_23 = data[data['Pclass'].isin([2 ,3])]
print(class_23.head())

# 'Pclass' 값이 2또는 3인 데이터 추출
class_23 = data[(data['Pclass'] == 2) | (data['Pclass'] == 3)]
print(class_23.head())

# 'Age' 컬럼이 NaN이 아닌 행만 필터링 (값이 존재하는 값만 가져오기)
age_no_na = data[data['Age'].notna()]
print(age_no_na.head())


# 조건을 사용한 행과 열 동시에 추출(loc[])
adult_names = data.loc[data['Age'] > 35, "Name"]
print(adult_names.head())

print('-'*50)

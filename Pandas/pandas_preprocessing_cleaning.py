# -데이터 전처리- 
# 데이터 수집이 완료되면 데이터를 모델에 넣기전에 알맞게 가공하는 과정
# 분석 결과의 질을 높이기 위해데이터를 병합한는 과정
# 어떤 전처리를 적용하느냐에 따라 원본 데이터가 다르게 변형되므로, 결과도 달라질 수 있음

# 데이터 처리 방법:
# 1. 데이터 형식 맞추기
# 2. 빈 칸 채우기
# 3. 데이터 열 추가 (연관 데이터 추가)
# 4. 데이터 열추가 (이상치 제거)


# missing 데이터 처리
# 1. isna() : df또는 배열에서 결측치가 있는 True,False 반환
# 2. fillna() : 결측값을 지정한 값으로 대체
# 2. dropna() : 결측값이 포함된 행열 삭제

import pandas as pd

data = pd.read_csv('Pandas/data/titanic.csv')

# missing 데이터 확인
print(pd.isna(data))

#전체 결측치 개수 확인
print(data.isna().sum())

# 특정 컬럼에서 결측치가 얼마나 있는지 확인
print(data['Embarked'].isna().sum())

print('-'*50)

# 결측치가 있는 행 제거
clean_df = data.dropna(subset=['Embarked'], how='any')
print('결측치 제거 후 데이터 개수:', clean_df.shape[0])
print(clean_df[['Survived','Pclass','Embarked']].head())


# Embarked 컬럼의 최빈값 확인
most_freq = data['Embarked'].value_counts().idxmax()
# 결측치 최빈값으로 채우기
filled_df = data.fillna({'Embarked':most_freq})
print('Embarked 결측치 채운 후:', filled_df['Embarked'].isna().sum())
print(filled_df[['Survived', 'Pclass', 'Embarked']].head())


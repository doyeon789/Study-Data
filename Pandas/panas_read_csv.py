import pandas as pd

# csv 파일 로드
data = pd.read_csv('Pandas/data/titanic.csv')

# datafraem 출력
print( data.head() )


# df 컬럼명 출력
print('coumns:', data.columns)

# df 인덱스 출력
print('index:', data.index)

# df 값을 배열 형태로 출력
print('index value:', data.index.values[0:100])

# 새로운 컬럼 'Age_new'를 생성
data['Age_new'] = 0

# 데이터 삭제
data.drop('Age', axis=1) # inplace를 권장하지 않음
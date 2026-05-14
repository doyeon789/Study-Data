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
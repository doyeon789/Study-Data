import pandas as pd

# 딕셔너리 데이터 선언
dl = {
    'Name': ['Doyeon','Eunjun','Jeongun','Babo'],
    'Year': [2021,2024,2025,2023],
    'Class': ['Java','Data','AI','Data'],
}

# 딕셔너리를 DataFrame으로 변환
data_df = pd.Data(dl)
print(data_df)
print('-'*50)

# 새로운 컬럼명을 추가
data_df = pd.DataFrame(dl, columns=['Name','Year','Class','Age'])
print(data_df)
print('-'*50)

# 인덱스를 새래로운 값으로 할당
data_df = pd.DataFrame(dl, index=['one','two','three','four'])
print(data_df)
print('-'*50)

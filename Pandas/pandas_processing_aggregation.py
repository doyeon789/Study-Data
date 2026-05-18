import numpy as np
import pandas as pd

# default index인 rangeindex을 사용한 객체 생성
s = pd.Series([1,3,4, np.nan, 6, 8])
print(s)

data = pd.read_csv('Pandas/data/titanic.csv')

# datetime index를 사용한 객체 생성
dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

print('-'*50)

# 딕셔너리를 사용한 객체 생성
df2 = pd.DataFrame({
    "A": 1.0,
    "B": pd.Timestamp("20130102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "D": np.array([3] * 4, dtype="int32"),
    "E": pd.Categorical(["test","train","test","train"]),
    "F": "foo"
})
print(df2)

print('-'*50)

# DateFrame을 numpy로 변환
df_to_numpy = df.to_numpy()
print(df_to_numpy)
print(type(df_to_numpy))

# 통계정보 확인
print(df.describe())
# Transpose 연산
print(df.T)

print('-'*50)

print(df["A"])

print(df[0:3])

print(df["20130102":"20130104"])

print('-'*50)

# reindex로 새로운 행/열 구성하기
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
print(df1)

print('-'*50)

# 이름 기준 오름차순 정렬
titanic_sorted = data.sort_values(by=['Name'], ascending=True)
print(titanic_sorted.head(3))

# Pclass와 Name 기준 내림차순 정렬
titanic_sorted = data.sort_values(by=['Pclass','Name'], ascending=False)
print(titanic_sorted.head(3))

print('-'*50)

# unique() 컬러 내 몇건의 고유값이 있는지 파악
print(data['Pclass'].nunique())
print(data['Pclass'].unique())

print(data['Survived'].nunique())
print(data['Survived'].unique())

print(data['Name'].nunique())
print(data['Name'].unique())

print('-'*50)
# DataFrame, Series에서 집계(Aggregation)

print(data.count())

# 평균
print(data[['Age','Fare']].mean())

# 합계
print(data[['Age','Fare']].sum())

# 최솟값
print(data[['Age','Fare']].min())

print('-'*50)

# groupby()
# 데이터를 특정 컬럼을 기준으로 묶은 후, 해당 그룹에 대해 집계연산 수행

# groupby 객체 생성
titanic_groupby = data.groupby('Pclass')

# Age와 Fare에 대해 count(다양한 집계 연산 기능)
print(titanic_groupby[['Age','Fare']].count())

# -- 동일한 컬럼에 대해서 서로 다른 집계함수르 ㄹ적용하고 싶은 경우 -> agg() 활용
# 최댓값과 최소값을 나란히 출력
print(data.groupby('Pclass')['Age'].max(), data.groupby('Pclass')['Age'].min())
# max, min 함께 보기
print(data.groupby('Pclass')['Age'].agg(['max','min']))

print(data.groupby('Pclass').agg(
    age_max=('Age','max'),
    age_mean=('Age','max'),
    fare_mean=('Fare','mean')
))

agg_format = {
    'Age': 'max',
    'SibSp':'sum',
    'Fare': 'mean'
}

print(data.groupby('Pclass').agg(agg_format))


print('-'*50)
# apply()
# 함수(람다)를 결합하여 데터를 일괄적으로 가공

# apply를 통한 이름 길이 계산
data['Name_len'] = data['Name'].apply(lambda x: len(x))
print(data[['Name','Name_len']].head())


# 나이를 기준으로 아동/성인 구분
data['Child/Adult'] = data['Age'].apply(lambda x: 'Child' if x <= 19 else 'Adult')
print(data[['Age','Child/Adult']].tail())

# lambda식을 결합하여 데이터를 일괄적으로 가공
def categorize_age(age):
    """
    나이에 따라 연령대를 분류하는 함수
    """

    if age <= 5:
        return 'Baby'
    elif age <= 12:
        return 'Child'
    elif age <= 18:
        return 'Teenager'
    elif age <= 25:
        return 'Student'
    elif age <= 35:
        return 'Young Adult'
    elif age <= 60:
        return 'Adult'
    else:
        return 'Elderly'

# 적용 및 확인
data['Categorized_Age'] = data['Age'].apply(categorize_age)
print(data[['Age','Categorized_Age']].head())

print('-'*50)

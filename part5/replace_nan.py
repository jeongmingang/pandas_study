import seaborn as sns

df = sns.load_dataset('titanic')
print("# age 열의 첫 10개 데이터 출력 (5 행에 NaN 값)")
print(df['age'].head(10), '\n')

# age 열의 NaN값을 다른 나이 데이터의 평균으로 변경하기
mean_age = df['age'].mean(axis=0) # age 열의 평균 계산 (NaN 값 제외)
print("mean_age", mean_age, end='\n\n')

df['age'].fillna(mean_age, inplace=True)

print("# age 열의 첫 10개 데이터 출력 (5 행에 NaN 값이 평균으로 대체)")
print(df['age'].head(10))


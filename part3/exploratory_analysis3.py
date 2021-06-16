import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 컬럼개수
pd.set_option('display.max_columns', len(df.columns))
# 컬럼별 사이즈
pd.set_option('display.max_colwidth', 30)
# 화면 폭 사이즈
pd.set_option('display.width', 1000)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print("# 평균값")
print(df.mean(), sep='\n', end='\n\n')
print(df['mpg'].mean(), df.mpg.mean(), df[['mpg', 'weight']].mean(), sep='\n', end='\n\n')

print("# 중간값 ")
print(df.median(), df['mpg'].median(), sep='\n', end='\n\n')

print("# 최대값 ")
print(df.max(), df['mpg'].max(), sep='\n', end='\n\n')

print("# 최소값 ")
print(df.min(), df['mpg'].min(), sep='\n', end='\n\n')

print("# 표준편차 ")
print(df.std(), df['mpg'].std(), sep='\n', end='\n\n')

print("# 상관계수 ")
print(df.corr(), df[['mpg', 'weight']].corr(), sep='\n', end='\n\n')


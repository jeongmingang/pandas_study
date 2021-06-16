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
print("# 데이터프레임 df의 내용을 일부 확인", end='\n\n')
print("df.head()", df.head(), sep='\n', end='\n\n')  # 처음 5개의 행
print("df.tail()", df.tail(), sep='\n')  # 마지막 5개의 행
print()

print("# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환")
print(df.shape)
print()

print("# 데이터프레임 df의 내용 확인")
print(df.info())
print()

print("# 데이터프레임 df의 자료형 확인")
print(df.dtypes)
print()

print("# 시리즈(mog 열)의 자료형 확인")
print(df.mpg.dtypes)
print()

print("# 데이터프레임 df의 기술통계 정보 확인")
print(df.describe(), '\n\n', df.describe(include='all'))


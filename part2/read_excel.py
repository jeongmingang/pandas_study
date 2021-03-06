import pandas as pd

# read_excel() 함수로 데이터프레임 변환
df1 = pd.read_excel('./남북한발전전력량.xlsx') # header=0 (default 옵션)
df2 = pd.read_excel('./남북한발전전력량.xlsx', header=None) # header=None 옵션

pd.set_option('display.max_columns', len(df1.columns))
pd.set_option('display.width', 1000)

# 데이터프레임 출력
print(df1, df2, sep='\n')


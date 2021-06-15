import pandas as pd
# 1번
exam_data = {'name': ['test1', 'test2', 'test3'],
             'math': [90, 80, 70],
             'eng': [98, 89, 95],
             'music': [85, 95, 100],
             'kor': [100, 90, 90]
             }

df = pd.DataFrame(exam_data)
print(df)
print()

# 2번
df = df.set_index('name')
print(df, sep='\n', end='\n\n')

# 3번
print(df.loc['test1'], sep='\n', end='\n\n')

# 4번
print(df.eng, end='\n\n')

# 5번
add_dict = {'name': 'test4', 'math': None, 'eng': 99, 'music':99, 'kor':99}
sr_add = pd.Series(add_dict, name=add_dict['name'])
print(sr_add, end='\n\n')
df = df.reset_index()
df = df.append(sr_add, ignore_index=True)
df.set_index('name', inplace=True)
print(df, end='\n\n')

# 6번
df.dropna(axis=0, inplace=True)
print(df, end='\n\n' )
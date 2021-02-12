import numpy
import pandas as pd


df = pd.read_excel('Exel_test.xlsx')
print(df)
# print(df['a'])
# print(df[df['a'] >= 4]['d'])

# print(df.loc[3])
# print(df.iloc[2, 0])
# print(df.loc[0])


# print(df['a'] >= 4)
# print(df[df['a'] >= 4][['d', 'c']])

# print(df.reset_index())
# print(df)
# df.reset_index(inplace=True)
# print(df)

# print(df.head(2))
# # print(df.info())

# print(df['d'].max())
# print(df['d'].min())
# print(df['e'].count())
# print(df['e'].value_counts())
# print(df['e'].unique())
# print(df['e'].nunique())
#
#
# def my_func(nr):
#     if nr >= 5:
#         return True
#     else:
#         return False
# print(df[df['a'].apply(my_func)])
#
# print(df.dropna())

# new_df = df[df['a'] >= 4][['d', 'c']]
# print(new_df)
#
# new_df.to_excel('tes.xlsx', index=False, sheet_name='new_sheet')



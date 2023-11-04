import pandas as pd
df = pd.read_csv("test.csv")
# print(df)
# print(df.head(2))
# print(df.tail(2))
# print(df["Salary"])
# ---------or-----------
# dx = df["Salary"]
# print(dx)
# --------------------
# dx1 = df["Salary"]
# dx2 = df[["Salary"]]
# print(dx1)
# print(dx2)
#
# print(df.shape)
# print(dx1.shape)
# print(dx2.shape)
# for i in df:
#     print( df[i])

# dx = df[["Emp_code", "Name", "Salary"]]
# print(dx)
# print(dx.shape)

# dx = df[ df['Depart'] != 'IT']
# print(dx)
# print(dx.shape)

# --------logical operator---------------
# dx = df[ df['Depart'] != 'IT']
# print(dx)
# print(dx.shape)


# --------------
# print (df['Salary'] + df ['Age'])
# print (df['Name'[3]])
# temp = df['Depart'].isin (['HR', 'IT'])
# print(df[temp])

# dx= df [df['Age'].notna()]
# print(dx)
# print(dx.shape)

# print(df['Salary'].sum())
# print(df['Salary'].max())
# print(df['Salary'].min())
# print(df['Salary'].mean())
# print(df['Salary'].median())
# print(df['Salary'].describe())

# ---------------------

# print(df['Name'].str.upper())
# print(df['Name'].str.lower())
# print(df['Name'].str.contains ('H'))
# print(df['Name'].str.contains ('H'))

# __________________Day_2_______________________
# print(df["Name"])
# print(df['Name'].str.split ('|'))

# x = df['Name'].replace({'Saleem': 'Shakeel', 'Ahmed': 'Ali'})
# print(x)
#
# x = df.sort_values(['Depart','Name'],ascending=False)
# print(x)

# x = df.sort_values(['Depart','Salary'],ascending=False)
# print(x)

# dx = pd.DataFrame (
#     {
#         'Name' : ['Abbas', 'Saeed', 'Ali', 'Asad'],
#         'Age' : [3,0,5,6]
#
# }
# )
# print(dx)
# dx.to_csv('Abcs.csv')

# itm = {'Name': 'New Data', 'Age':50}
# df = df._append(itm,ignore_index=True)
# print(df)
# df.to_csv('test2.csv')

from matplotlib import pyplot as plt
df = df.sort_values('Age')
x = df['Age']
y = df['Name']
plt.plot (args:x,y)
plt.show()


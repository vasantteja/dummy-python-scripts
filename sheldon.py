import pandas as pd

df1 = pd.DataFrame({'a':[1,2,3], 'b':[{'c':1}, {'d':3}, {'c':5, 'd':6}]})

def joris1(df):
    return pd.concat([df.drop('b', axis=1), df['b'].apply(pd.Series)], axis=1)

def joris2(df):
    return pd.concat([df.drop('b', axis=1), pd.DataFrame(df['b'].tolist())], axis=1)

def jpp(df):
    return df.join(pd.DataFrame(df.pop('b').tolist()))

df1 = pd.concat([df1]*1000, ignore_index=True)

"""
%timeit joris1(df.copy())  # 1.33 s per loop
%timeit joris2(df.copy())  # 7.42 ms per loop
%timeit jpp(df.copy())     # 7.68 ms per loop
"""
print(df1)
print(jpp(df1))
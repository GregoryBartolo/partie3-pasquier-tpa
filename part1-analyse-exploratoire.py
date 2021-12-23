import pandas as pd
import numpy as np

df = pd.read_csv("../Catalogue.csv", encoding='latin-1')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

# Display a describe of all columns in current df, could be splited as 
# include=[np.number] / include=[object] / include=['col']
print(df.describe(include='all'))

df_analyse = pd.DataFrame()

ser = []
# For each column in df, append to a Pandas Series a key/value association which contains a counts value for elems 
[ser.append(str({k:v for k,v in zip(df[col].value_counts().index,df[col].value_counts().values)})) for col in df.columns]
# Add the Pandas Series to df_analyse with good mapping indexes
df_analyse = pd.concat([df_analyse, pd.Series(ser, index=df.columns).to_frame().T])
# Rename row index in df_analyse
df_analyse.rename(index={0:'Count'},inplace=True)

# Same shit with normalize which convert count to percentage, to provide more analytics ways
ser = []
[ser.append(str({k:v for k,v in zip(df[col].value_counts().index,df[col].value_counts(normalize=True).values)})) for col in df.columns]
df_analyse = pd.concat([df_analyse, pd.Series(ser, index=df.columns).to_frame().T])
df_analyse.rename(index={0:'Percent'},inplace=True)

print(df_analyse)
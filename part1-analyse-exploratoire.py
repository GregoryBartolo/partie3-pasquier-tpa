import pandas as pd

df = pd.read_csv("../Catalogue.csv", encoding='latin-1')

print(df['marque'].value_counts())
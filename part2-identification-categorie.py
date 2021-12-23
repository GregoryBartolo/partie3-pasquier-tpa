import pandas as pd
import numpy as np

# Les criteres pour separer les vehicules:
# Longueur
# Puissance
# NbPlaces
# NbPortes

# Les categories de vehicules selon les criteres :
# Citadine - Moyenne max - 5 portes max - 100ch max
# Routiere - Longue max
# Sportive - 300ch min
# Berline - Tres longue min - 5 portes min
# SUV - Moyenne min - 5 portes min

df = pd.read_csv("../Catalogue.csv", encoding='latin-1')

# print(df.head(3))

# Definition des conditions dans l'ordre des valeurs associees a la suite
conditions = [
    ((df['longueur'] == 'moyenne') | (df['longueur'] == 'courte')) & (df['nbPortes'] <= 5) & (df['puissance'] < 100),
    (df['longueur'] != 'très longue'),
    (df['puissance'] >= 300),
    (df['longueur'] == 'très longue') & (df['nbPortes'] >= 5),
    (df['longueur'] != 'courte') & (df['nbPortes'] >= 5)
]

# Valeurs dans l'ordre des conditions de critere definis ci-dessus
values = ['Citadine', 'Routiere', 'Sportive', 'Berline', 'SUV']
df['Categorie'] = np.select(conditions, values)

# Affichage de tout le csv avec la nouvelle colonne
print(df.to_string())
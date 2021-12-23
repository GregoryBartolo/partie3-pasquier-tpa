import pandas as pd
import numpy as np

# On combine les deux fichiers CSV client
combined_clients = pd.concat([pd.read_csv("../Clients_0.csv", encoding='latin-1'), pd.read_csv("../Clients_8.csv", encoding='latin-1')])

# On recupere le fichier Immatriculations.csv
immatriculations = pd.read_csv("../Immatriculations.csv", encoding='latin-1')

# On ajoute la colonne "Categorie" aux donnees d'Immatriculations
#####################################################################################
# Definition des conditions dans l'ordre des valeurs associees a la suite
conditions = [
    ((immatriculations['longueur'] == 'moyenne') | (immatriculations['longueur'] == 'courte')) & (immatriculations['nbPortes'] <= 5) & (immatriculations['puissance'] < 100),
    (immatriculations['longueur'] != 'très longue'),
    (immatriculations['puissance'] >= 300),
    (immatriculations['longueur'] == 'très longue') & (immatriculations['nbPortes'] >= 5),
    (immatriculations['longueur'] != 'courte') & (immatriculations['nbPortes'] >= 5)
]

# Valeurs dans l'ordre des conditions de critere definis ci-dessus
values = ['Citadine', 'Routiere', 'Sportive', 'Berline', 'SUV']
immatriculations['Categorie'] = np.select(conditions, values)
#####################################################################################

# On combine les deux dataframes selon la colonne commune qui est "immatriculation"
combined_client_and_immatriculation = pd.merge(combined_clients, immatriculations, on='immatriculation')

# On genere le csv correspondant au resultat
combined_client_and_immatriculation.to_csv("Clients_Immatriculations.csv", index=False, encoding='latin-1')
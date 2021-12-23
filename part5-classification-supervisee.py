import matplotlib.pyplot as plt
import pandas as pd

clients_and_immatriculations = pd.read_csv("Clients_Immatriculations.csv", encoding='latin-1')
# print(clients_and_immatriculations.columns)

noms_categorie = clients_and_immatriculations['Categorie'].unique()
# print(noms_categorie)

nombres_vehicule = clients_and_immatriculations.groupby(clients_and_immatriculations['Categorie'], sort = False).size()
# print(nombres_vehicule)

# plt.bar(noms_categorie, nombres_vehicule, color=['r','blue','orange','y'])
# plt.title('Diagramme: Categorie vs Nombre')
# plt.xlabel('Nom des categories')
# plt.ylabel('Nombre')
# plt.show()

x = clients_and_immatriculations.iloc[:,[0]].values
y = clients_and_immatriculations.iloc[:,16].values
# print(x,y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state = 0)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
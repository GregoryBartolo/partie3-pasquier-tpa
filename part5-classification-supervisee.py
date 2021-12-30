import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

clients_and_immatriculations = pd.read_csv("Clients_Immatriculations.csv", encoding='latin-1')
# print(clients_and_immatriculations.columns)

noms_categorie = clients_and_immatriculations['Categorie'].unique()
# print(noms_categorie)

nombres_vehicule = clients_and_immatriculations.groupby(clients_and_immatriculations['Categorie'], sort = False).size()
# print(nombres_vehicule)

# Nettoyage des donnees
########################################################################
clients_and_immatriculations['sexe'].replace({
        'Féminin': 'F',
        'Femme': 'F',
        'Homme': 'M',
        'Masculin': 'M',
        'N/D': '?',
        ' ': '?',
    }, inplace=True)

clients_and_immatriculations['situationFamiliale'].replace({
        'Seule': 'Célibataire',
        'Seul': 'Célibataire',
        'Divorcée': 'Célibataire',
        'Marié(e)': 'En Couple',
        ' ': '?',
        'N/D': '?',
    }, inplace=True)

clients_and_immatriculations['age'].replace({
        '-1': '?',
        ' ': '?',
    }, inplace=True)

clients_and_immatriculations['taux'].replace({
        '-1': '?',
        ' ': '?',
    }, inplace=True)

clients_and_immatriculations['nbEnfantsAcharge'].replace({
        '-1': '?',
        ' ': '?',
    }, inplace=True)

clients_and_immatriculations['2eme voiture'].replace({
        ' ': '?',
    }, inplace=True)

clients_and_immatriculations = clients_and_immatriculations[clients_and_immatriculations['age'] != '?']
clients_and_immatriculations = clients_and_immatriculations[clients_and_immatriculations['sexe'] != '?']
clients_and_immatriculations = clients_and_immatriculations[clients_and_immatriculations['situationFamiliale'] != '?']
clients_and_immatriculations = clients_and_immatriculations[clients_and_immatriculations['2eme voiture'] != '?']
clients_and_immatriculations = clients_and_immatriculations[clients_and_immatriculations['taux'] != '?']
clients_and_immatriculations = clients_and_immatriculations[clients_and_immatriculations['nbEnfantsAcharge'] != '?']
########################################################################

# Changement des donnees string en numerique
########################################################################
# 1 pour Homme et 0 pour Femme
clients_and_immatriculations.loc[(clients_and_immatriculations.sexe == 'M'),'sexe'] = '1'
clients_and_immatriculations.loc[(clients_and_immatriculations.sexe == 'F'),'sexe'] = '0'

# 1 pour En Couple et 0 pour Celibataire
clients_and_immatriculations.loc[(clients_and_immatriculations.situationFamiliale == 'En Couple'),'situationFamiliale'] = '1'
clients_and_immatriculations.loc[(clients_and_immatriculations.situationFamiliale == 'Célibataire'),'situationFamiliale'] = '0'

# 1 pour true et 0 pour false
clients_and_immatriculations.loc[(clients_and_immatriculations['2eme voiture'] == 'true'),'2eme voiture'] = '1'
clients_and_immatriculations.loc[(clients_and_immatriculations['2eme voiture'] == 'false'),'2eme voiture'] = '0'
########################################################################

clients_and_immatriculations["age"] = pd.to_numeric(clients_and_immatriculations["age"])
clients_and_immatriculations["sexe"] = pd.to_numeric(clients_and_immatriculations["sexe"])
clients_and_immatriculations["situationFamiliale"] = pd.to_numeric(clients_and_immatriculations["situationFamiliale"])
clients_and_immatriculations["taux"] = pd.to_numeric(clients_and_immatriculations["taux"])
clients_and_immatriculations["nbEnfantsAcharge"] = pd.to_numeric(clients_and_immatriculations["nbEnfantsAcharge"])
clients_and_immatriculations["2eme voiture"] = pd.to_numeric(clients_and_immatriculations["2eme voiture"])


x = clients_and_immatriculations.iloc[:,[0,1,2,3,4,5]].values
y = clients_and_immatriculations.iloc[:,16].values

X_train, X_test, y_train, y_test = train_test_split(x,y,random_state = 0)

# Decision Tree
############################################################################
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier().fit(X_train, y_train)
print('Accuracy of Decision Tree classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of Decision Tree classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))
############################################################################

# K-Nearest Neighbors
############################################################################
print()
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of K-NN classifier on training set: {:.2f}'
     .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
     .format(knn.score(X_test, y_test)))
############################################################################

# Linear Discriminant Analysis
############################################################################
print()
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)
print('Accuracy of LDA classifier on training set: {:.2f}'
     .format(lda.score(X_train, y_train)))
print('Accuracy of LDA classifier on test set: {:.2f}'
     .format(lda.score(X_test, y_test)))
############################################################################

# Gaussian Naive Bayes
############################################################################
print()
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)
print('Accuracy of GNB classifier on training set: {:.2f}'
     .format(gnb.score(X_train, y_train)))
print('Accuracy of GNB classifier on test set: {:.2f}'
     .format(gnb.score(X_test, y_test)))
############################################################################

# Matrice de confusion
############################################################################
print()
print('Matrice de confusion :')
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
pred = knn.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
############################################################################
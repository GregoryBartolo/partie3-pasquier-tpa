import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)


def analyseCSV(name, listDim, parallel_color, yVio, xVio, colorVio):

    df = pd.read_csv("../"+name+".csv", encoding='latin-1')

    # Display a describe of all columns in current df, could be splited as 
    # include=[np.number] / include=[object] / include=['col']
    print(" *********** " + name + " Describe ***********")
    print(df.describe(include='all'))


    print(" *********** " + name + " Infos ***********")
    print(df.info())

    print(" *********** " + name + " Missing Values ***********")
    print(df.isna().sum())

    print(" *********** " + name + " Alluvial Diagram")
    fig = px.parallel_categories(df, dimensions=listDim,
                    color=parallel_color, color_continuous_scale=px.colors.sequential.Inferno)
    fig.show()

    #fig = px.parallel_categories(df[['marque', 'nom', 'puissance', 'longueur', 'nbPlaces', 'nbPortes', 'couleur', 'occasion', 'prix']],
    #color_continuous_scale=px.colors.sequential.Inferno)
    #fig.show()

    print(" *********** " + name + " Violon Diagram")
    fig = px.violin(df, y=yVio, x=xVio, box=True, color=colorVio, points='all', hover_data=df.columns)
    fig.show()


    df_analyse = pd.DataFrame()

    ser = []
    # For each column in df, append to a Pandas Series a key/value association which contains a counts value for elems 
    [ser.append(str({k:v for k,v in zip(df[col].value_counts().index,df[col].value_counts().values)})) for col in df.columns]
    # Add the Pandas Series to df_analyse with good mapping indexes
    df_analyse = pd.concat([df_analyse, pd.Series(ser, index=df.columns).to_frame().T])
    # Rename row index in df_analyse
    df_analyse.rename(index={0:'Count'},inplace=True)

    # Same thing with normalize which convert count to percentage, to provide more analytics ways
    ser = []
    [ser.append(str({k:v for k,v in zip(df[col].value_counts().index,df[col].value_counts(normalize=True).values)})) for col in df.columns]
    df_analyse = pd.concat([df_analyse, pd.Series(ser, index=df.columns).to_frame().T])
    df_analyse.rename(index={0:'Percent'},inplace=True)

    print(df_analyse)

    # Duplicated rows ? 
    #[print(x) for x in df.duplicated()]


listCatalogue = ['marque', 'nom', 'puissance', 'longueur', 'nbPlaces', 'nbPortes', 'couleur', 'occasion']
analyseCSV('Catalogue',listCatalogue, 'prix', 'prix', 'marque', 'marque')


#age,sexe,taux,situationFamiliale,nbEnfantsAcharge,voitureSecondaire
#21,F,1396,Cï¿½libataire,0,false

listMarketing = ['age','sexe','taux','situationFamiliale','nbEnfantsAcharge','voitureSecondaire']
analyseCSV('Marketing',listMarketing, 'taux', 'taux', 'situationFamiliale', 'situationFamiliale')
import os
#chargement de fichier
os.chdir("'/usr/'")
import pandas
import numpy
#importation de la fonction apriori
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
#importation des données
D = pandas.read_table("market_basket.txt",delimiter="\t",header=0)
#10 premières lignes
print(D.head(10))
#vérification des dimensions
print(D.shape)
#tableau binaire 0/1
TC= pandas.crosstab(D.ID,D.Product)
#20 premières transactions et les 3 premiers produits
print(TC.iloc[:20,:3])
#dimensions
print(TC.shape)
#liste des noms de produits
print(TC.columns)
#itemsets frequents
freq_itemsets = apriori(TC,min_support=0.025,max_len=4,use_colnames=True)
#affichage des 15 premiers itemsets
print(freq_itemsets.head(15))
#fonction de test d'inclusion
def is_inclus(x,items):return items.issubset(x)
#recherche des index des itemsets correspondant à une condition
id = numpy.where(freq_itemsets.itemsets.apply(is_inclus,items={'Aspirin'})) 
print(id)
#affichage des itemsets correspendant
print(freq_itemsets.loc[id])
#affichage des itemsets corresp.
print(freq_itemsets[freq_itemsets['itemsets'].ge({'Aspirin','Eggs'})])
#génération des règles à partir des itemsets fréquents
regles = association_rules(freq_itemsets,metric="confidence",min_threshold=0.75)
#5 "premières" règles
print(regles.iloc[:5,:])
#affichage des règles avec un LIFT supérieur ou égal à 7
print(myRegles[myRegles['lift'].ge(7.0)])
#filtrer les règles menant au conséquent {‘2pct_milk’}
print(myRegles[myRegles['consequents'].eq({'2pct_Milk'})])
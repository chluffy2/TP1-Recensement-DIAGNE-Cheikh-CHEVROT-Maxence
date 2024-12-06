import csv
table1 = []
with open('donnees_2008.csv', newline="") as csvfile :
    reader = csv.reader (csvfile, delimiter = ',')
    for row in reader :
        #print(','.join(row))
        table1.append(row)
#On enlève la première ligne
table1.remove(table1[0])
#On convertit les valeurs mises en chaines de caractères de base en integer (des chiffres)
for i in table1 :
    i[0]=int(i[0])
    i[3]=int(i[3])
    i[4]=int(i[4])
    i[5]=int(i[5])
    i[7]=int(i[7])
    i[8]=int(i[8])
    i[9]=int(i[9])
table1.sort()
#print(table1)


table2 = []
with open('donnees_2016.csv', newline="") as csvfile :
    reader = csv.reader (csvfile, delimiter = ',')
    for row in reader :
        #print(','.join(row))
        table2.append(row)
table2.remove(table2[0])

for j in table2 :
    j[0]=int(j[0])
    j[3]=int(j[3])
    j[5]=int(j[5])
    j[7]=int(j[7])
    j[8]=int(j[8])
    j[9]=int(j[9])
table2.sort()
#print(table2)

table3 = []
with open('donnees_2023.csv', newline="") as csvfile :
    reader = csv.reader (csvfile, delimiter = ';')
    for row in reader :
        #print(','.join(row))
        table3.append(row)
table3.remove(table3[0])

for h in table3 :
    h[0]=int(h[0])
    h[3]=int(h[3])
    h[5]=int(h[5])
    h[8]=int(h[8])
    h[9]=int(h[9])
    h[10]=int(h[10])
table3.sort()
#print(table3)

#Ici on va comparer la population totale d'Auvergne en 2008 à celle d'Auvergne-Rhône-Alpes en 2023

A=0
L=0
for l in range(len(table1)):
    if table1[l][1]=='Auvergne':
        A=table1[l][9]
for m in range(len(table3)):
    if table3[m][1]=='Auvergne-Rhône-Alpes':
        L=table3[m][10]

#if A > L:
    #print("La population la plus élevée est celle D'Auvergne en 2008 avec :", A)
#else:
    #print("La population la plus élevée est celle D'Auvergne-Rhône-Alpes en 2023 avec :", L)

#On essaie de créer un graphique qui affiche l'évolution de la population totale de 2008 à 2023'


import matplotlib.pyplot as plt
import numpy as np
y=np.array(table3)
my_labels=["en 2008", "en 2016", "en 2023"]
plt.pie(y)
plt.title("Graphique du nombre de population")
plt.xlabel('Nombre de Population')
plt.ylabel('Année')
plt.show()
 





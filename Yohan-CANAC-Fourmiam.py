#Import des bibliothèques nécessaires au bon fonctionnement du script Python
import pants
import math
import csv
import networkx as ntx
import matplotlib.pyplot as mtpl

#Création et initialisation des variable
position= ""
index = 0
label = row[1]
tenant = 6
aboutissant = 7
BI_MIN = 8
BP_MIN = 9
BI_MAX = 10
BP_MAX = 11

#Création et initialisation d'un graph Newtworkx
graph = ntx.Graph()

#Import du fichier CSV, vérification d'absence de valeur "null"
with open("VOIES_NM.csv") as csv_file:
	reader_file = csv.reader(csv_file)
	index = 0
	for line in reader_file:
		index += 1
		if (line[tenant] != "" and line[aboutissant] != ""):
			if (line[BI_MIN] == ""):
				line[BI_MIN] = 1
			else:
				line[BI_MIN] = int(line[BI_MIN])
			if (line[BP_MIN] == ""):
				line[BP_MIN] = 2
			else:
				line[BP_MIN] = int(line[BP_MIN])
			if (line[BI_MAX] == ""):
				line[BI_MAX] = line[BI_MIN]
			else:
				line[BI_MAX] = int(line[BI_MAX])
			if (line[BP_MAX] == ""):
				line[BP_MAX] = line[BP_MIN]
			else:
				line[BP_MAX] = int(line[BP_MAX])

			#Calcul du poids des rues
			poids = max(((line[BI_MAX] - line[BI_MIN])/2)+1, ((line[BP_MAX] - line[BP_MIN])/2)+1)

			#Ajout des liens entre les noeuds
			graph.add_edge(line[tenant], line[aboutissant], weight=poids, label=label)

			#Configuration du Graph Networkx
			pos = ntx.spring_layout(graph)

#Affichage du graph et de ses paramètres
ntx.draw_networkx_edges(graph, pos)
ntx.draw_networkx_labels(graph, pos)
ntx.draw_networkx_nodes(graph, pos)
ntx.draw_networkx_edge_labels(graph, pos)

#Affiche le graph. (si des "draw_xxx" ont été réalisés)
mtpl.show()

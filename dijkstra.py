## Création de la class Graph

import sys #importation du package sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Retourner le noeud du graphe"
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Retourner les voisins du noeud."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Retourne la valeur d'un coté entre deux noeuds"
        return self.graph[node1][node2]




# fonction dijkstra
def dijkstra(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
       
    shortest_path = {}
 
    
    previous_nodes = {}
 
      
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # Initialisation du noeud à 0   
    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        # Trouver le noeud avec la plus petite valeur
        current_min_node = None
        for node in unvisited_nodes: 
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
    
        # Le block de code qui suit nous permet de récupérer le noeud des voisins et fait une mise à jour de la distance
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
              
                #Mise à jour du meilleur chemin sur le noeud en cours
                previous_nodes[neighbor] = current_min_node
  
    #Après avoir visité les voisins, nous marquons le noeud comme "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path


#Affichage des résultats
def affiche_resultat(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Ajout des nodes
    path.append(start_node)
    
    print("Nous avons trouvé ce chemin plus rapide pour une distance de:{}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))
    return f"Le plus court chemin entre les deux villes choisies est de:{shortest_path[target_node]}\n{'Les villes intermédiaires sont:'}\n{'->'.join(reversed(path))}"

'''
Liste des villes constituant des noeuds
'''
nodes = ["Matam", "Saint Louis", "Louga", "Dakar", "Kolda", "Tamba", "Bakel", "Saint Louis", "Diourbel", "Thiés", "Kédougou", "Louga", "Mbour", "Fatick","Cap Skirring","Kaolack","Ziguinchor"]
 
init_graph = {}
for node in nodes:
    init_graph[node] = {}    
init_graph["Matam"]["Bakel"] =151
init_graph["Matam"]["Saint Louis"] =429
init_graph["Matam"]["Louga"] = 365
init_graph["Bakel"]["Tamba"] =220
init_graph["Saint Louis"]["Louga"] = 61
init_graph["Louga"]["Thiés"] = 133	
init_graph["Louga"]["Diourbel"] = 178
init_graph["Thiés"]["Dakar"] = 70
init_graph["Thiés"]["Mbour"] = 48
init_graph["Thiés"]["Diourbel"] = 76
init_graph["Dakar"]["Mbour"] = 83
init_graph["Mbour"]["Fatick"] = 72
init_graph["Fatick"]["Kaolack"] = 37
init_graph["Fatick"]["Diourbel"] = 102
init_graph["Kaolack"]["Diourbel"] = 64
init_graph["Kédougou"]["Tamba"] =235
init_graph["Tamba"]["Kolda"] =203
init_graph["Tamba"]["Kaolack"] =443
init_graph["Kolda"]["Ziguinchor"] =240
init_graph["Ziguinchor"]["Cap Skirring"] = 50
init_graph["Ziguinchor"]["Kaolack"] = 50

"""
#Création de l'objet graphe
graph = Graph(nodes, init_graph)
#instanciation des variables previous_nodes, shortest_path
previous_nodes, shortest_path = dijkstra(graph=graph, start_node="Ziguinchor")
#Afficher les résultats sur le chemin le plus court
affiche_resultat(previous_nodes, shortest_path, start_node="Ziguinchor", target_node="Saint Louis")
"""

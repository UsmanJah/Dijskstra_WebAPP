#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:30:08 2022

@author: ousmanealhayri
"""
import osmnx as ox
import networkx as nx
import folium
#import folium

ox.config(log_console=True, use_cache=True)
# define the start and end locations in latlng
start_latlng = (14.8180,-17.3079)
end_latlng = (13.8301533, -13.0891759)
# location where you want to find your route
place     = 'Dakar, Senegal'
# find shortest route based on the mode of travel
mode      = 'walk'        # 'drive', 'bike', 'walk'
# find shortest path based on distance or time
optimizer = 'time'        # 'length','time'
# create graph from OSM within the boundaries of some 
# geocodable place(s)
graph = ox.graph_from_place(place, network_type = mode)
# find the nearest node to the start location
# orig_node = ox.get_nearest_node(graph, start_latlng)
orig_node = ox.distance.nearest_nodes(graph, -17.3079, 14.8180, return_dist=False)
# find the nearest node to the end location
dest_node = ox.distance.nearest_nodes(graph, -13.0891759, 13.8301533, return_dist=False)
#  find the shortest path
shortest_route = nx.shortest_path(graph, orig_node, dest_node, weight=optimizer)
#shortest_route=ox.distance.shortest_path(graph, orig_node, , weight='length', cpus=1)
shortest_route_map = ox.plot_route_folium(graph, shortest_route)
#shortest_route_map.save(templates/nom.html)
# Map
shortest_route_map = ox.plot_route_folium(graph, shortest_route)
shortest_route_map
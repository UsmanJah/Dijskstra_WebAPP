#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:30:08 2022

@author: ousmanealhayri
"""
import networkx as nx
G=nx.Graph()
G.add_nodes_from(['Ziguinchor','Fatick','Kaolack','Dakar','Kolda','Tamba','Kédougou','Bakel','Matam','Saint Louis','Louga','Thiés','Diourbel','Mbour', 'Cap Skirring'])
G.add_weighted_edges_from([("Ziguinchor","Fatick", 300),
               ("Ziguinchor","Kaolack", 252),
               ("Kaolack","Dakar", 192),
               ("Ziguinchor","Kolda", 275),
               ("Kaolack","Tamba", 275),
               ("Kolda","Tamba", 203),
               ("Kédougou","Tamba", 235),
               ("Tamba","Bakel", 220),
               ("Bakel","Matam", 151),
               ("Matam","Saint Louis",429),
               ("Saint Louis","Louga",61),
               ("Louga","Thiés", 133),
               ("Thiés","Dakar", 264),
               ("Kaolack","Diourbel", 64),
               ("Diourbel","Thiés", 264),
               ("Mbour","Dakar", 83),
               ("Kaolack","Fatick", 37),
               ("Kaolack","Mbour", 109),
               ("Fatick","Mbour", 72),
               ("Ziguinchor","Cap Skirring", 50)])
nx.draw_networkx(G)
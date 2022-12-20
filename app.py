#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:10:51 2022

@author: ousmanealhayri
"""

from flask import Flask, render_template, Response, request, redirect, url_for, logging
from dijkstra import Graph
from dijkstra import dijkstra
from dijkstra import affiche_resultat
from dijkstra import nodes
from dijkstra import init_graph

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=["GET", "POST"])
def affichage():
    depart = request.args.get('dep', type=str)
    arrive = request.args.get('arr', type=str)
    graph = Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra(graph=graph, start_node=depart)
    affichage=affiche_resultat(previous_nodes, shortest_path, start_node=depart, target_node=arrive)
    print(depart,arrive)
    return render_template("index.html", affichage=affichage , depart=depart, arrive=arrive)



PEOPLE_FOLDER = os.path.join('static', 'assets1/webfonts')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
@app.route('/map', methods=["GET", "POST"])
def map():
    position =request.args.get('dep_map', type=str)
    destination =request.args.get('arr_map', type=str)
    if (position=="0" and destination=="0"):
         map= os.path.join(app.config['UPLOAD_FOLDER'], 'Dak.png')

    if (position=="Ma" and destination=="Bel"):
         map= os.path.join(app.config['UPLOAD_FOLDER'], 'Mabel.png')
    if (position=="Bel" and destination=="Ma"):
         map= os.path.join(app.config['UPLOAD_FOLDER'], 'Mabel.png')

    if (position=="Ma" and destination=="Cap"):
         map= os.path.join(app.config['UPLOAD_FOLDER'], 'MaCap.png')
    if (position=="Cap" and destination=="Ma"):
         map= os.path.join(app.config['UPLOAD_FOLDER'], 'MaCap.png')

    if (position=="Ma" and destination=="Glf"):
         map= os.path.join(app.config['UPLOAD_FOLDER'], 'MaGlf.png')
    if (position=="Glf" and destination=="Ma"):
         map= os.path.join(app.config['UPLOAD_FOLDER'], 'MaGlf.png')
    
    if (position=="Ma" and destination=="Km"):
         map= os.path.join(app.config['UPLOAD_FOLDER'], 'MaK.png')
    if (position=="Km" and destination=="Ma"):
         map= os.path.join(app.config['UPLOAD_FOLDER'], 'MaK.png')
    
    return render_template("index.html", map=map)



























   
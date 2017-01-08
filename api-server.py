#!/usr/bin/python

import sys
import socket
import re
from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO

#Function definitions

#Search using "Breadth-First Search" algorithm
def searchCollision(graph, start, end):
    if start not in graph:
        return False
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex == end:
            return True
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return False

#Load collision graph as an adjacency list
def loadGraph(filename):
    with open(filename, "r") as inputFile:
        graph = {}
        for line in inputFile:
            aux = line.strip().split()
            x = aux[0]
            y = aux[1]

            if x not in graph:
                graph[x] = set()
            graph[x].add(y)
        
            if y not in graph:
                graph[y] = set()
            graph[y].add(x)
    return graph

def addCollision(filename, v1, v2):
    with open(filename, "a") as outputFile:
        aux = v1 + " " + v2 + "\n"
        outputFile.write(aux)
    return

class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message

def processRequest(request_text):
    #Parse request message
    request = HTTPRequest(request_text)

    #Parse request URI
    aux = request.path.split("/")

    global collisionNets
    global FILENAME

    if aux[1].lower() == "search" and len(aux) == 4:
        return '{"status":"ok", "nodesHaveCollision":"' + str(searchCollision(collisionNets, aux[2], aux[3])) + '"}'
    if aux[1].lower() == "add" and len(aux) == 4:
        if searchCollision(collisionNets, aux[2], aux[3]) == False:
            addCollision(FILENAME, aux[2], aux[3])
            collisionNets = loadGraph(FILENAME) #Reload the graph after changes
        return '{"status":"ok", "message":"Collision added"}'

    return '{"status":"error", "message":"Invalid request URI.", "requestUri":"'+ request.path +'"}'

#Main program
HOST = "localhost"
PORT = 80
FILENAME = "collision-networks.txt"

collisionNets = loadGraph(FILENAME)

#Server setup
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print ("Serving HTTP on port %s..." % PORT)

#Server loop
while True:
    print("Waiting for new requests...")

    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(2048)

    response = processRequest(request)
    http_response = "HTTP/1.1 200 OK\n"+"Content-Type: application/json\n"+"\n"+response+"\n"
    client_connection.sendall(http_response)
    client_connection.close()



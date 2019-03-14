import math
import queue as q

class SSSP:
	def __init__(self,graph):
		self.graph = graph
		self.visited = []
		self.dist = {}
		self.sourceId = 0

	def __str__(self):
		out = ""
		for key,val in self.dist.items():
			out+="d({},{})={}\n".format(self.sourceId,key,val)
		return out

	def Dijkstra(self,sourceId):
		previous = {}	# Previous node in optimal path from source
		Q = q.PriorityQueue()	# all nodes in the graph are unoptimized - thus are in Q
		for vid in self.graph.getVertices():	# Initialization
			self.dist[vid] = math.inf	# initial distance from source to vertex v is set to infinite
			Q.put((math.inf,vid))
		self.dist[sourceId] = 0	# Distance from source to source
		Q.put((0,sourceId))
		
		while Q.empty() is not True:	# main loop
			uId = Q.get()[1]
			u = self.graph.getVertex(uId)
			for neighbor in u.outEdgeNeighbors:	# where v has not yet been removed from Q.
				neighborId = neighbor.getId()
				alt = self.dist[uId] + u.getWeight(neighbor)
				if (alt < self.dist[neighborId]):	# Relax (uId,v)
					self.dist[neighborId] = alt
					previous[neighborId] = uId

		return self.dist
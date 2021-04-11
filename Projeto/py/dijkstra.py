#By:cin.ufpe.br/~phfcs
def dijkstra(graph, start, goal):
	shortest_distance = {}
	predecessor = {}
	unseen_nodes = graph
	infinity = 9999999
	path = []

	for node in unseen_nodes:
		shortest_distance[node] = infinity
	shortest_distance[start] = 0

	while unseen_nodes:
		min_node = None
		for node in unseen_nodes:
			if min_node is None:
				min_node = node
			elif shortest_distance[node] < shortest_distance[min_node]:
				min_node = node
		for child_node, weight in graph[min_node].items():
			if weight + shortest_distance[min_node] < shortest_distance[child_node]:
				shortest_distance[child_node] = weight + shortest_distance[min_node]
				predecessor[child_node] = min_node
		unseen_nodes.pop(min_node)

	current_node = goal
	
	while current_node != start:
		try:
			path.insert(0, current_node)
			current_node = predecessor[current_node]
		except KeyError:
			return -1, -1
			break

	path.insert(0, start)

	if shortest_distance[goal] != infinity:
		return shortest_distance[goal], path
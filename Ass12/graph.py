import heapq
from collections import deque

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_location(self, location):
        if location not in self.vertices:
            self.vertices[location] = {}

    def remove_location(self, location):
        if location in self.vertices:
            self.vertices.pop(location)
        for v in self.vertices:
            self.vertices[v].pop(location, None)

    def add_road(self, from_loc, to_loc, travel_time):
        if from_loc not in self.vertices:
            self.add_location(from_loc)
        if to_loc not in self.vertices:
            self.add_location(to_loc)
        self.vertices[from_loc][to_loc] = travel_time

    def remove_road(self, from_loc, to_loc):
        if from_loc in self.vertices:
            self.vertices[from_loc].pop(to_loc, None)

    def dijkstra(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return None, float('inf')
        distances = {v: float('inf') for v in self.vertices}
        distances[start] = 0
        prev = {v: None for v in self.vertices}
        pq = [(0, start)]

        while pq:
            current_dist, u = heapq.heappop(pq)
            if current_dist > distances[u]:
                continue
            for neighbor, weight in self.vertices[u].items():
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    prev[neighbor] = u
                    heapq.heappush(pq, (distance, neighbor))

        path = []
        u = end
        if distances[end] == float('inf'):
            return None, float('inf')
        while u:
            path.insert(0, u)
            u = prev[u]
        return path, distances[end]

    def bfs_reachable(self, start):
        if start not in self.vertices:
            return []
        visited = set()
        queue = deque([start])
        reachable = []

        while queue:
            u = queue.popleft()
            if u not in visited:
                visited.add(u)
                reachable.append(u)
                for neighbor in self.vertices[u]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return reachable

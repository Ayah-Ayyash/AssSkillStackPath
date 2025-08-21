from graph import Graph

city = Graph()

locations = ["Hospital", "School", "Store", "Library", "Park", "Station"]
roads = [
    ("Hospital", "School", 5),
    ("Hospital", "Store", 10),
    ("School", "Library", 3),
    ("Store", "Library", 2),
    ("Library", "Park", 4),
    ("Park", "Station", 6),
    ("Store", "Station", 12),
    ("School", "Store", 1),
    ("Hospital", "Park", 15),
    ("Library", "Station", 8)
]

for loc in locations:
    city.add_location(loc)

for from_loc, to_loc, time in roads:
    city.add_road(from_loc, to_loc, time)

print("Reachable from Hospital:", city.bfs_reachable("Hospital"))

path, distance = city.dijkstra("Hospital", "Station")
print("Shortest path from Hospital to Station:", path)
print("Total travel time:", distance)

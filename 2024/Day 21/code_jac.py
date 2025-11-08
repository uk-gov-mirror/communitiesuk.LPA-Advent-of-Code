import heapq

codes = ['459A', '671A', '846A', '285A', '083A']
example = ['029A', '980A', '179A', '456A', '379A']

d_pad = {'^': set(['v', 'A']),
         'A': set(['^', '>']),
         '<': set(['v']),
         'v': set(['<', '^', '>']),
         '>': set(['v', 'A']),
         }

n_pad = {'A': set(['0', '3']),
         '0': set(['A', '2']),
         '1': set(['1', '4']),
         '2': set(['0', '1', '3', '5']),
         '3': set(['A', '2', '6']),
         '4': set(['1', '5', '7']),
         '5': set(['2', '4', '6', '8']),
         '6': set(['3', '4', '9']),
         '7': set(['4', '8']),
         '8': set(['5', '7', '9']),
         '9': set(['6', '8']),
         }

def dijkstra(graph, start, end):
    
    queue = [(0, start, [start])]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    shortest_paths = []

    while queue:
        current_distance, current_node, path = heapq.heappop(queue)

        if current_node == end:
            shortest_paths.append(path)
            continue

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph[current_node]:
            distance = current_distance + 1

            if distance <= distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor, path + [neighbor]))

    return shortest_paths if shortest_paths else None

# N <-- D <-- D <-- D

#  ^A
# <v>

# 789
# 456
# 123
#  0A
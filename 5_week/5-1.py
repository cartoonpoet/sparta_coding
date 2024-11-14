import heapq

example = [
    4,
    5,
    [1, 2, 4],
    [1, 3, 2],
    [2, 3, 5],
    [2, 4, 1],
    [3, 4, 7],
    [1, 4]
]


def short_cost(example):
    N, C = example[0], example[1]
    road_array = example[2:C + 2]

    graph = {}
    for road in road_array:
        if road[0] not in graph:
            graph[road[0]] = {}
        graph[road[0]][road[1]] = road[2]
        if road[1] not in graph:
            graph[road[1]] = {}
        graph[road[1]][road[0]] = road[2]

    start, end = example[-1][0], example[-1][1]
    distances = {node: float('infinity') for node in range(1, len(graph) + 1)}
    distances[start] = 0
    queue = [(start, 0)]

    while queue:
        node, cost = heapq.heappop(queue)
        if cost > distances[node]:
            pass
        for key in graph[node]:
            if graph[node][key] + cost < distances[key]:
                distances[key] = graph[node][key] + cost
                heapq.heappush(queue, (key, graph[node][key] + cost))

    return distances[max(distances)]


print(short_cost(example))

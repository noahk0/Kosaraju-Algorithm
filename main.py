from collections import defaultdict

graph, g_rev = defaultdict(list), defaultdict(list)

with open("SCC.txt") as file:
  for line in file:
    tail, head = map(int, line.strip().split())

    if tail != head:
      graph[tail].append(head)
      g_rev[head].append(tail)

order, explore = [], set()

for start in g_rev:
  if start not in explore:
    stack = [start]
    explore.add(start)

    while stack:
      node = stack[-1]

      for neighbor in g_rev[node]:
        if neighbor not in explore:
          explore.add(neighbor)
          stack.append(neighbor)

      if node == stack[-1]:
        order.append(stack.pop())

explore, scc = set(), defaultdict(list)

for lead in order[::-1]:
  if lead not in explore:
    stack = [lead]
    explore.add(lead)

    while stack:
      node = stack.pop()
      explore.add(node)

      for neighbor in graph[node]:
        if neighbor not in explore:
          explore.add(neighbor)
          stack.append(neighbor)

      if node != lead:
        scc[lead].append(node)


def dijkstra(graph, start, end):
  nodes = []
  current = start
  
  for j in graph.keys():
    nodes.append(j)
    
  d = [float('inf')]*len(nodes)

  visited = [False]*len(nodes)
  
  previous = ['']*len(nodes)

  for x in range(0, len(nodes)):
    if(nodes[x] == start):
      d[x] = 0.0
           

  complete = False
  nopath = False

  while(complete == False):
    
    for y in range(0, len(nodes)):
      if(nodes[y] == current):
        location = y

    complete = True
    neighbours = graph[current]
    for k in neighbours.keys():
      for x in range(0, len(nodes)):
        if(nodes[x] == k and visited[x] == False):
          if(d[x] > d[location] + neighbours[k]):
            d[x] = d[location] + neighbours[k]
            previous[x] = previous[location] + current
      
    for x in range(0, len(nodes)):
      if(nodes[x] == current):
        visited[x] = True
    
    minimum = float('inf')
    nextnode = ''

    for y in range(0, len(nodes)):
      if(visited[y] == False and current != nodes[y]):
        if(d[y] < minimum):
          minimum = d[y]
          nextnode = nodes[y]

    current = nextnode
    
    skip = True
    for x in range(0, len(visited)):
      if(visited[x] == False):
        complete = False
        skip = False

    if(skip == False):
      if(nextnode == ''):
        complete = True
        nopath = True

  for z in range(0, len(nodes)):
    if(nodes[z] == end):
      select = z
  
  if(nopath == True):
    return ("No path from start to end", (d[select]))

  return (previous[select]+end, int(d[select]))


def a_star(graph, heuristics, start, end):
  nodes = []
  current = start
  
  for j in graph.keys():
    nodes.append(j)
    
  d = [float('inf')]*len(nodes)

  visited = [False]*len(nodes)
  
  previous = ['']*len(nodes)

  for x in range(0, len(nodes)):
    if(nodes[x] == start):
      d[x] = 0.0
           

  complete = False
  nopath = False

  while(complete == False):
    
    for y in range(0, len(nodes)):
      if(nodes[y] == current):
        location = y

    complete = True
    neighbours = graph[current]
    for k in neighbours.keys():
      for x in range(0, len(nodes)):
        if(nodes[x] == k and visited[x] == False):
          if(d[x] > d[location] + neighbours[k]):
            d[x] = d[location] + neighbours[k]
            previous[x] = previous[location] + current
      
    for x in range(0, len(nodes)):
      if(nodes[x] == current):
        visited[x] = True
    
    minimum = float('inf')
    nextnode = ''

    for y in range(0, len(nodes)):
      if(visited[y] == False and current != nodes[y]):
        if(d[y]+heuristics[nodes[y]] < minimum):
          minimum = d[y] + heuristics[nodes[y]]
          nextnode = nodes[y]

    current = nextnode
    
    skip = True
    for x in range(0, len(visited)):
      if(visited[x] == False):
        complete = False
        skip = False

    if(skip == False):
      if(nextnode == ''):
        complete = True
        nopath = True
    
    if(current == end):
      complete = True

  for z in range(0, len(nodes)):
    if(nodes[z] == end):
      select = z
  
  if(nopath == True):
    return ("No path from start to end", (d[select]))

  return (previous[select]+end, int(d[select]))

  return ()
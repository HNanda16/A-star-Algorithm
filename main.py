from pathfinding import a_star
from pathfinding import dijkstra

def test_assert(name, expected, result):
    #assert
    print("Executing test..." + name)
    if expected == result:
        print("Test passed")
    else:
        print("Test failed")
        print("Expected: " + str(expected))
        print("But Got: " + str(result))

def test_dijkstra(graph, start, end, expected):
    #arrange
    #act
    result = dijkstra(graph, start, end)
    #assert
    test_assert("dijkstra", expected, result)

def test_a_star(graph, heuristics, start, end, expected):
    #arrange
    #act
    result = a_star(graph, heuristics, start, end)
    #assert
    test_assert("a*", expected, result)

#TESTS
graph = {'a':{'b':1, 'c':2},
         'b':{'a':1, 'c':2, 'd':3},
         'c':{'a':2, 'b':2, 'd':1},
         'd':{'b':3, 'c':1}}

heuristics = {'a':5, 'b':3, 'c':9, 'd':0}

#dijkstra
test_dijkstra(graph, 'a', 'd', ('acd', 3))
#a star
test_a_star(graph, heuristics, 'a', 'd', ('abd', 4))


graph2 = {'a':{'b':1, 'c':2},
         'b':{'a':1, 'd':3},
         'c':{'a':2, 'd':1},
         'd':{'b':3, 'c':1}}
test_dijkstra(graph2, 'b', 'c', ('bac', 3))
#a star
test_a_star(graph2, heuristics, 'b', 'c', ('bac', 3))


#erroneous
graph3 = {'a':{'c':2},
         'b':{'d':3},
         'c':{'a':2},
         'd':{'b':3}}
test_dijkstra(graph3, 'a', 'd', ("No path from start to end", float('inf')))
#a star
test_a_star(graph3, heuristics, 'a', 'd', ("No path from start to end", float('inf')))


graph4 = {'a':{'b':1, 'c':2, 'e':6},
          'b':{'a':1, 'c':2, 'd':3, 'e':5},
          'c':{'a':2, 'b':2, 'd':1},
          'd':{'b':3, 'c':1, 'e':1},
          'e':{'a':6, 'b':5, 'd':1, 'j':1}, 
          'f':{'g':1, 'h':2, 'j':6},
          'g':{'f':1, 'h':2, 'i':3, 'j':5},
          'h':{'f':2, 'g':2, 'i':1},
          'i':{'g':3, 'h':1, 'j':1},
          'j':{'f':6, 'g':5, 'i':1, 'e':1}}


new_heuristics = {'a':5, 'b':3, 'c':9, 'd':0, 'e':6, 'f':5, 'g':3, 'h':9, 'i':0, 'j':6}

#dijkstra
test_dijkstra(graph4, 'a', 'f', ('acdejihf', 9))
#a star
test_a_star(graph4, new_heuristics, 'a', 'f', ('abdejigf', 11))

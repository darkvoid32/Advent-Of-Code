puzzle = """
abcccaaaaacccacccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaacaccccccaaacccccccccccccccccccccccccccccccccccaaaaaaaaccccccccccccccccccccccccccccccccaaaaaa
abcccaaaaacccaaacaaacccccccccccccccccaaccccccacccaacccccccccccaacccccaaaaaaaaaaaccaaaaaaccccccccccccccccccccccccccccccccccaaaaaccccccccccccccccccccccccccccccccccaaaaaa
abccccaaaaaccaaaaaaaccccccccccccccaaaacccccccaacaaacccccccccaaaaaacccaaaaaaaaaaaccaaaaaacccccccccccccccccccccccccccccccccccaaaaaccccccccccccccaaacccccccccccccccccaaaaa
abccccaacccccaaaaaacccccccccccccccaaaaaacccccaaaaaccccccccccaaaaaacaaaaaaaaaaaaaccaaaaaacccccccccccccccccccccccccccccccccccaacaaccccccccccccccaaaaccccccccccccccccccaaa
abccccccccccaaaaaaaacccccccccccaaccaaaaaccccccaaaaaacccccccccaaaaacaaaaaaaaccccccccaaaaacccccccccccccccccccccccccccccccccccaacccccccccccccccccaaaaccaaacccccccccccccaac
abaaaaaccccaaaaaaaaaaccccccaaccaacaaaaacccccaaaaaaaaaaacccccaaaaacaaaacaaaaacccccccaacaacccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaaaaacccccccccccaaac
abaaaaaccccaaaaaaaaaacaacccaaaaaacaccaacccccaaaaaaaaaaacccccaaaaaccccccaaaaaccccccccccaacccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaakkkllccccccccccccccc
abaaaaacccccccaaacaaaaaaccccaaaaaaaccccccaaacccaacccaaaaaaacccccccccccccaaaaacccccccccaaaaaaccccccccccccccccccccccccccaaccccccccccccccccccccccackkkkkklllccccaaaccccccc
abaaaaacccccccaaacaaaaaaacccaaaaaaaccccccaaaacaaacaaaaaaaacccccccccccccaaaaaacccccccccaaaaaaccaacaacccccccccccccccaaaaaacccccccccccccccccccaaakkkkkkkkllllcccaaacaccccc
abaaaaaccccccccaacaaaaaaaacaaaaaaccccccccaaaaaaacaaaaaaaaacccccccccccccaaaacccccccccaaaaaaacccaaaaacccccccccccccccaaaaaaccccccccccccccccjjjjjkkkkkkpppplllcccaaaaaacccc
abaaaccccccccccccccaaaaaaacaaaaaacccccccccaaaaaaccaaaaaaaccccccccccccccccaaaccccccccaaaaaaaccccaaaaacccccccccccccccaaaaaaaccccaaccccccjjjjjjjkkkkppppppplllcccaaaaacccc
abccccccccccccccccaaaaaacccccccaaccccccaaaaaaaacccccaaaaaaccccccccccccccccccccccccccccaaaaaaccaaaaaacccccccccccccccaaaaaaaaaacaacccccjjjjjjjjjkooppppppplllcccaaacccccc
abccccccccccccccccaaaaaacccccccccccccccaaaaaaaaacccaaacaaacccccccccccccccccccccccaaaccaaccaaccaaaaccccccccccccccccaaaaaaaccaaaaaccccjjjjooooooooopuuuupppllccccaaaccccc
abccccccccccccccccccccaaccccccccccccccccaaaaaaaacccaaaccaacccccccccccccccccccccccaaaaaaacccccccaaaccccccccccccccccaaaaaaccccaaaaaaccjjjoooooooooouuuuuupplllccccaaccccc
abccaaaaccccaaacccccccccccccccccccccccccccaaaaaaaccaaccccccccccccaacccccccccccccccaaaaacccaaccaaaccccccccccccccccccccaaacccaaaaaaaccjjjoootuuuuuuuuuuuuppllllccccaccccc
abccaaaaaccaaaacccccccccccccccccccccccccccaacccacccccccccccccccacaaaacccccccccccaaaaaaacccaaaaaaacccccccccccccccccccccccccaaaaaacccciijnoottuuuuuuxxyuvpqqlmmcccccccccc
abcaaaaaaccaaaacccccccaaaaccccccccccacccccaaccccaaaccccccccccccaaaaaacccccccccccaaaaaaaaccaaaaaacccccccccccccccccaacccccccaacaaacccciiinntttxxxxuxxyyvvqqqqmmmmddddcccc
abcaaaaaacccaaacccccccaaaaccccaaaaaaaaccaaaaccccaacaacccccccccccaaaaccccccccccccaaaaaaaacccaaaaaaaacccccccccccccaaaaccccccccccaacccciiinntttxxxxxxxyyvvqqqqqmmmmdddcccc
abcaaaaaacccccccccccccaaaacccccaaaaaacccaaaaaaaaaaaaacccccccccccaaaaccccccccccccccaaacacccaaaaaaaaacccccccccccccaaaacccccccccccccccciiinnnttxxxxxxxyyvvvvqqqqmmmdddcccc
abcccaaccccccccccccccccaaccccccaaaaaacccaaaaaaaaaaaaaaccccccccccaacaccccccccccccccaaaccccaaaaaaaaaacccccccccccccaaaacccccccccccccccciiinnntttxxxxxyyyyyvvvqqqqmmmdddccc
SbccccccccccccccccccccccccccccaaaaaaaaccaaaccaaaaaaaaacccccccccccccccccccccccccccccccccccaaaaaaacccccccccaacccccccccccccccccccccccccciiinntttxxxxEzyyyyyvvvqqqmmmdddccc
abcccccccccccccccccccccccccccaaaaaaaaaacccccccaaaaaacccccccccccccaaacccccaacaacccccccccccccccaaaaaaccccccaacaaacccccccccccccccccccccciiinntttxxxyyyyyyyvvvvqqqmmmdddccc
abcccccccccccccccccccccccccccaaaaaaaaaaccccccaaaaaaaaccccccccccccaaaccccccaaaacccccccccccccccaaaaaaccccccaaaaacccccccccccccccccccccciiinnnttxxyyyyyyyvvvvvqqqqmmmdddccc
abcccccccccccccccccccccccccccacacaaacccccccccaaaaaaacccccccccccaaaaaaaacccaaaaacccccccccccccccaaaaaaaacaaaaaaccccccccccccccccccccccciiinntttxxwyyyyywwvvrrrqqmmmdddcccc
abaccccccccccccccccccccccccccccccaaacccccccccaaacaaaaacccccccccaaaaaaaaccaaaaaacccccccccccccccaaaaaaaacaaaaaaacccccccccccccccccccccchhnnnttwwwwwwwyyywvrrrrnnnnmdddcccc
abaccccccccccccccccccccccccccccccaaccccccccccccccaaaaaacccccccccaaaaaccccaaaacaccccccccccccccccaaaaacccccaaaaaaccccccaaaccccccaaaccchhnmmttswwwwwwywwwrrrrnnnnneeeccccc
abaccccccccccccccccccccccccccccccccccccccccccccccaaaaaacccccaaccaaaaaacccccaaccccccccccccccccccaaaaaaccccaaccaaccccaaaaaacccccaaacahhhmmmsssssssswwwwwrrrnnnneeeecccccc
abaaaccccccccccccccccccccccccccccaaaccccccccccccccaaaaaccccaaaccaaaaaacccccccccccccccccccccccccaaaaaaccccaaccccccccaaaaaacccaaaaaaahhhmmmmsssssssswwwwrrnnnneeeeacccccc
abaaaccccccccccccccccccccccccccccaaaaaaccccccccccaaaaacaaaaaaaccaaaccaccccccccaaaaaccccccccccccaaaacacccccccccccccccaaaaacccaaaaaaahhhhmmmmssssssswwwwrrnnneeeeaacccccc
abaaacccccccccccccccccccccccccccaaaaaaaccccccccccaaaaacaaaaaaaaaacccaaaaacccccaaaaacccccccccacaaaaaccacccccccccccccaaaaacccccaaaaaachhhmmmmmmmmmsssrrrrrnnneeeaaaaacccc
abaccccccccccccccaaaaccccccccccaaaaaaaacccccccccccccccccaaaaaaaaacccaaaaaccccaaaaaacccccccccaaaaaaaaaacccccccccccccaaaaaccccccaaaaachhhhmmmmmmmooossrrronneeeaaaaaacccc
abaccccccccccccccaaaaccccccccccaaaaaaacccccccccccccccccccaaaaaaaccccaaaaaacccaaaaaaccccaaaccaaaaaaaaaacccccccccccaaccccccccccaaaaaacchhhhhggggooooorrroonnfeeaaaaaccccc
abcccccccccccccccaaaaccccccccccccaaaaaacccccccccccccccccaaaaaaccccccaaaaaacccaaaaaaccccaaaaaacaaaaaacccccccccaaccaacccccccccccaacccccchhhhggggggoooooooooffeaaaaacccccc
abccccccccccccccccaacccccccccccccaaaaaacccccccaaccacccccaaaaaaacccccaaaaaaccccaaaccccccaaaaaacaaaaaacccccccccaaaaacccccccccccccccccccccccgggggggggooooooffffaaaaaaccccc
abccccccccccccccccccccccccccaaaccaacccccccccccaaaaacccccaaccaaacccccccaaacccccccccccccaaaaaaacaaaaaacccccccccaaaaaaaaccccccccccccccccccccccaaaggggfooooffffccccaacccccc
abaaccccccccccccccccccccccccaaacaccccccccccccaaaaacccccccccccaacccccccaaaacccaacccccccaaaaaaaaaaaaaaaccccccccccaaaaacccccccccccccaaaccccccccccccggfffffffffcccccccccccc
abaaccccccccccccccccccccccaacaaaaacccccccccccaaaaaacccccccccccccccccccaaaacaaaacccccccaaaaaaaaaccccaccccccccccaaaaaccccccccccccccaaaccccccccccccagfffffffccccccccccccca
abaacccccccaacccccccccccccaaaaaaaaccccccaacccccaaaacccccccccccccccccccaaaaaaaaacccccccccaaacaacaaacccccccccccaaacaaccccaaccaaccaaaaaaaaccccccccaaaccffffcccccccccccccaa
abaaaaaaaccaaccccccccccccccaaaaacccccccaaaacccaaccccccccccccccccccacaaaaaaaaaaccccccccccaaacaaaaaacccccccccccccccaaccccaaaaaaccaaaaaaaacccccccccaacccccccccccccccaaacaa
abaaaaaaaaaaccccccccccccccccaaaaaccccccaaaacccccccccccccccccccccccaaaaaaaaaaaaccccccccccccccaaaaaacccccccccccccccccccccaaaaaacccaaaaaacccccccccaaacccccccccccccccaaaaaa
abaaaacaaaaaaaacccccccccccccaacaaccccccaaaaccccccccccccccccccccccccaaaaaaaaaaacccccccccccccaaaaaaaacccccccccccccccccccaaaaaaaaccaaaaaaccccccccccccccccccccccccccccaaaaa
""".strip().split("\n")

import heapq

def find_shortest_path(graph, start, end):
  # Initialize a priority queue to store the paths
  queue = [(0, [start])]
  # Initialize a set to keep track of visited cells
  visited = set([start])

  # Loop until the queue is empty
  while queue:
    # Get the path with the lowest distance from the queue
    distance, path = heapq.heappop(queue)
    # Get the last cell from the path
    cell = path[-1]
    print("Cell : " + str(cell) + " | " + graph[cell[0]][cell[1]])
    # If the cell is the end cell, return the path
    if cell == end:
      return path
    # Loop through the valid moves from the current cell
    for move in get_valid_moves(graph, cell, visited):
      # Calculate the distance to the end cell using the Manhattan distance heuristic
      heuristic = abs(move[0] - end[0]) + abs(move[1] - end[1])
      # Create a new path by appending the move to the path
      new_path = path + [move]
      # Add the new path to the queue with the total distance (distance + heuristic) as the priority
      heapq.heappush(queue, (distance + heuristic, new_path))
      visited.add(move)

  # If no path was found, return an empty list
  print("No path found")
  return []

def get_valid_moves(maze, cell, visited):
  row, col = cell
  moves = []
  for move in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
    if is_valid_move(maze, cell, move) and move not in visited:
      moves.append(move)
  return moves

def is_valid_move(graph, move, newMove):
    xInBounds = 0 <= newMove[0] < len(graph)    
    yInBounds = 0 <= newMove[1] < len(graph[0])

    if not xInBounds or not yInBounds:
        return False

    if graph[move[0]][move[1]] == "E" :
        if graph[newMove[0]][newMove[1]] == "z":
            return True
        else:
            return False
    elif graph[newMove[0]][newMove[1]] == "S":
        if graph[move[0]][move[1]] == "a" or graph[move[0]][move[1]] == "b":
            return True
        else:
            return False

    oldElevation = ord(graph[move[0]][move[1]])
    newElevation = ord(graph[newMove[0]][newMove[1]])

    return -1 <= newElevation - oldElevation <= 1

# Driver Code
src = 0, 0
end = 0, 0

# Construct 2D Graph of input
graph = []
for idx, line in enumerate(puzzle):
    graph.append(list(line))
    if "S" in line:
        end = idx, line.index("S")
    if "E" in line:
        src = idx, line.index("E")

row = len(graph)
col = len(graph[0])
 
path = find_shortest_path(graph, src, end)
print(path)
print(len(path) - 1)
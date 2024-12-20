import numpy as np, sys
np.set_printoptions(threshold=sys.maxsize, linewidth=1000)

inp = open('antenna.txt').read()

grid = np.array([list(i) for i in inp.split('\n')])
anti = set()

antenna_type = set(list(inp))
antenna_type.remove('.')
antenna_type.remove('\n')

def get_line_distance(p1, p2):
  return p2[0] - p1[0], p2[1] - p1[1]

for antennas in antenna_type:
  posts = np.nonzero(grid == antennas)
  grid2 = np.full([len(grid), len(grid[0])], '.', dtype=str)
  current_ant_points = set()
  for i in range(len(posts[0])-1):
    for j in range(i+1,len(posts[0])):
      vert, horz = get_line_distance((posts[0][i], posts[1][i]), (posts[0][j], posts[1][j]))
      if 0 <= posts[0][j] + vert < len(grid) and 0 <= posts[1][j] + horz < len(grid[0]):
        current_ant_points.add(((posts[0][j] + vert).item(), (posts[1][j] + horz).item()))
      if 0 <= posts[0][i] - vert < len(grid) and 0 <= posts[1][i] - horz < len(grid[0]):
        current_ant_points.add(((posts[0][i] - vert).item(), (posts[1][i] - horz).item()))
  anti = anti.union(current_ant_points)
# part a
print(len(anti))

for antennas in antenna_type:
  posts = np.nonzero(grid == antennas)
  current_ant_points = set()
  for i in range(len(posts[0])-1):
    for j in range(i+1,len(posts[0])):
      vert, horz = get_line_distance((posts[0][i], posts[1][i]), (posts[0][j], posts[1][j]))
      vert_mult, horz_mult = vert, horz
      while 0 <= posts[0][j] + vert < len(grid) and 0 <= posts[1][j] + horz < len(grid[0]):
        current_ant_points.add(((posts[0][j] + vert).item(), (posts[1][j] + horz).item()))
        vert += vert_mult
        horz += horz_mult
      vert, horz = vert_mult, horz_mult
      while 0 <= posts[0][i] - vert < len(grid) and 0 <= posts[1][i] - horz < len(grid[0]):
        current_ant_points.add(((posts[0][i] - vert).item(), (posts[1][i] - horz).item()))
        vert += vert_mult
        horz += horz_mult
    for i in range(len(posts[0])):
      anti.add(((posts[0][i]).item(), (posts[1][i]).item()))
  anti = anti.union(current_ant_points)
# part b
print(len(anti))
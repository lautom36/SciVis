import numpy as np
import pyvista as pv

coords = np.genfromtxt(fname="Code/Question 1/data/coordinates.txt", skip_header=1, delimiter=" ")
connections = np.genfromtxt(fname="Code/Question 1/data/connections.txt", skip_header=1, delimiter=" ")
radii = np.genfromtxt(fname="Code/Question 1/data/radii.txt", skip_header=1)

# print(len(coords))
# print(len(radii))
# print(connections[8][1])

def getColor(n):
  n = int(n * 100)
  colors = ['purple', 'yellow', 'blue', 'red', 'teal', 'green'];
  if n in range(0, 38):
    return colors[0]
  elif n in range(38, 69):
    return colors[1]
  elif n in range(69, 74):
    return colors[2]
  elif n in range(74, 75):
    return colors[3]
  elif n in range(75, 78):
    return colors[4]
  elif n in range(78, 210):
    return colors[5]

def renderBalls(plotter):
  length = len(coords)
  for i in range(0, length):
    center = coords[i]
    rad = radii[i]
    ball = pv.Sphere(center=center, radius=(rad/2))
    color = getColor(rad)
    plotter.add_mesh(ball, color=color)

def renderConnections(plotter):
  length = len(connections)
  for i in range(0, length):
    connection = connections[i]
    a = coords[int(connection[0])]
    b = coords[int(connection[1])]
    tube = pv.Tube(a,b,radius=0.1)
    plotter.add_mesh(tube)


def render():
  plotter = pv.Plotter(notebook=False)
  legend_entries = []
  legend_entries.append(['0.37', 'purple'])
  legend_entries.append(['0.68', 'yellow'])
  legend_entries.append(['0.73', 'blue'])
  legend_entries.append(['0.74', 'red'])
  legend_entries.append(['0.77', 'teal'])
  legend_entries.append(['2.00', 'green'])
  plotter.add_legend(legend_entries) 
  renderBalls(plotter)
  renderConnections(plotter)
  plotter.show()

render()

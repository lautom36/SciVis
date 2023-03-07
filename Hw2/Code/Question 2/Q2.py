import numpy as np
import pyvista as pv

plotter = pv.Plotter()

ctScan = pv.read('Code\Question 2\data\ctscan_ez.vtk')
slices = ctScan.slice_orthogonal(x=25, y=200, z=250)
plotter.add_mesh(slices, cmap='bone')
plotter.show_grid()

liver = pv.read('Code\Question 2\data\ctscan_ez_bin.vtk')
contours = liver.contour()
plotter.add_mesh(contours, color='orange', line_width=1)


plotter.show()


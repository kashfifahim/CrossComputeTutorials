from matplotlib.pyplot import savefig
from bikeshare  import *
from sys import argv
from os.path import join 
import json

bikeshare = State(olin = 6, wellesley = 6)
results = run_simulation(bikeshare, 0.2, 0.1, 30)
simulation_figure = display_results(results)
plt.savefig(join(".", "simulation-graph.png"))
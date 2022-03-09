from matplotlib.pyplot import savefig
import bikeshare as bs
from sys import argv
from os.path import join 
import json

bikeshare_sim = bs.State(olin = 6, wellesley = 6)
results = bs.run_simulation(bikeshare_sim, 0.2, 0.1, 30)
simulation_figure = bs.display_results(results)
bs.plt.savefig(join(".", "simulation-graph.png"))
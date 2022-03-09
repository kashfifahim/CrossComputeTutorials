from matplotlib.pyplot import savefig
from bikeshare  import *
from sys import argv
from os.path import join 
import json

# input_folder, output_folder = argv[1:]

bikeshare = State(olin = 6, wellesley = 6)
# variables = json.load(open(join(input_folder, "variables.dictionary"), 'rt'))
# results = run_simulation(bikeshare, variables["p1"], variables["p2"], variables["num_steps"])
results = run_simulation(bikeshare, 0.2, 0.1, 30)
simulation_figure = display_results(results)
plt.savefig(join(".", "simulation-graph.png"))
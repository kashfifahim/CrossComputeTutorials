from matplotlib.pyplot import savefig
from bikeshare  import *
from sys import argv
from os.path import join 
import json
from sys import argv

# Get folder paths from command-line arguments
input_folder, output_folder = argv[1:]

variables = json.load(open(join(input_folder, 'variables.dictionary'), 'rt'))

bikeshare = State(olin = 6, wellesley = 6)
results = run_simulation(bikeshare, variables["p1"], variables["p2"], variables["num_steps"])
simulation_figure = display_results(results)
plt.savefig(join(output_folder, "simulation-graph.png"))
# Title of Tutorial
## Section 0: Summary -- What you will need, what you will get done by the end of the tutorial, who to reach out if you are having problems

## Section 1: Introduction to the simulation

Your company has taken on a new project.  The stakeholders want to implement a bike sharing system between the campus of Wellesley College and the campus of Olin College of Engineering. Your team has been tasked with writing a program that simulates this system.  

In the following days, you and your team discuss and gather the requirements.  Then, the team collaborated to map out the user stories. Finally, after some time developing and testing, your team has a minimum viable product in the form of a simulation, written in Python. 

Let's git clone the team's simulation program to a local folder on our machine.

## TO DO: git clone source files

Scrolling through the script we discover that it is mainly made up of function definitions.  What is of interest to us is discovering the interface to the simulation. This way, when we program to the interface, we will not have to concern ourselves with the implementation details of the simulation. All we need to be concerned with is what inputs does the simulation require and what output will it return. This is the common programming principle of programming to the interface, not to the implementation.

Near the end of the program we find the program initializes a ```State``` object with ```olin = 6``` and ```wellesley = 6``` and saves it to a variable called bikeshare.  This is the starting point for simulation, initializing the system with six bikes at each campus. In the next line, the program calls the ```run_simulation``` function. From looking at functiond definition, the ```run_simulation``` function takes the previously created ```State``` object, and three other arguments: ```p1```, ```p2```, and ```num_steps```. Those are the inputs to the ```run_simulation``` function.  The function then returns a ```TimeSeries``` object, which is saved in the variable ```results```. Next the program pushes the ```results``` to the ```display_results``` function which returns a graph of the data simulated and saved in the ```TimeSeries``` object.  

From our first analysis of the program we found that the simulation needs a ```State``` object initialized to how many bikes the system should have.  Then to run the simulation, the program needs three inputs.  The first pair of inputs, ```p1``` and ```p2``` are floating point numbers between 0.1 and 0.9. The third input, ```num_steps```, is the length of time, in mimutes, the system is simulating.  For example, if the ```num_step = 60```, this means the resulting simulation is one that takes place over sixty-minutes.  

To make our workflow easier, we are going to create a second Python script, in the same folder as the simulation source code, called ```run.py```. We will import all the functions from the simulation source code and run the code necessary to run a simulation successfully. Let us then run ```run.py``` to see all the functions are imported successfully.  Once ```run.py``` runs without error, we are then ready to continue and introduce ```crosscompute``` to the project.
## TO DO: add comments to the function definitions

With an understanding of the interface of the simulation under our belt, let's now create a new Python script and save it as ```run.py```.  

Within ```run.py``` we will import all the functions from the simulation script.  Now, let's take a second to test that our import works by running a test simulation. 

Great, everything is working. 

Up to this point we have a script holding all the functions for running the simulation.  We also developed an understanding of what the inputs and output are for the simualation.  In the next section, we will start configuring our simulation with the latet version of the CrossCompute Automation Framework.

## Section 2: Setting up your vevn

![Create a virtual environment for crosscompute automation](gifs/01-Create-venv-automation.gif)[](gifs/01-Create-venv-automation.gif)

![Checking virtual environment's pip list](gifs/02-Check-pip-list-in-venv.gif)[](gifs/02-Check-pip-list-in-venv.gif)

![Installing latest version of crosscompute framework](gifs/03-installing-latest-version-of.gif)[](gifs/03-installing-latest-version-of.gif)

### What is venv? So what? How to make one?

## Section 3: Identifying input and output

### Reviewing the modeling script: 
### What libraries will we need? Set up a setup.sh file to install all the dependencies
### Once we have our input-output create the data.dictionary file. It's going to store the user input/interactivity
### Do the same for the outputs

## Section 4: Configuring the automate.yml file

## Section 5: crosscompute automate.yml
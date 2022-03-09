# Chapter 2: Using Batch Folder to Set Input Values
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
## Configuring the automate.yml file

In the previous section we inspected the source code of the bike share simulation.  From our inspection we were able to identify the program's key functions, and more importantly, we were able to identify the inputs and output for the simulation.  With that knowledge, we then created a new script called ```run.py```. Within this new script we will now imports all the functions from the simulation source code and at the same time provides us the space to write code to the simulation's interface and not to its implementation.

(image of above paragraph)

Now in this section we take the first step towards using the CrossCompute Automation framework: configuring our ```automate.yml``` file. 

For those new to automations you might be asking, "what is a .yml file?"  

A ```.yml``` file extension refers to a ```YAML``` file.  A YAML is a human-readable data format. If you are familiar with other data formats, such as ```JSON``` or ```XML```, ```YAML``` functions much in the same way but it is easier to read and write.  As you begin to use automation tools, like our CrossCompute Automation Framewrk, you will discover more tools that require configuring and using a ```YAML``` for a given automation workflow.  With this in mind, let's start configuring our ```automate.yml``` file for the CrossCompute Automation Framwork.

Let's start by creating a new file and then saving it as ```automate.yml```. 

The ```automate.yml``` file can be filled with many sections. For this tutorial we are going to need to configure four sections. The first section provides the automation with some ```metadata```.  The second section then configures the ```inputs and outputs```. Next, we configure ```the batch section``` where we will tell the script where to find our inputs, datasets, and other options. Finally, we configure ```the scripts``` for running our automation.


Next, let us enter some metadata for our automation.  

Now, let us define the inputs.

After configuring the inputs, let's configure our outputs.

The next section we must configure for our automation is the ```batches``` section.

Finally, let's configure our ```script``` section.  

With our ```automate.yml``` file ready to go, now is a good time to activate the virtual environment that holds the ```crosscompute``` package.  Refer to the ["How to Install CrossCompute"](https://github.com/kashfifahim/CrossComputeTutorials/tree/main/Chapter-1-How-To-Install-CrossCompute) tutorial for an indepth walkthrough on how to set up your virtual environment. 

With our virtual environment activated, let us go ahead and run ```crosscompute autoamte.yml```. 

What should you see? In the terminal you should see the local address where your automation is being served.  

You should also see, in the project directory, a new folder called batches.  We need to go into that directory, and there you should see another folder called ```input```. Let's go into that folder and create a new file called ```variables.dictionary```.





## Section 5: crosscompute automate.yml

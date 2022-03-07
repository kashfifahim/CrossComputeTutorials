# Title of Tutorial

<!-- You have an idea.  You get your pen and your paper to take down that idea and put it on paper.  You then take your idea on paper, you head to your machine. At your machine, you work line after line, funtions after functions, tests after tests, that idea from your head, to your paper, is now on your machine. You run your code. You solve a problem. The program But now your tool just sits on your machine, it waits for you to run it, it waits for you to give it some inputs, it waits to solve a problem and return to the world the solution.  -->


## Section 1: Introduction to the simulation

Your company has taken on a new lucrative project.  The stakeholders want to implement a bikes sharing system between the campus of Wellesley College and the campus of Olin College of Engineering. In the following days, you and your team discuss and gather the requirements.  Then together you discuss and map out the user stories, before finally having a minimum viable product in the form of a simulation. With some creative programming, your team's simulation can depict in a graph the likelihood of a customer arriving to an available bike, wait for a bike, or not use the system.

Let's check out the team's program.  Let us get ourselves a copy the team's code.  Let's git clone the team's repository to a local folder on our machine.  

Now that we have a copy of the code, let us analyze the code to discover what the simulation needs in terms of its inputs and what the simulation returns as its output. In other words, let's discover the interface for the simulation.

Now that we know how the simulation works, let's create a new Python script call run.py.  In this script we will import all the functions from the simulation script.  This way we can build on the team's work, while not worrying about any of the implementation details. Some of you may know this as the principle of programming to the interface and not to the implementation.

Within this run.py script, let's import all the functions from the previous script.  Now, let's take a second to test that our import works by running a test simulation. 

Great, everything is working. Up to this point we have a script holding all the functions for running the simulation.  We also developed an understanding of what the inputs and output are for the simualation.  In the next section, we will start configuring our simulation with the latet version of the CrossCompute Automation Framework.


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
# Title of Tutorial

<!-- You have an idea.  You get your pen and your paper to take down that idea and put it on paper.  You then take your idea on paper, you head to your machine. At your machine, you work line after line, funtions after functions, tests after tests, that idea from your head, to your paper, is now on your machine. You run your code. You solve a problem. The program But now your tool just sits on your machine, it waits for you to run it, it waits for you to give it some inputs, it waits to solve a problem and return to the world the solution.  -->


## Section 1: Introduction to the simulation

Your company has taken on a new project.  The stakeholders want to implement a bike sharing system between the campus of Wellesley College and the campus of Olin College of Engineering. In the following days, you and your team discuss and gather the requirements.  Then, the team collaborated to map out the user stories. Finally, after some time developing and testing, your team has a minimum viable product in the form of a simulation, written in Python. 

Let's git clone the team's repository to a local folder on our machine. Then let's check out the team's program.  

The script is filled with lots of function definitions.  What is of interest to us is discovering the interface to the simulation. This way, when we program to the interface, we will not have to concern ourselves with the implementation details of the simulation. All we need to be concerned with is what inputs does the simulation require and what output will it return. This is the common programming principle of programming to the interface, not to the implementation.


With an understanding of the interface of the simulation under our belt, let's now create a new Python script and save it as ```run.py```.  

Within ```run.py`` we will import all the functions from the simulation script.  Now, let's take a second to test that our import works by running a test simulation. 

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
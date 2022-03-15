# Chapter 2: Using Batch Folder to Set Input Values
## Section 0: Summary -- What you will need, what you will get done by the end of the tutorial, who to reach out if you are having problems

## Introduction to the simulation

Your company has taken on a new project.  The stakeholders want to implement a bike sharing system between the campus of Wellesley College and the campus of Olin College of Engineering. Your team has been tasked with writing a program that simulates this system.  

In the following days, you and your team discuss and gather the requirements.  Then, the team collaborated to map out the user stories. Finally, after some time developing and testing, your team has a minimum viable product in the form of a simulation, written in Python. 

In the next section, let us look at the team's simulation program. [You can follow along with the code found in the ```src``` folder in the tutorials. For this next section the code can be found here.](https://github.com/kashfifahim/CrossComputeTutorials/blob/main/src/Chapter-2/bikeshare.py)

### Programming to the Interface, Not the Implementation

What is of interest to us is discovering the interface to the simulation. This is an important design principle of programming to the interface, not to the implementation. When we program to the interface, we will not have to concern ourselves with the implementation details of the simulation. All we need to be concerned with is what inputs does the simulation require and what output will it return.
 
![Scroll view of the program](/assets/gifs/Scrolling%20through%20bikeshare.gif "Scroll view of the program")

Scrolling through the script we discover that it is mainly made up of function definitions.  We just need to take note of what these functions definitions need as inputs and what they will return as output, if any.  We trust the team has implemented efficient implmenetation to each function, and that is the most we will think about the implementation details.

Near the end of the program we find the program initializes a ```State``` object with ```olin = 6``` and ```wellesley = 6``` and saves it to a variable called bikeshare.  This is the starting point for simulation, initializing the system with six bikes at each campus. In the next line, the program calls the ```run_simulation``` function. From looking at function definition, the ```run_simulation``` function takes the previously created ```State``` object, and three other arguments: ```p1```, ```p2```, and ```num_steps```. Those are the inputs to the ```run_simulation``` function.  The function then returns a ```TimeSeries``` object, which is saved in the variable ```results```. Next the program pushes the ```results``` to the ```display_results``` function which returns a graph of the data simulated and saved in the ```TimeSeries``` object.  

From our first analysis of the program we found that the simulation needs a ```State``` object initialized to how many bikes the system should have.  Then to run the simulation, the program needs three inputs.  The first pair of inputs, ```p1``` and ```p2``` are floating point numbers between 0.1 and 0.9. The third input, ```num_steps```, is the length of time, in minutes, the system is simulating.  For example, if the ```num_step = 60```, this means the resulting simulation is one that takes place over sixty-minutes.  

To make our workflow easier, we are going to create a second Python script, in the same folder as the simulation source code, called ```run.py```. We will import all the functions from the simulation source code and run the code necessary to run a simulation successfully. Let us then run ```run.py``` to see all the functions are imported successfully.  Once ```run.py``` runs without error, we are then ready to continue and introduce ```crosscompute``` to the project.

With an understanding of the interface of the simulation under our belt, let's now create a new Python script and save it as ```run.py```.  

![Our first iteration of run.py](/assets/gifs/run-py-1.gif "Our first go at run.py")

Within ```run.py``` we will import all the functions from the simulation script.  Now, let's take a second to test that our import works by running a test simulation. 

Up to this point we have a script holding all the functions for running the simulation.  In addition, we now have a ```run.py``` script that serves as our entry point to the simulation.  We know the arguments that must be passed to the simulation, those arguments will serve as the variables to change in automating the simulation. In the next section, we will start configuring our simulation with the latest version of the CrossCompute Automation Framework.
## Configuring our ```automate.yml``` file

In the previous section we inspected the source code of the bike share simulation.  From our inspection we were able to identify the program's key functions, and more importantly, we were able to identify the inputs and output for the simulation.  With that knowledge, we then created a new script called ```run.py```. Within this new script we will now have all the functions from the simulation source code and at the same time have the space to write code to the simulation's interface and not to its implementation.

![UML Diagram](/assets/imgs/ch2-01.png "UML Diagram")

Now in this section we take the first step towards using the CrossCompute Automation framework: configuring our ```automate.yml``` file. 

For those new to automations you might be asking, "what is a .yml file?"  

A ```.yml``` file extension refers to a ```YAML``` file.  A YAML is a human-readable data format. If you are familiar with other data formats, such as ```JSON``` or ```XML```, ```YAML``` functions much in the same way but it is easier to read and write.  As you begin to use automation tools, like our CrossCompute Automation Framework, you will discover more tools that require configuring and using a ```YAML``` for a given automation workflow.  With this in mind, let's start configuring our ```automate.yml``` file for the CrossCompute Automation Framework.

Let's start by creating a new file and then saving it as ```automate.yml```. 

The ```automate.yml``` file can be filled with many sections. For this tutorial we are going to need to configure four sections. The first section provides the automation with some ```metadata```.  The second section then configures the ```inputs and outputs```. Next, we configure ```the batch section``` where we will tell the script where to find our inputs, datasets, and other options. Finally, we configure ```the scripts``` for running our automation.

### ```automate.yml``` > metadata section
Let us get started with configuring our ```automate.yml``` file by filling in the first section: our project's metadata.

First configure the version of ```crosscompute``` you will be using. At the time of writing, ```crosscompute``` is at version ```0.9.1```.  

    ---
    # version of crosscompute
    crosscompute: 0.9.1

Next, we are going to give a name to our automation.

    ---
    # version of crosscompute
    crosscompute: 0.9.1

    # name of your automation
    name: Olin-Wellesley Bike Share System

Finally, to wrap up the ```metadata``` section let's add a version number to our ```automation```. This completes the ```metadata``` part of our ```automate.yml``` configuration file.  Our ```automate.yml``` file should contain the following:

    ---
    # version of crosscompute
    crosscompute: 0.9.1

    # name of your automation
    name: Olin-Wellesley Bikeshare System

    # version of your automation
    version: 0.0.2

Next we will configure the input and output configurations.

### ```automate.yml``` > ```input configuration``` section
Now, let us define the inputs. Earlier when we analyzed the source code of the simulation, ```bikeshare.py``` we took note of the inputs the simulation needed to run.  We noted that we needed 3 variables, ```p1```, ```p2```, and ```num_steps```. Let's go ahead and add these three variables to the ```input``` section.

First we're going to tell our ```automate.yml``` file that we are now configuring the inputs with ```input:```. Next, after an indent, let's tell the file that we are now configuring the ```variables``` for the ```input``` section with ```variables:```. Since we know we are going to need three variables, we are going to create an ```- id``` for each of the variables and connect those variables to the ```id``` as follows below:

    # input configuration
    input:
    # input variables
      variables:
        - id: p1
        - id: p2
        - id: num_steps

Next, we need to tell our ```automate.yml``` file how to render each of these variables.  We know each input variable, ```p1```, ```p2```, ```num_steps``` are going to be holding numbers, so we are going to add a ```view``` attribute to each of the ```id``` and set them to ```number```.

    # input configuration
    input:
      # input variables
      variables:
        - id: p1
          view: number
        - id: p2
          view: number
        - id: num_steps
          view: number

Finally, we need to provide ```automate.yml``` a path to where the script can load these variables.  Here we have a lot of choices.  You can use a ```csv```, you can use a ```json```, but for this tutorial we can actually work with a simple ```.dictionary``` file which we will call ```variables.dictionary```. Since each of the variables will be located in the same file, we can now go ahead and assign the ```path``` attribute to each ```id``` and assign the ```variables.dictionary``` to the ```path```. The ```variables.dictionary``` file path will be relative to a folder called ```input_folder``` that we will need to later create.

    # input configuration
    input:
    # input variables
      variables:
        - id: p1
          view: number
            path: variables.dictionary
        - id: p2
          view: number
            path: variables.dictionary
        - id: num_steps
          view: number
            path: variables.dictionary

We are going to need to complete some follow up tasks. To keep track of those follow up tasks let's create a ``TO DO`` note and add the following tasks for ourselves: 

    TO DO 
        [] create an input_folder
        [] create a variables.dictionary
        [] declare and assign value to p1, p2, num_steps for first simulation
    
That covers configuring the ```input variables``` section of our ```automate.yml``` file.  Next let's configure the ```output variables```.

### ```automate.yml``` > ```output configuration``` section
Configuring the ```output``` section is similar to the steps taken when configuring the ```input``` section.  

First let's declare the ```output``` section and underneath declare the ```variables``` section.

    output:
      variables:

Earlier in our inspection of the simulation source code we noted that there were three input variables, ```p1```, ```p2```, and ```num_steps```. For each set of these ```input variables``` came an output that was a graph saved as an image, ```simulation-graph.png```.  We just need to configure these details into our ```automate.yml``` file. 

First let's give the output variable an ```id```. 

    output:
      variables:
        - id: simulation_graph

Next, because the variable is going to be rendered and saved as a ```.png``` we need to set ```simulation_graph```'s ```view``` attribute as that of an ```image```.

    output:
      variables:
        - id: simulation_graph
          view: image

The last detail to configure, just like we did for ```input```, we need to give a path where ```simulation_graph``` output would be found. This path is relative to an ```output_folder``` that we will need to create.

 output:
  variables:
    - id: simulation_graph
      view: image
        path: simulation-graph.png

At this point, be sure to save your ```automate.yml``` file.  We are now going to move on to configuring the ```batches``` section of our ```automate.yml``` file.

### ```automate.yml``` > ```batches configuration``` section
The next section we must configure for our automation is the ```batches``` section.  Up to this point we've defined our ```metadata```, our ```input configuration```, and our ```output_cofiguration```.  The ```batch configuration``` is where ```crosscompute``` shows off its ease of use. 

For the ```batch configuration``` there are three key use cases. 

The first use case is to define a batch folder from which a set of values for your input variables can be found. 

The second use case is providing a ```batch configuration``` where an assorted amount of variable values can be provided to the automation through, for example, a simple ```csv``` file. 

Finally, in the third use case, we can use a reference folder with a set of default values. Those default values can then be used to fill in missing values for variables while shifting and changing selected variables. 

In our current tutorial, we are working on the first use case of just defining a ```folder``` in the ```batch``` configuration section where our ```variables.dictionary``` will be stored. After declaring the batch section with ```batches:```, in the following line, after an indent, we're going to set the ```folder``` attribute to ```batches/a```. This means that within the current project directory we will need a folder called ```batches``` which has a subfolder within it called ```a```.  Feel free to set the folder name to anything you wish, just make sure to create the folder and subfolder with the same names.

    batches:
      - folder: batches/a

For the first use case, for the purposes of this first tutorial, that is all that is needed for configuring the ```batches``` section of our ```automate.yml``` file.  In the next section we are going to configure the final section of our ```automate.yml``` file, the ```scripts configuration``` section.

### ```automate.yml``` > ```script configuration``` section
Finally, let's configure our ```scripts``` section.  In this section ```scripts``` all we need to do is tell ```crosscompute``` the ```command``` to execute for our automation to execute. 

Now, we have two scripts.  Which script should we choose? 

Our first script, ```bikeshare.py```, originally had all the function definitions and the entry point to running the simulation.  Then we created a second script called ```run.py```. ```run.py``` then became the script to which we imported all the functions from the aforementioned ```bikeshare.py```. ```run.py``` is also now the entry point to automating our simulation.  To answer the question, we are going to choose ```run.py``` as it will serve as the brain to our automation. 

At the time of writing this tutorial, ```crosscompute``` needs Python version 3.9 and higher.  Naturally, it follows that our command will use the ```python3.9```, our script, ```run.py```, and two placeholder variables ```{input_folder} {output_folder}``` that the ```crosscompute automation framework``` will provide to the script. 

    # script configuration
    scripts:
      - command: python3.9 run.py {input_folder} {output_folder}

With those three lines, we are done configuring our ```automate.yml``` file. 

![Creating our automate.yml file](/assets/gifs/Creating%20the%20automate-yml%20file.gif "Creating our automate.yml file")

## Activate ```automation``` virtual environment, run ```crosscompute autoamte.yml```

Up to this point we have our Bike Share model, ```bikeshare.py```, we have our ```run.py``` which we use to program to the model's interface. In the last section, we created our ```automate.yml``` file.  While we are not done setting up our automation, we are going to run ```crosscompute``` with our ```automate.yml``` file.  

First, let's activate our virtual environment, which we earlier called ```automation```. [We will be using the virtual environment created in the previous tutorial](https://github.com/kashfifahim/CrossComputeTutorials/tree/main/Chapter-1-How-To-Install-CrossCompute).  This virtual environment holds ```crosscompute``` package and all the related packages necessary for our automation.  Refer to the ["How to Install CrossCompute"](https://github.com/kashfifahim/CrossComputeTutorials/tree/main/Chapter-1-How-To-Install-CrossCompute) tutorial for an in depth walkthrough on how to set up your virtual environment.

Why run ```crosscompute automate``` now?  By running it now, ```crosscompute``` will create our automation's folder structure, think of it as a shortcut.

![Run ```crosscompute automate.yml```](/assets/gifs/runCrossComputeAutomate1.gif "Run ```crosscompute automate.yml```")

Let's examine the terminal in the ```gif``` above. 

Once we run ```crosscompute automate.yml``` a webserver on your local machine is created.  That webserver then serves our automation in a browser at the address ```127.0.0.1:7000```.  If we were to click on it, our default web-browser would open to our automation.  However, we're not quite there yet.  In the lines that follow, our machine is telling us that our ```variables.dictionary``` is not found.  That is normal since we have not created it.

On the other hand, look at the project directory.  After running ```crosscompute automate.yml```, ```crosscompute``` creates a new folder for us.  The folder, ```batches/a``` is the one we configured in our ```automate.yml``` file.  Within this folder we find an ```input``` folder, where we will now create and save a ```variables.dictionary``` file and an ```output``` folder, where our simulation's graph will be saved as a ```.png``` file. 

Before continuing, we can stop our webserver by pressing the ```ctrl + C``` buttons together on your keyboard.  
## ```batches > a > variables.dictionary```

Within the ```batches/a``` folder, let us create a ```variables.dictionary``` file.

![create variables.dictionary](/assets/gifs/create-var-dic-2.gif "create variables.dictionary")

What about creating an ```output_folder```?  As you saw earlier, from running ```crosscompute automate.yml```, ```crosscompute``` created the folder structures for our project.  We have our ```input``` folder, which now holds the ```variables.dictionary``` file. Once our automation is successfully run, the ```output``` folder will be where we will have our image output.

Let us now move on to updating our ```run.py```.

### Modifying run.py

We have four tasks that will modify ```run.py```.   These four tasks will connect our script to the variables found in the ```variables.dictionary``` file.  We will then use that connection to pass on the ```input_variables``` to our automation. 

Let's get started.

First, we are going to import ```argv``` from Python's ```sys``` library. ```argv``` will allow the ```command script``` in our ```automate.yml``` file to pass in the ```input_folder``` and ```output_folder``` as arguments to ```run.py```.  

    from sys import argv

After importing ```argv```, let us then create the ```input_folder``` and ```output_folder``` variables that ```argv``` will get as arguments.

    from sys import argv
    input_folder, output_folder = argv[1: ]

![Import argv from sys then create variables](/assets/gifs/argvForRun.gif "Import argv from sys then create variables to hold arguments passed from command line")

Next, we are going to use the ```json``` library to import the data from our ```variables.dictionary``` file.  

    variables = json.load(open(join(input_folder, 'variables.dictionary), 'rt'))

Now, let's connect the data to our simulation. We will replace the second, third, and fourth arguments in our call to ```run_simulation``` with the correspoinding data found in our variables.dictionary file.

    results = run_simulation(bikeshare, variables["p1"], variables["p2"], variables["num_steps"])

![connect variables.dictionary to our simulation](/assets/gifs/ConnectVariablesDictionary.gif "Connect variables.dictionary to our simulation")

We have just one more task to complete for our ```run.py``` file.   Just as we specified to load the data from the ```input_folder``` we need to now tell the script to save the figure image to the ```output_folder```.  For this we go to the last line of ```run.py``` where we have:

  plt.savefig(join(".", "simulation-graph.png"))

We need to change it so that it does not save to the root folder as it currently does.  Instead we are going to tell the script to save to the ```output_folder```. 

    plt.savefig(join(output_folder, "simulation-graph.png"))

![Save to output_folder](/assets/gifs/SaveToOutputFolder.gif "Save to output_folder")
## Ready For Launch

With our ```automate.yml``` file ready to go, our project structure with correct contents in place, and our virtual environment already activated from earlier, we are ready to run our automation. All that is left for us to do is in our terminal enter and run the following ```crosscompute automate.yml```. 

## Running Our Automation

In the terminal you should see ```crosscompute``` fire up and show you a local host address. If your terminal has permission to launch your web browser, your default web browser should have launched. If not, please copy the address in the terminal window, paste and enter into your default web browser.  Your web browser should then show you a link, which when clicked will take you to the automation. 

Then there will be a link for ```input``` and ```output```.  Clicking on ```input``` will take you to a page with numerical input fields. These fields will be pre-populated with the values defined in our ```variables.dictionary``` file.  The more interesting link is the ```output```.  The ```output``` link will take you to the figure generated from running our script with the variables found in the ```variables.dictionary``` file.

![Runninng our automation](/assets/gifs/RunningAutomationSuccess.gif "running our automation")

Congratulations on completing your first automation with ```CrossCompute Automation Framework```.

At this point we have reached the end of this tutorial. In the next tutorial, we are going to build on this automation. We are going use a ```csv``` file, filled with lots of values for our ```input variables```.  By doing this we are not just going to see one graph but one graph for each row of variable values found in the ```.csv``` file. 
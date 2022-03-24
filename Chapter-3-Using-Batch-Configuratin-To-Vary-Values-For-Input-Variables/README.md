![CrossCompute Logo](https://crosscompute.com/images/CrossCompute-LogoBrand-Horizontal-20200420.svg "CrossCompute logo")
# Chapter 3: Using Batch Configuration to Vary Values For Input Variables

![run-automation-folder](/assets/gifs/3-runautomation.gif "run-automation")
![101-folder](/assets/imgs/100%20folders.png "101 folder")
## Section 1: Recap of Tutorial 1

In the first chapter, we were introduced to the model of our Bike Share System, ```bikeshare.py```.  We then created ```run.py``` that would act as the brains of our automation.  ```run.py``` connected to the interface of our model, while also connecting to the ```crosscompute automation framework``` via the ```automate.yml``` file. 

Speaking of our ```yml``` file, in the last tutorial we configured the four essential sections of the file: the meta-section, the input and output configuration, the batch configuration section, and finally the script configuration. 

We then made some modifications to our ```run.py``` for connecting our inputs to the functions found in ```bikeshare.py```.  

Finally, when we ran our automation ```crosscompute``` launched a server in our local machine.  ```Crosscompute``` then served the automation in the form of a web based report.  Within this report we could see the inputs used for the automation as well as the output, an image of the activity chart used to represent our simulation. Now, in this chapter, we are going to build on everything from the previous tutorial.  

The key difference between the introductory tutorial and this current tutorial hinges on one idea: a lot more input varaibles.  What we are going to work on in this tutorial is take the same model but now feed it a hundred more input variable.  In return, we are going to expect a hundred more outputs in the form of a hundred activity figures, saved as a ```.png``` file.    

Let's get started.

## Section 2: What's In Our Project Folder

To start off, let us review the contents of our project folder.  What do we have?

![Image of project starter files](/assets/imgs/Ch3Start.png "Project starter files")

As mentioned earlier, we have our ```bikeshare.py``` file that holds the functions needed to run our simulation.  Then we have our ```run.py``` file and our ```automate.yml``` file. We also have a folder called ```batches```.  What's inside of that folder?

![Inside of batches folder](/assets/gifs/ch301.gif "Inside of batches")

When we configured the ```batches```section of our ```automate.yml``` file, we configured the creation of a folder called ```a```.  So inside ```batches``` we first have ```a```.  Then when we open ```a``` we see the folders ```debug```, ```input```, ```log```, and ```output```.  They key folders of interest are ```input```, where we have our ```variables.dictionary``` file, and the ```output``` folder, which holds the saved image of the figure generated from the simulation.

## Section 3: A little about batch configuration to vary values for input variables

In the last tutorials, we had a minimal configuration in the ```batches``` section of our ```automate.yml``` file.  The reason for that was because we just wanted our simulation to be automated for one set of data. That lone set of data was stored in a ```variables.dictionary``` file within the ```/batches/a/input``` folder. 

In this tutorial, we are going to build up on the first ```batch configuration```.  We are now going to provide our automation with a path to a ```batches.csv``` file. This ```csv``` file will not just hold one set of values for our ```input variables``` but will hold a hundred set of values. The automation will then yield, for each row of our ```batches.csv``` file, and record a simulation. Our ```automation``` will also manage the ```output_folder``` by creating a folder for each set of output images.

Let's get started.
## Section 4: A Look At Our ```batches.csv``` File

As promised, for this tutorial we are really going to test the ```crosscompute autoamtion framework``` by asking it to automate one hundred rows of data from a ```batches.csv```.  

![100-rows-of-data](/assets/gifs/100-batches-csv.gif "100-rows-of-data")

Our ```csv``` file is made up of three attributes, one for each input variable: p1, p2, and num_steps.  The values of ```p1``` and ```p2``` are random floating point numbers between 0.1 and 0.9.  Meanwhile, the values of ```num_steps``` are random integer values between ```10``` and ```60``` representing time intervals in minutes.

## Section 5: Configuring the ```batch configuration```

Next, let's configure the ```batches``` section of our ```automate.yml``` file.  

In our last tutorial, [](), we configured the ```batches``` section with a folder, which we simply set up as ```folder: batches/a```.  Now we're going to add another folder.

    # batches configuration
    batches:
      - folder: batches/a
      - folder: batches/p1{p1}-p2{p2}-numsteps{num_steps}

Our folder name here contains placeholder variables.  Why is that?  This is so that our folder structure can be linked to the set of input values our automation used from the ```.csv``` file.  

Next, we are going to provide our folder with ```configuration``` attribute which will have a ```path``` attribute. This ```path``` will point the automation to the location of the datasets with our ```.csv``` file, which we are going to name ```batches.csv```.

    # batches configuration
    batches:
      - folder: batches/a
    
      - folder: batches/p1{p1}-p2{p2}-numsteps{num_steps}
        configuration:
          path: datasets/batches.csv

Before we continue, let us get a quick recap of what is going on with our ```batches``` configuration.  

The first folder, which we configured in the last tutorial, genrally serves as a reference for the automation.  Now in the second folder we are configuring it so that the ```automation``` now has access to more input variables. Key point is that the ```input variables``` are still configured as earlier. The only difference is in the second cofiguration will automate and yield more results rather than one.

![Configuring-batches-section](/assets/gifs/3-batchescongfig.gif "Configuring batches section")

## Section 6: Create ```datasets``` folder, add ```batches.csv``` file

With our ```automate.yml``` now configured with the updated ```batches``` configuration, we now need to place our ```batches.csv``` inside a new directory called ```datasets```.

![Create-datasets-dir](/assets/gifs/3-mkdirdatasets.gif "Create datasets dir")

To create the ```datasets``` directory, first check you are in the project's root folder. Then you can create a new folder and name it ```datasets```.  

    mkdir datasets

Then we can move the ```batches.csv``` file into this newly created ```datasets``` directory.

![Batches-In-Datasets](/assets/imgs/batchesInDatasets.png "image of batche.csv inside datasets directory")

## Section 7: Running ```crosscompute automate.yml```

Up to now, we added a new configuration to our ```batches``` section.  We created a new folder ```datasets``` that holds our ```batches.csv``` file.  Now, we are ready to run our automation. 

Before running our automation, first check which folder you are currently in.  If you are still inside the ```datasets``` folder, change your directory and move up one level to the project folder directory that holds the ```automate.yml``` file.  Then once you are in your project's root directory, activate your ```virtual environment``` and then run ```crosscompute automate.yml```.

What should you be seeing?  Once you run ```crosscompute automate.yml```, you will first see an address where the web-app of your automation can be accessed via your localhost.  When you open your browser to that address, you will see a list of each automation with its ```input``` and ```output```.

![web-app-view](/assets/gifs/3-webappview.gif "web-app view of automation")

Meanwhile, in your project folder you will star to see the ```batches``` folder be populated with new folders. Each one is a completed simulation with the ```input``` variables sourced from our ```batches.csv``` file and an ```output``` image.  Once the automation completes your batches folder will hold 101 folders.

![run-automation-folder](/assets/gifs/3-runautomation.gif "run-automation")

![101-folder](/assets/imgs/100%20folders.png "101 folder")

## Section 8: Conclusion
With that we have completed our automation of simulating 100 rows of data.

This concludes the third tutorial in this introductory set of tutorials on the CrossCompute Automation Framework. If you have any questions, comments, or would like to reach out to us about helping you automate today reach out to us at ```contact@crosscompute.com```.  

The Bike Share Simulation was inspired by the simulation of the same name from Allen B. Downey's course on Models and Simulation.
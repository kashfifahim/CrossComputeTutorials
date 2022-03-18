# Chapter 4: Using Reference Folder to Set Default Values for Missing Variable

![TerminalView](/assets/gifs/Ch4ViewFromTerminal.gif "Terminal view")
![BrowserView](/assets/gifs/Ch4BrowserView.gif "Browser View")

## Section 1: Recap

Up to now, we discovered how we can use the ```crosscompute automation framework``` to configure an automation with a simple dataset.  Then, we found out how it can work with a dataset made up of one hundred rows of input variables.  Now in this tutorial, we are going to see how the ```crosscompute automation framework``` can manage datasets with missing variables.

## Section 2: Introduction

Up to now our automation requires three input variables. The first pair of input variables, ```p1``` and```p2```, simulate customers deciding to use, wait, or pass on using our the Bike Share System. Then we have our third input variable, ```num_steps```, that simulates a block of time, in minutes.  

For our given simulation, varying values for ```p1``` and ```p2``` would be beneficial for a team to simulate as many cases that simulate the random decision of a simulated customer.  One can then argue that varying ```num_steps``` may not yield any valuable insights for an analyst. 

In this tutorial, once again, we are going to build on our last tutorial.  We are going to take our ```batches.csv``` dataset and take out all the varied values of ```num_steps```.  In its place, we are going to set ```num_steps``` to one value of ```60```.  In a sense this will allow us to focus our simulation, zoom in to specific scenario, returning invaluable insights into the possible decision making of the customers.

With that said, let's get started.

## Section 3: A little about using reference folder to set default values for missing variables

Up to now we have learnd how to set up our automation with ```crosscompute automation framework```.  At the heart of our automations are our ```batch configurations```.  We used batches for different purposes.  In the first tutorial, [](), we had a minimal configuration in the ```batches``` section of our ```automat.yml``` file.  The reason for that was because we just wanted our simulation to be automated for one set of data. That lone set of data was stored in a ```variables.dictionary``` file within the ```/batches/a/input``` folder. 

In the second tutorial, [](), we built up on the first ```batch configuration```.  We now provided our automation with a path to a ```csv``` file that had many more sets of input variables. From that ```csv``` file, we wanted our automation to yield a simulation for each set of input data.

Now, in this third tutorial, we are going to build up on the prior two ```batch configuration```.  In this tutorial, we are going to explore how we can configure our automation to handle missing values for our variables.  

This ```batch configuration``` is meant to allow you to dig deeper into your data. By isolating one variable, you can now observe and record trends from varying the other two variables.  

Let's get started.
## Section 4: Picking up from previous tutorial

![Ch4Starter](/assets/gifs/Ch4Starter.gif "Chapter 4 Starter")

Let us take a quick look at our project to see what we should all have at the start of this tutorial.  

Within our project folder we should have our ```automate.yml``` file, the model of our simulation in ```bikeshare.py```, and a controller script in ```run.py```. Then, we should have a folder called ```datasets``` within which we should have a couple of files, ```batches.csv```--from the last tutorial--and ```batches2variables.csv``` which we will use in this tutorial.  Jumping back to the project folder, we should also have a folder called ```batches```, within which is another folder which was titled ```a``` and within that folder is where our ```variables.dictioanry``` file is located.  This ```variables.dictioanry``` file will play a key role in this tutorial so please make sure it is there. 

All these files and folders were created with a thorough walkthrough of their contents in the previous two tutorials, so if you are just joining this tutorial, please complete the earlier two tutorial before starting this one.
## Section 5: Configuring the ```batch configuration```

Our goal for this automation is from the three variables, ```p1```, ```p2```, ```num_steps```, that our model requires, we are going to keep one of the variables to a single value of ```60```. Then we are going to plug a new ```batches2variables.csv``` data source that only has values for ```p1``` and ```p2```.  

How are we going to set ```num_steps``` to a single value of ```60```?  We are going to use the ```variables.dictionary``` file to assign to ```num_steps``` the value of ```60```.  With this simple assignment, whenvever our automation comes upon the variable ```num_steps``` it is going to automatically use the value first initialized in ```variables.dictionary```. With the ```CrossCompute Automation Framework``` it is really that simple to keep a variable fixed with a single value. 

Next, let us go to the ```batches``` section of our ```automate.yml``` file.  

In the previous tutorila, [](), we configured the ```batches``` section with two folder.  The first folder was configured to hold a singel set of ```input variables``` that were pulled from the ```variables.dictionary```.  The second folder built on top of that first folder by now providing the ```automation``` with a ```csv``` file that provided the ```automation``` with more sets of values for our ```input_variables```.  The second folder configuration also organized the output folders with the variable name and value that was used, ```p1{p1}-p2{p2}-numsteps{num_steps}```.

Now, we are going to keep those two earlier configurations and add to it.  We're going to add another folder configuration, and another ```csv``` file.  However, instead of the ```csv``` file having three variables this time our ```csv``` file will only have two of the three variables. 

If you are thinking that configuring the ```automate.yml``` to work with three ```input_variables``` and then just giving it only two will cause problems for the ```autoamtion```.  You are right.  That is why for this ```batch``` configuration our ```folder``` configuration will also have a ```reference``` attribute.  

The ```reference``` attribute is going to be where our ```automation``` finds a value for the missing ```input_variable``` and uses that value for each set of ```input_variables``` found in the ```csv``` file. 

Let's configure our ```batches``` section.

From our previous work, our ```batches``` section has the following configuration.

    # batches configuration
    batches:
      - folder: batches/a
    
      - folder: batches/p1{p1}-p2{p2}-numsteps{num_steps}
        configuration:
          path: datasets/batches.csv

Let's first comment out the second folder and it's configurations.  Then, we are going to add our third folder. Within this third folder, add a ```reference``` attribute to the folder. The ```reference``` here will point to our first folder configuration where the three ```input_variables``` are sourced from the ```variables.dictionary```. along with a ```path``` to the location of the ```csv``` file with only sets of values for the ```p1``` and ```p2``` ```input_variables```.


    # batches configuration
    batches:
      - folder: batches/a
    
      # - folder: batches/p1{p1}-p2{p2}-numsteps{num_steps}
      # configuration:
      #  path: datasets/batches.csv
        
      - folder: batches/p1{p1}-p2{p2}
        reference:
          folder: batches/a
        configuration:
          path: datasets/batches2variables.csv

With just those simple configuration updates to our ```automate.yml``` file, we are ready to run our automation.

## Section 6: Running ```crosscompute automate.yml```
Once you are ready to run your automation, activate the virtual environment.  This is the virtual environment where you set up and installed the ```crosscompute``` package. You will know that your virtual environment is running when the name of your virtual environment is shown in parenthesis on your command line interface.

  ```bash
  (automation) kashfifahim@crosscompute BikeShare %
  ```

Then make sure that you are in the root of your project folder. Once there, you can now run ```crosscompute``` with your ```automate.yml``` file.

  ```bash
  (automation) kashfifahim@crosscompute BikeShare % crosscompute automate.yml
  ```

In your terminal, you should see the automation process the first batch configuration ```batches/a```.  From this first run, our missing variable, ```num_steps``` will be intialized to our value of ```60```.  

Next, ```crosscompute``` is going to create and serve our automation from a server in our local machine.

After that, in your terminal window, you will see each set of values from our ```batches2variables.csv``` file being processes and then served.

![TerminalView](/assets/gifs/Ch4ViewFromTerminal.gif "Terminal view")

The image below shows our ```automation``` from the browser.

![BrowserView](/assets/gifs/Ch4BrowserView.gif "Browser View")

## Section 7: Conclusion

With just a few modifications to our ```automate.yml``` file, the ```crosscompute automation framework``` was able to compute another 100 rows of data. More interestingly, this time around, it still processed all three input variables required by our model ```bikeshare.py```, but by initializing our ```variables.dictionary``` to a default value of ```60```, wihtout missing a beat the automation framework processed our automation flawlessly.

This concludes the fourth tutorial introducing you to the CrossCompute Automation Framework. If you have any questions, comments, or would like to reach out to us about helping you automate today reach out to us at ```contact@crosscompute.com```.  

The Bike Share Simulation was inspired by the simulation of the same name from Allen B. Downey's course on Models and Simulation.
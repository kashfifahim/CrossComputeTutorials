# Chapter 3: Using Batch Configuration to Vary Values For Input Variables

## Section 0: Summary

## Section 1: Recap of Tutorial 1

In the first chapter, we were introduced to the model of our Bike Share System, ```bikeshare.py```.  We then created ```run.py``` that would act as the brains of our automation.  ```run.py``` connected to the interface of our model, while also connecting to the ```crosscompute automation framework``` via the ```automate.yml``` file. 

Speaking of our ```yml``` file, in the last tutorial we configured the four essential sections of the file: the meta-section, the input and output configuration, the batch configuration section, and finally the script configuration. 

We then made some modifications to our ```run.py``` for connecting our inputs to the functions found in ```bikeshare.py```.  

Finally, when we ran our automation ```crosscompute``` launched a server in our local machine.  ```Crosscompute``` then served the automation in the form of a web based report.  Within this report we could see the inputs used for the automation as well as the output, an image of the activity chart used to represent our simulation. Now, in this chapter, we are going to build on everything from the previous tutorial.  


## Section 2: A little about batch configuration to vary values for input variables

In the last tutorials,[](), we had a minimal configuration in the ```batches``` section of our ```automat.yml``` file.  The reason for that was because we just wanted our simulation to be automated for one set of data. That lone set of data was stored in a ```variables.dictionary``` file within the ```/batches/a/input``` folder. 

In this tutorial, we are going to build up on the first ```batch configuration```.  We are now going to provide our automation with a path to a ```csv``` file. This ```csv``` file will not hold one set of values for our ```input variables``` but will hold a dozen set of values. For each dozen set of values, the automation will yield and record a simulation in the form of a graph saved as a ```.png``` image. Our ```automation``` will also manage the ```output_folder``` by creating a folder for each set of output images.

Let's get started.
## Section 3: Starting from last tutorial

## Section 4: Configuring the ```batch configuration```

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

A quick recap of what is going on with our ```batches``` configuration.  The first folder, which we configured in the last tutorial, genrally serves as a reference for the automation.  Now in the second folder we are configuring it so that the ```automation``` now has access to more input variables. Key point is that the ```input variables``` are still the same kind as configured earlier in the first folder. The only difference is in the second cofiguration will automate and yield more results rather than one.

With our ```automate.yml``` now configured with the updated ```batches``` configuration, we can go ahead and run the automation.

## Section 5: Running ```crosscompute automate.yml```

## Section 6: Inspecting ```batch``` folder

## Section 7: Conclusion
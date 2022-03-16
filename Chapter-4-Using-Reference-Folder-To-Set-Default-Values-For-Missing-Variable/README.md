# Chapter 4: Using Reference Folder to Set Default Values for Missing Variable

## Section 0: Summary

## Section 1: Recap

First, we discovered how to configure our automation with a simple dataset.  Then, we found out how to work with a dataset made up of one hundred rows of input variables.     

## Section 2: A little about using reference folder to set default values for missing variables

Up to now we have learnd how to set up our automation with ```crosscompute automation framework```.  At the heart of our automations are our ```batch configurations```.  We used batches for different purposes.  In the first tutorial, [](), we had a minimal configuration in the ```batches``` section of our ```automat.yml``` file.  The reason for that was because we just wanted our simulation to be automated for one set of data. That lone set of data was stored in a ```variables.dictionary``` file within the ```/batches/a/input``` folder. 

In the second tutorial, [](), we built up on the first ```batch configuration```.  We now provided our automation with a path to a ```csv``` file that had many more sets of input variables. From that ```csv``` file, we wanted our automation to yield a simulation for each set of input data.

Now, in this third tutorial, we are going to build up on the prior two ```batch configuration```.  In this tutorial, we are going to explore how we can configure our automation to handle missing values for our variables.  

This ```batch configuration``` is meant to allow you to dig deeper into your data. By isolating one variable, you can now observe and record trends from varying the other two variables.  

Let's get started.
## Section 3: Picking up from previous tutorial

## Section 4: Configuring the ```batch configuration```

Let us go to the ```batches``` section of our ```automate.yml``` file.  

In the previous tutorila, [](), we configured the ```batches``` section with two folder.  The first folder was configured to hold a singel set of ```input variables``` that were pulled from the ```variables.dictionary```.  The second folder built on top of that first folder by now providing the ```automation``` with a ```csv``` file that provided the ```automation``` with more sets of values for our ```input_variables```.  The second folder configuration also organized the output folders with the variable name and value that was used, ```p1{p1}-p2{p2}-numstes{num_steps}```.

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

Now we are going to add our third folder. Then add a ```reference``` attribute to the folder. The ```reference``` here will point to our first folder configuration where the three ```input_variables``` are sourced from the ```variables.dictionary```. along with a ```path``` to the location of the ```csv``` file with only sets of values for the ```p1``` and ```p2``` ```input_variables```.


    # batches configuration
    batches:
      - folder: batches/a
    
      - folder: batches/p1{p1}-p2{p2}-numsteps{num_steps}
        configuration:
          path: datasets/batches.csv
        
      - folder: batches/p1{p1}-p2{p2}-numsteps-ref
        reference:
          folder: batches/a
        configuration:
          path: datasets/batches-p1-p2.csv



## Section 5: Running ```crosscompute automate.yml```

## Section 6: Inspecting the ```batch``` folder

## Section 7: Conclusion
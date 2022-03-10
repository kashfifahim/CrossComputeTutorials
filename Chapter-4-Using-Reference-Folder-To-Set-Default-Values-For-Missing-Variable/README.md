# Chapter 4: Using Reference Folder to Set Default Values for Missing Variable

## Section 0: Summary

## Section 1: Recap

## Section 2: A little about using reference folder to set default values for missing variables

The last tutorials, we used batches for different purposes.  In the first tutorial, [](), we had a minimal configuration in the ```batches``` section of our ```automat.yml``` file.  The reason for that was because we just wanted our simulation to be automated for one set of data. That lone set of data was stored in a ```variables.dictionary``` file within the ````/batches/a/input``` folder. 

In the second tutorial, [](), we built up on the first ```batch configuration```.  We now provided our automation with a path to a ```csv``` file that had many more sets of input variables. From that ```csv``` file, we wanted our automation to yield a simulation for each set of input data.

Now, in this third tutorial, we are going to build up on the prior two ```batch configuration```.  Here we are going to keep one of the three variables with a constant value, ```60```. In other words, we are going to isolate one variable and vary the other two. 

This ```batch configuration``` is meant to allow you to dig deeper into your data. By isolating one variable, you can now observe and record trends from varying the other two variables.  

Let's get started.
## Section 3: Picking up from previous tutorial

## Section 4: Configuring the ```batch configuratin```

## Section 5: Running ```crosscompute automate.yml```

## Section 6: Inspecting the ```batch``` folder

## Section 7: Conclusion
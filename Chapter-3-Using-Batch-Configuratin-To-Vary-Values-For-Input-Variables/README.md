# Chapter 3: Using Batch Configuration to Vary Values For Input Variables

## Section 0: Summary

## Section 1: Recap

## Section 2: A little about batch configuration to vary values for input variables

In the last tutorials,[](), we had a minimal configuration in the ```batches``` section of our ```automat.yml``` file.  The reason for that was because we just wanted our simulation to be automated for one set of data. That lone set of data was stored in a ```variables.dictionary``` file within the ```/batches/a/input``` folder. 

In this tutorial, we are going to build up on the first ```batch configuration```.  We are now going to provide our automation with a path to a ```csv``` file. This ```csv``` file will not hold one set of values for our ```input variables``` but will hold a dozen set of values. For each dozen set of values, the automation will yield and record a simulation in the form of a graph saved as a ```.png``` image. Our ```automation``` will also manage the ```output_folder``` by creating a folder for each set of output images.

Let's get started.
## Section 3: Starting from last tutorial

## Section 4: Configuring the ```batch configuration```

## Section 5: Running ```crosscompute automate.yml```

## Section 6: Inspecting ```batch``` folder

## Section 7: Conclusion
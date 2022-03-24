![CrossCompute Logo](https://crosscompute.com/images/CrossCompute-LogoBrand-Horizontal-20200420.svg "CrossCompute logo")
# Tutorial 1: Getting Started

## Setting Up Your Environment
Before we dive into creating our automation, we need to first prepare our project environment.  For this section of the tutorial, we are using a machine running Linux's Ubuntu distribution, version 20.04 with Long Term Support (LTS).  Our machine has 1 CPU, 1GB of RAM and 25 GB or storage and is connected to the internet.   

## Is Your Linux Distro Up to Date?
Let's start by opening up our command line interpreter, also known as the terminal. We need to check if your Linux distribution, in this case, Ubuntu, is up to date.  To do this type the following command in your terminal:

    sudo apt update

This command will check for and return how many packages in your system can be upgraded. To see what packages can be upgraded type in:

    apt list --upgradeable

If you are ready to upgrade your distribution, go ahead and run 

    sudo apt upgrade

After this command completes execution your machine's operating system is now up to date and we're ready to continue.
## Do You Have Python3.9 Installed?
In order to work with the latest version of CrossCompute, we are going to need Python version 3.9 and higher. To begin, let's check if your operating system already has Python3.9.  In your terminal application, type: 

    python3.9

If you do not have Python version 3.9, the terminal is going to return the message: 

    Command python3.9 not found, but can be installed with: 
    apt install python3.9

Following the suggestion from your terminal, go ahead and install python3.9 py entering the suggested command

    apt install python3.9

Now that you have installed python3.9, run the earlier command:

    python3.9

You now should see the following

    Python 3.9.5 (default, Nov 23 2021, 15:27:38) 
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

which verifies to us that you have successfully installed Python3.9.  To get out of the Python3.9 interpreter type the following into the prompt:

    exit()

## Do You Have pip?
As you may have heard, the Python programming language is one of the most popular programming languages out there.  This means there are a lot of libraries, frameworks, projects out there for you to learn, explore, and adopt into your day to day activities.  For us to be able to download and install such projects, commonly referred to as packages, we are going to need a package installer for Python.  Meet pip.  pip is what we will be using to download and install CrossCompute on to your machine.  

First let's check if your system has pip already installed.  Type the following command into your terminal:

    python3.9 -m pip --version

If pip has not been already installed you are going to receive the following message:

    No module named pip

In this case, let's get pip installed in your machine. Type the follwing into your interpreter

    apt install python3.9 -m pip

The above command will download and then install pip it into our machine.

To confirm pip having been installed type the following command

    python3.9 -m pip --version

You should see the interpreter return a message similar to the one below

    pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.9)

## Do We Have Python3.9's venv?
Next, we are going to need another import Python3.9 module: venv, short for virtual environment.  

What is a virtual environment?  A virtual environment, in short, allows us to install packages in an environment that is separate from your system's environment.  

You might wonder, so what?  Well, the significance of a virtual environment is that it allows you to set up projects in isolation. As a result of using a virtual environment what you use for one project doesn't conflict with another.  

For our purposes of creating automations, having the space to control what packages, tools, and the likes are used is crucial.  

Let's first check if you do or do not have Python3.9's venv module by entering the following into your terminal and then pressing Enter:

    python3.9 -m venv --automation

If your system does not have Python3.9's venv module ready and available, you are going to get this message back from your machine:

    The virtual environment was not created successfully because ensurepip is not available.  On Debian/Ubuntu systems, you need to install the python3-venv package using the following command.

    apt install python3.9-venv
    
    You may need to use sudo with that command.  After installing the python3-venv package, recreate your virtual environment.

Let's follow the recommended command and enter the following into your terminal and then pressing Enter:

    apt instapp python3.9-venv

After the system installs the venv package let us try again to create our new virtual environment, with the name automation:

    python3.9 -m venv automation

Did it work?  If nothing happens, your terminal just executes the command and returns to you without any error messages, then yes python created a virtual environment with the name automation. You can check this my listing the files in your current directory with the command ```ls``` and you will find a directory titled 'automation'. 

Next, let's activate our virtual enviroment by typing the following command and then pressing Enter:

    source automation/bin/activate

You will now notice that ```(automation)``` shows up at the far left side of the terminal's prompt.  This is how you will recognize whether or not your virtual environment is active.  

## Check Packages Inside Activated Virtual Environment
With our virtual environment activated, we are ready to install CrossCompute to our machine. But, before we do that, let's just quickly check at what packages are already included in our freshly activated virtual environment.  Type the following into your terminal and then press Enter

    pip list

Your machine should return you a list of packages, with their respective version numbers, like below

    Package       Version
    ------------- -------
    pip           20.0.2 
    pkg-resources 0.0.0  
    setuptools    44.0.0 

Now we know what packages are included in our virtual environment, we are ready to install CrossCompute.

## Installing CrossCompute

Up to this point we (i) updated our Ubuntu distribution, (ii) installed Python3.9, (iii) installed pip, python's package manager, (iv) installed and activated our virtual environment named automation and checked to see what packages were included in the environment (v) and now we're ready to install CrossCompute. 

In your terminal's command line type the following command and then press Enter

    pip install crosscompute

Your machine will then install CrossCompute and it's dependencies.  Let's check to see that we have successfully installed CrossCompute by checking pip's list of packages installed in the machine

    pip list

which will return the following list

    Package                        Version
    ------------------------------ -------
    crosscompute                   0.9.1.2  
    hupper                         1.10.3 
    importlib-metadata             4.10.1 
    invisibleroads-macros-disk     1.2.1  
    invisibleroads-macros-log      1.0.4  
    invisibleroads-macros-security 1.0.1  
    invisibleroads-macros-text     1.1.1  
    Jinja2                         3.0.3  
    Markdown                       3.3.6  
    MarkupSafe                     2.0.1  
    PasteDeploy                    2.1.1  
    pip                            20.0.2 
    pkg-resources                  0.0.0  
    plaster                        1.0    
    plaster-pastedeploy            0.7    
    pyramid                        2.0    
    pyramid-jinja2                 2.8    
    ruamel.yaml                    0.17.20
    ruamel.yaml.clib               0.2.6  
    setuptools                     44.0.0 
    tomli                          2.0.0  
    translationstring              1.4    
    venusian                       3.0.0  
    waitress                       2.0.0  
    watchgod                       0.7    
    WebOb                          1.8.7  
    zipp                           3.7.0  
    zope.deprecation               4.4.0  
    zope.interface                 5.4.0  

Congratulations, you now have successfully set up your machine and installed CrossCompute in your virtual environment named ```automation```. We will be using this virtual environment to run our automations using the crosscompute framework.  

To deactivate the virtual environment simply write ```deactivate``` and press enter into your terminal.  This ends the virtual environment.  

The next time you want to activate the ```automation``` environment, enter the following into your terminal prompt:

    source LOCATION_OF_YOUR_AUTOMATION_FOLDER\bin\activate

You and your machine are now ready to continue on to the next tutorials.

This concludes the first tutorials introducing you to the CrossCompute Automation Framework. If you have any questions, comments, or would like to reach out to us about helping you automate today reach out to us at ```contact@crosscompute.com```.  

The Bike Share Simulation is inspired by the simulation from Allen B. Downey's course on Models and Simulation.

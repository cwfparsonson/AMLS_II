AMLS II
=======

This code is for use within the UCL Electronic Engineering AMLS II module (ELEC0135).

Setup
-----
Open Git Bash. Change the current working directory to the location where you wants to
clone this GitHub project, and run::

    $ git clone https://github.com/cwfparsonson/AMLS_II

It is recommended that you run this project in a virtual environment. A good virtual
environment manager is Anaconda: https://anaconda.org/

**Your environment or machine must be using Python 3.6**

In your Python 3.6 environment or machine, from the route directory of where you
cloned this project, install the required packages by running::

    $ python -m pip install -r requirements.txt

To test that your packages have installed correctly, open `Day3/Day3_MLP/DAY3_MLP.ipynb` 
in a Jupyter Notebook and try to run the cells.

If everything has been correctly installed, you should be able to run all Jupyter Notebook
scripts in each of the folders.

Issues
------
The following issues have previously been encountered and resolved:

- **Problems with `dlib`**: For `dlib==19.16.0` to install, you may need to separately install `cmake` 
  by running `python -m pip install cmake`. For cmake to work, you may also need to install
  a C++ compiler with `sudo apt-get install g++` (Linux). You should then be able to run
  `python -m pip install dlib==19.16.0`

- **Jupyter accessing environment**: For your environment to be selectable as a kernel in Jupyter Notebook, once you
  have installed the required packages into your virtual environment called `<env_name>`,
  you may need to run `python -m ipkykernel install --user --name <env_name> --display-name "<env_display_name>"`
  so that you can select your `<env_name>` in the Jupyter Notebook under Kernel -> Change kernel -> `<env_name>`.

- **Linux memory errors**: If you are partitioning your drive to run Linux, you may encountary tmp memory errors
  when installing the `requirements.txt` file. To solve this, you will need to free up swap memory
  on your Linux machine so the packages can be installed: https://askubuntu.com/questions/178712/how-to-increase-swap-space

If you have any issues, please post your questions on the Moodle forum: https://moodle.ucl.ac.uk/course/view.php?id=20557

AMLS II
=======

This code is for use within the UCL Electronic Engineering AMLS II module (ELEC0135).

Setup
-----
**If using Google Colab to run the code, do the following steps:**

Open the .ipynb file that you would like to run in GitHub. 
Then, in the URL above, change **github.com** to **githubtocolab.com** and press Enter.

In the first cell, clone this GitHub project, and run::

    !git clone https://github.com/cwfparsonson/AMLS_II
    
Go to the directory where the file you initially opened is saved, using %cd.

For example::
    If you opened the file Lab1_MLP.ipynb initially.
    You add a code line at the top of the code to clone the repository.
    Then, you add a new code cell that you use to enter the corresponding directory, %cd AMLS_II/Lab1/Lab1_MLP/
    
Now, in a new cell at the top of the code, run the following lines to install the needed packages::
    
    For Lab2:
        !pip install --upgrade tf_slim
        
**If using Anaconda virtual environment manager to run the code, do the following steps:**

Download Git using the following link::

    https://git-scm.com/downloads

Change the current working directory to the location where you want to
clone this GitHub project, and run::

    git clone https://github.com/cwfparsonson/AMLS_II

If you have installed Anaconda, you can create a new environment with Python 3.6 called amls2 by running::

    conda create --name amls2 python=3.6

In your Python 3.6 environment or machine, from the route directory of where you
cloned this project, install the required packages by running::

    For Lab1 - MLP:
        pip install tensorflow==1.12.0
        pip install keras==2.2.4
        pip install pillow
        pip install opencv-python
        conda install -c conda-forge dlib
    
    For Lab1 - MoE:
        pip install tensorflow==1.12.0
        pip install keras==2.2.4
        pip install seaborn==0.7.1
        pip install pydot==1.4.1
    
    For Lab2:
        pip install tensorflow==1.12.0
        pip install matplotlib
        pip install dask --upgrade

To test that your packages have installed correctly, open ``Lab1/Lab1_MLP/lab1_MLP.ipynb``
in a Jupyter Notebook and try to run the cells.

If everything has been correctly installed, you should be able to run all Jupyter Notebook
scripts in each of the folders.

**Note that if you are using windows, please uncomment line 112 in Lab1/Lab1_MLP/lab3_data.py**

**If using Jupyter Online to run the code, do the following steps:**

In the first cell, clone this GitHub project, and run::

    !git clone https://github.com/cwfparsonson/AMLS_II
    
Open the binder folder and open the .ipynb file you want to run.

Now, in a new cell at the top of the code, run the following lines to install the needed packages::
    
    For Lab1 - MLP:
        !pip install tensorflow==1.12.0
        !pip install keras==2.2.4
        !pip install pillow
        !pip install opencv-python
        !pip install opencv-python-headless
        !conda install -y -c conda-forge dlib
    
    For Lab1 - MoE:
        !pip install tensorflow==1.12.0
        !pip install keras==2.2.4
        !pip install seaborn
        !pip install pydot==1.4.1
        !pip install 'h5py==2.10.0' --force-reinstall
    
    For Lab2:
        !pip install tensorflow==1.12.0
        !pip install matplotlib
        !pip install dask --upgrade


**Note that if you are using windows, please uncomment line 112 in Lab1/Lab1_MLP/lab3_data.py**

Issues
------
The following issues have previously been encountered and resolved:

- **Problems with dlib**: For ``dlib==19.16.0`` to install, you may need to separately install ``cmake``
  by running ``python -m pip install cmake``. For ``cmake`` to work, you may also need to install
  a C++ compiler with ``sudo apt-get install g++`` (Linux). You should then be able to run
  ``python -m pip install dlib==19.16.0``

- **Jupyter accessing environment**: For your environment to be selectable as a kernel in Jupyter Notebook, once you
  have installed the required packages into your virtual environment called ``<env_name>``,
  you may need to run ``python -m ipkykernel install --user --name <env_name> --display-name "<env_name>"``
  so that you can select your ``<env_name>`` in the Jupyter Notebook under Kernel -> Change kernel -> ``<env_name>``.

- **Linux memory errors**: If you are partitioning your drive to run Linux, you may encounter tmp memory errors
  when installing the ``requirements.txt`` file. To solve this, you will need to free up swap memory
  on your Linux machine so the packages can be installed: https://askubuntu.com/questions/178712/how-to-increase-swap-space

If you have any questions or issues, please do not hesitate to raise a GitHub issue 
on this AMLS_II repository. To raise an issue, at the top of the window at https://github.com/cwfparsonson/AMLS_II,
go to Issues -> New issue, and fill out your post. We will answer your issues/questions ASAP.

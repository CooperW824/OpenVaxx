# OpenVaxx
 An Open Source Vaccine Passport Demo APP for the 2021 Congressional App Challenge

## Building and Running the App 
We recomend building a Python 3.7+ environment, but we are pretty confident it could work in most Python 3 environments.

We also recomend running this in a virtual environment during development which can be done a variety of ways:

#### Creating a venv:

Navigate to the folder of the repository using 

-       $ cd path/to/repo

Then use command:

-       $ python3 -m venv venv

#### Activating the venv:

-   Linux
    -       $ . venv/bin/activate

- Windows
    -       $ ./venv/scripts/activate

#### Installing Necessary Modules:

To install the various modules needed for the program you can run the pip command below from the shell.

-       $ python3 -m pip install pandas numpy qrcode opencv-python pyzbar pysimplegui

**Disclaimer: Pyzbar on windows needs some certain DLLs they can be found on Microsoft's website, download the one required for your version of python (32bit or 64bit): [https://www.microsoft.com/en-US/download/details.aspx?id=40784](https://www.microsoft.com/en-US/download/details.aspx?id=40784)**
This will install needed modules for the project to run.

#### Running the Project

The project can now be run like any other python project

While inside the VENV run the command

        python3 -m openvaxx.py

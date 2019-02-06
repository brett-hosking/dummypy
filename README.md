# dummypy
A package dummy template for Python 


## How to install virtualenv:

### Install **pip** first

    sudo apt-get install python3-pip

### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 


### Create virtualenv using Python3
    virtualenv -p python3 myenv

### Instead of using virtualenv you can use this command in Python3
    python3 -m venv myenv

>you can use any name insted of **myenv**

## Install Package

    git clone https://github.com/brett-hosking/dummypy.git

### Install requirements from file 
    pip install -r requirements.txt

### Run pip to install package (locally)
    pip install .

## Upgrade Package (local)
    git pull
    pip install . --upgrade


## Notes 

### Create a requirements.txt file in the format:
    feedparser==5.1.3
    wsgiref==0.1.2
    django==1.4.2
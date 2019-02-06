# A dummy package template for Python 


## Install and setup virtualenv:

### Install **pip** first

    sudo apt-get install python3-pip

### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

### Create virtualenv using Python3
    virtualenv -p python3 myenv

### Instead of using virtualenv you can use this command in Python3
    python3 -m venv myenv

>you can use any name insted of **myenv**

## Activate virtual environment

    python3 -m venv myenv

>the environment can be deactivated with the **deactivate** command

## Install Package

    git clone https://github.com/brett-hosking/dummypy.git

### Install requirements from file 
    pip install -r requirements.txt

### Run pip to install package (locally)
    pip install .

## Upgrade Package (local)
    git pull
    pip install . --upgrade

## Notes for building packages

### Create a requirements.txt file in the format:
    feedparser==5.1.3
    wsgiref==0.1.2
    django==1.4.2


## Useful commands 

### List Python packages
    pip list


## Creating Documentation 

### install sphinx 
    pip install sphinx 
    pip install sphinx_rtd_theme

### setup docs 
    mkdir docs 
    cd docs
    sphinx-quickstart

### Edit and Make
    edit source/conf.py -> html_theme = "sphinx_rtd_theme"; html_theme_path = ["_themes", ]
    make html

### Upload docs 
Go to https://readthedocs.org
Login using github and create service hook
Go to import and add repository details 

    cd docs 
    make clean 
    cd ../
    git add docs 
    git commit -am 'added docs'
    push

#Project: Item Catalog Application

## Project Description

This project is a demo application for the Udacity Full Stack Web Developer Nanodegree Program.It is a web application built using **fask** framework **(python)**. The web application provides a list of items within a variety of categories and integrates third party user registration and authentication. Authenticated users should have the ability to post, edit, and delete their own items.

##Getting Started
###Installing the Vagrant VM
### Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

### VirtualBox
VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.
Launch the Vagrant VM (by typing vagrant up in the directory Catalog/vagrant from the terminal). 
    
Run your application within the VM by typing python3 application.py into the Terminal.
Access the application by visiting **http://localhost:8000** locally on your browser.
    Clone the Catalog repository. 
    
    
###Run the virtual machine!
Using the terminal, change directory to catalog (cd catalog), then type **vagrant up** to launch your virtual machine.

## Project functionality
- The user can browse items based on particular category out of availble categories.
- After **logged in with google** authentication, the user can add their own category and items.
- User can modify and delete categories and items those are created by them.
- The user who creates a category can only manage (add/edit/delete) items of that category

###Running the Catalog App
```
git clone https://github.com/RamonLugo/FSWDND-catalog
cd catalog
vagrant up
vargant ssh
cd /vagrant
cd catalog
python3 database_setup.py
python3 createDataForDatabase.py
python3 application.py
```
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt. To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run **vagrant up** again before you can log into it.

Now that you have Vagrant up and running type **vagrant ssh** to log into your VM. change to the **/vagrant** directory by typing **cd /vagrant**. This will take you to the shared folder between your virtual machine and host machine.

Type **ls** to ensure that you are inside the directory that contains project.py, database_setup.py, createDataForDatabase.py and two directories named 'templates' and 'static'

Type **python3 database_setup.py** to initialize the database.  Type **python3 createDataForDatabase.py** to create the sample data.

Type **python project.py** to run the Flask web server. In your browser visit **http://localhost:8000** to view the Catalog app. You should be able to view, add, edit, and delete items and categories.

Type `Ctrl-D`, to logout of it and shut it down using this command **vagrant halt**.

### API Endpoints (JSON Endpoints)
- Get all categories by calling the following url:
    `http://localhost:8000/categories/JSON`

- Get all items of particular category by calling the following url:
    `http://localhost:8000/category/<int:category_id>/items/JSON` Just supply the Category Id (integer).
    
- Get one item of a particular category by calling the following url:
    `http://localhost:8000/category/<int:category_id>/<int:items_id>/JSON` Just supply the Category Id (integer) and the Item Id (integer).
    
###Cross-site Request Forgery Protection

The site protects against cross-site request forgery. A cookie is stored in the client. When a user logs in, adds, edits or deletes an item, the contents of this cookie is checked to make sure it matches the value on the server. If it does not match or is missing, no change to the database will be made.

## Required Libraries (see - requirements.txt)
The project code requires the following software:

* Python 3.x.x
* [SQLAlchemy](http://www.sqlalchemy.org/) 1.3.3 or higher (a Python SQL toolkit)
* [Flask](http://flask.pocoo.org/) 1.0.2 or higher (a web development microframework)
* The following Python packages:
    * oauth2client 4.1.3 or higher
    * requests 2.22.0 or higher
    * httplib2 0.13.0 or higher
    * Werkzeug 0.15.4 or higher
    * itsdangerous 1.1.0 or higher
    * Jinja2 2.10.1 or higher

Run `pip  install  -r  requirements.txt` to install requred modules.

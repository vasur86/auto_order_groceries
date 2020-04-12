# auto_order_groceries


##Run script to Order
- Login to Amazon
- Add items to the cart from whole foods
- Make sure the payment details are up to date 
- Make sure the delivery address is update to date


Open your terminal(mac/linux) or git bash(windows)
Make sure your current directory is the one we created earlier named "order_auto"
Input the command below in the terminal:
```
python order.py
Amazon.com SignIn Username: 
Amazon.com SignIn Password: 
```
or 
```
python order.py -u your-amazon-user-name -p your-amazon-password
```

##How to Install (one time setup):
###Step 1: Check if Python and pip is installed
Where to get Python 3.4+: https://www.python.org/downloads/
1. Python 3.4+ installed
2. Pip installed(should come packaged with Python)
```
# check if python is installed - it should return something similiar to this "Python 3.6.7"
python --version

# check if pip is installed - it should return something similiar to this "pip 19.1.1 from <your_path>"
pip --version
```

###Step 2: Download chrome driver
Download the driver that matches the version of chrome that your running and correct operating system: https://sites.google.com/a/chromium.org/chromedriver/downloads

If you do not know your chrome version, copy and paste this to your url search and you will get your version:
chrome://settings/help

Add path of the chromedriver to PATH environment variable.


###Step 3: Folder/dir setup
Open your terminal(mac/linux) or git bash(windows)
Make a folder to store all of the contents we will be working with and navigate to it in the terminal:
```
# make directory/folder to store our project files 
mkdir order_auto
# change directory to the directory we just created
cd order_auto
```

###Step 4: Installing virtualenv and creating our virtual environment
Make sure your current directory is the one we created earlier named "order_auto"
Lets install, create, and activate our virtual environment with the commands below:
```
# This command will install virtualenv
pip install virtualenv

# This command will create our virtual env with python3 installed
virtualenv -p python3 env
# ONLY RUN THIS COMMAND if you get an error from the above command(windows users issue perhaps)
virtualenv -p python env

# This command will activate our virtual envirnoment and allow us to work with contained dependencies
source env/bin/activate
# ONLY RUN THIS COMMAND if the command from above causes error Windows might have this path instead for activating virtual environment
source env/Scripts/activate
```

###Step 5: Installing dependencies
Input the command below in the terminal:
```
pip install -r requirements.txt
```

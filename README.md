# Invoicer
A webapp that generates "Tax Invoice" within few steps. The aim of this webapp is to simplify the process of creating the tax invoice by just entering some info. The invoice's template is used to fill the details entered by the user. With its responive design, this webapp is easy to use in phones, tablets and desktops.

#Frameworks and Libraries used
..* Django 1.8.18
..* Material Design Lite 1.3.0

#Getting Started
Python 3.X and virtualenv must be installed on your OS.

#How to run it locally
First, install virtualenv

For Mac OS / Linux
```bash
	pip3 install virtualenv
```
For Windows
```bash
	pip install virtualenv
```

Clone this repo
```bash
	git clone https://github.com/rishabhnehra/Invoicer.git
```

Change the directory
```bash
	cd Invoicer
```

Create a virtual environment of any name (say venv)
```bash
	virtualenv venv
```

Activate that virtual environment
```bash
	source venv/bin/activate
```

Install the required dependencies
```bash
	pip install -r requirements.txt
```

Change the directory into invoicer
```bash
	cd invoicer
```

Run the migrate command
```bash
	python manage.py migrate
```

Create a super user to access the Django admin panel, and enter the required information
```bash
	python manage.py createsuperuser
```

Now run the development server by
```bash
	python manage.py runserver
```

# License
```
 Copyright 2017 Rishabh Nehra

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
   
 ```
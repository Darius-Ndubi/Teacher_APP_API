[![Build Status](https://travis-ci.org/Darius-Ndubi/Teacher_APP_API.svg?branch=master)](https://travis-ci.org/Darius-Ndubi/Teacher_APP_API) [![Coverage Status](https://coveralls.io/repos/github/Darius-Ndubi/Teacher_APP_API/badge.svg?branch=master)](https://coveralls.io/github/Darius-Ndubi/Teacher_APP_API?branch=master)

# Teacher APP API

Teacher APP is a platform that allows teacher to manage day to cay class activities from the comfort of an internet enabled device. It assists in keeping track of students from any location


#### Getting Started
Go to https://github.com/Darius-Ndubi/Teacher_APP_API.git
Download or clone the repository to your local machine. 
Open the project using your favorite IDE

----
#### Prerequisites
 - Python3.
 - Virtual environment.
 - Django
 - Docker
 - Postman or insomnia
 - Postgres
 - Browser e.g Chrome, firefox

#### Application requirements
Create a .env_sample and in it add:
  - DATABASE_NAME=db_name
  - DATABASE_USER=db_owner
  - DATABASE_PASSWORD=db_user_password
  - DATABASE_HOST=db_host
  - DATABASE_PORT=db_port

- SECRET_KEY='Applications_secret_key'
- APP_DEBUG_MODE=App_debug_mode
 
 Save the file.

 ----
#### Setting up without docker
Navigate to your project folder and open it using the terminal.
Create a virtual environment. *virtualenv name_of_virtual_environment preferably `venv`.
Folder with the 'name_of_virtual_environment' will be created and that is our environment.
Clone this repo to your local computer using git clone https://github.com/Darius-Ndubi/Teacher_APP_API.git
Activate the environment via `source venv/bin/activate. Switch into the project directory. 
run source .env_sample
Install the project's dependencies by running pip install -r requirements.txt
Initialize the app migrations with `python manage.py makemigrations` run migrations with `python manage.py migrate`
Start the development server with the command `python manage.py runserver`

To stop the development server run `Ctrl+C` command on the terminal running the server.
  

#### Setting up with docker [Most preferred due the uniformity offered using this environment]
Navigate to your project folder and open it using the terminal.
Install docker 
[Link](https://docs.docker.com/install/)
Use the documentation to install docker on your machine. Always works.
Clone the repository https://github.com/Darius-Ndubi/Teacher_APP_API.git
Change Directory into tk-django. Setup the .env file following directives from  sample.env file or Steps above.
*run* `docker-compose build` to build the development image. This takes some time. 😅 :sweat_smile:
*then* `docker-compose up` to start up the application in docker development environment

To stop the development server run `Ctrl+C` command on the terminal running the server. 


#### Postman or Insomnia
API Routes. 
Endpoints available for this api are shown in the table below:

````
| Requests    |   EndPoint                     | Functionality              | Fields
| ----------- |:-------------------------------:| --------------------------:|
|  POST       |  /api//users/register/          | New teacher signup         | eg {"email": "string@user.com","firstName": "string123","lastName": "string123",  "username": "stranger","password": "string123" "is_teacher": "True"}
}
|  POST       |   /api/users/login/             | Known teacher signin       | eg {"email": "string@user.com","password":"string123"}
|  POST       |/api/classes/create/             | Create a new class         | eg {"className": "1 West"}
|  GET        | /api/classes/my_classes/        | get specific teacherclasses| 
|  PUT        |/api/classes/'Old_classname'/edit| edit classname             |eg {"className": "1 West"}
|  POST       | /api/students/add_student/      |Add new student             |eg {"firstName": "", "lastName": "Dennddoo", "age": 25,"regNumber": "11111A","className": "3 blue"}
|  GET        |/api/students/class/'class_name'/| get students of a class    |
| PUT         |/api/students/'reg_num/edit      | Edit student details       |eg {"firstName": "", "lastName": "Dennddoo", "age": "Null","regNumber": "11111A","className": "3 blue"}
| GET         |/api/students/name/search/       |Search student name or   age| 
|  POST       |/api/subjects/assign/            |assign student subject      |eg {"regNumber": "11111","maths": "True","english": "True"}
|   GET       |/api/subjects/'subject/filter/   |filter by subject           | 
|    GET      |/api/subjects/regNum/            |Get students taking subject |
|    PUT      |/api/subjects/regNum/score/      | assign scores per subject  | eg {"maths_score": 1000,"english_score": 50}

````
 
Test the API on postman or insomnia
 
 #### Built with using

* python 3.6.9
* Django
* Django Rest Framework
* Postgres DB
* Docker

*********

#### Versioning
Most recent version: [version 3](https://teacher-api-prod.herokuapp.com/api/users/register/).

***

#### Author
Darius Ndubi
 

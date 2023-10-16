# greenbone Task
## Table of contents
* [Description](#Description)
* [Usage](#usage)
* [Features](#Features)
* [Additional requirements](#Additional-requirements-for-a-Productive-version)
* [Tech stack used](#Tech-stack-used)
* [Task Description](#Task-description)
* [License](#License)

## Description
This project is intended to serve the requirements of a Backed system which are part of a task provided by Greenbone GmbH. The task description is provided as a document which can be found [here](). To see the requirements stated in the task description read the [Task description](#Task-description) section. To be able to use or review the working of the project please follow the [usage](#usage) section.

## Installation 
- Step 1: Clone the repository
```bash 
git clone https://github.com/gantaAishwarya/greenboneTask.git 
```
- Step 2: Install [Docker](https://www.docker.com/get-started/)

## Usage

``` bash
cd greenboneTask/.ci-cd
```
```bash
docker-compose up
```
Note: Python 3 is used to develop this project and necessary python libraries will be installed into the docker container automatically based on the provided Dockerfile. To have a detailed overview of python library requirements along with uwsgi and nginx configurations see [requirements.txt](https://github.com/gantaAishwarya/greenboneTask/blob/main/resources/requirements.txt), [application.ini](https://github.com/gantaAishwarya/greenboneTask/blob/main/resources/application.ini) and [nginx.conf](https://github.com/gantaAishwarya/greenboneTask/blob/main/resources/nginx.conf) files in the .ci-cd directory.
## Features

The features of this project are as per the requirements provided in the [task description](#task-description) and are not suitable to be used in production. Follow the [Additional requirements](#Additional-requirements-for-a-Productive-version) section to read about some of the improvements to be made to the project to make it production-ready. 

- Get all computers (http://localhost:80/api/)
- Get all computers assigned to an employee ()
- Get data of a single computer ()
- Remove a computer from an employee ()
- Assign a computer to another employee ()
- Add new computer ()
- Notify admin when a user gets assigned 3 or more computers using the service provided by docker image "greenbone/exercise-admin-notification". 
## Additional requirements for a Productive version


## Tech stack used
- Python 3
- Flask
- Flask-SQLAlchemy
- nginx
- uWSGI

## Task description
For the following task, an application in the selected programming language should be written and managed in a git repository.

The system administrator of our SampleCompany wants to keep track of the computers issued by the company. For this purpose, computer details should be stored in an arbitrary database.

The system administrator needs to store the following elements for each computer: MAC 
address (required), computer name (required), IP address (required), employee abbreviation 
(optional) and description (optional). The employee abbreviation consists of 3 letters. For 
example Max Mustermann should be mmu.

The system administrator wants to access the data via REST interface. The operations 
CREATE, READ, UPDATE, DELETE for a computer are to be implemented. Additionally 
the system administrator wants to be able to request the information about all computers. 

The system administrator would like to be notified if 3 or more devices are already assigned 
to a single user. Therefore an existing messaging service has to be called. This messaging 
service is running in a docker container. The image can be retrieved with docker pull 
greenbone/exercise-admin-notification. Within the image is a small service listening to 
requests on port 8080. The source code for this service can be found at 
https://github.com/greenbone/exercise-admin-notification. 

This service informs the system administrator team when the following REST endpoint is 
called: POST http://localhost:8080/api/notify The expected body of this REST 
endpoint is defined as follows: 
 
{  
    "level": "warning",  
    "employeeAbbreviation": "mmu",   
    "message": "some message"   
 } 

Requirements:
- The system administrator wants to be able to add a new computer to an employee 
- The system administrator wants to be informed when an employee is assigned 3 or 
more computers 
- The system administrator wants to be able to get all computers 
- The system administrator wants to be able to get all assigned computers for an 
employee 
- The system administrator wants to be able to get the data of a single computer 
- The system administrator wants to be able to remove a computer from an employee 
- The system administrator wants to be able to assign a computer to another employee



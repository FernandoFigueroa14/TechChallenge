# Tech Challenge

_For this challenge you must create a system that processes a file from a mounted directory. The file will contain a list of debit and credit transactions on an account. Your function should process the file and send summary information to a user in the form of an email._

## Getting started 🚀

_These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system._


### Prerequisites 📋

_Docker is the only software required for the deployment of this project. 

If you dont have Docker installed, please go to:_

* [Installing Docker](https://docs.docker.com/engine/install/)

### Installing 🔧

_The first thing you need to do is cloning this repo in your computer. To do that you can download a .zip with all the project or you can use the following command in the path you desire to have the project. (It's neccesary to have Git)_

```
git clone https://github.com/FernandoFigueroa14/TechChallenge.git
```

_Then you need to move to the 'PythonSolution' directory:_

```
cd TechChallenge
cd PythonSolution
```

_If you are in the 'PythonSolution' directory you are ready to test the code._

## Running the tests ⚙️

_Once you have cloned the project and installed Docker, you will build a Docker Container using the Dockerfile:_

```
docker build --tag container-name .
```
_Finally to run the container with the project:_

```
docker run container-name
```

### Tests 🔩

_To test the code there are 4 .csv files that contains different kind of content_

* [account1.csv]() - Example of the .pdf with the problem.
* [account2.csv]() - Testing the behaviour with a bunch of data.
* [account3.csv]() - Testing adding more columns than the expected.
* [account4.csv]() - Testing adding more columns than the expected.

_The 4 files are tested when you run the docker container

### Constraints ⚠️
_The input file must have the next columns:_

```
* Id
* Date
* Transaction
```
_The info contained in the columns is essential for the correct behaviour of the code._

## Built with 🛠️

* Python (Libraries)
```
* csv - Read the .csv files
* smtplib - Sending the email
* email.message - Email content
* PyMySQL - Connection with the Data Base
```
* Docker - Testing Environment
* HTML5 - Email content
* MySQL - DataBase
* AWS RDS - DataBase
## Versioning 📌

[Git](https://git-scm.com/) was used for the version control.

## Authors ✒️

⌨️ with ❤️ by [FernandoFigueroa14](https://github.com/FernandoFigueroa14) 😊
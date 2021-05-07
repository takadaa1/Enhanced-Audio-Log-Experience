# Enhanced Audio Log Experience

## About
This is an enhanced version of the already existent audio library with the addition of possible **real-time delivery of references** (imgs, hyperlinks, short descriptions) relating to timestamps in a specific audio file. We will be primarily focusing on the additions of such files and data into the database of the website application and how we would query them and present them to end-users. [Original Trentoniana Library](https://archive.org/search.php?query=trentoniana)
* Implement additions to an already existent database 
* Have reference files (imgs, hyperlinks, text) that appear on timestamps for users
* Support for admin accounts/audio files owners to add/modify reference files

## Collaborators
* [Akira Takada](https://github.com/takadaa1)
* [Jason Chen](https://github.com/jchen39)
* [Luke Rogers](https://github.com/Luke328)

## Repository Files
* `doc` contains all related documents for each of the stages of our project
* `code` contains the code for our project 
* `scripts` contain all the sql scripts that are needed to populate the database

## Technologies & Installation
The main technologies used for this include:
* [PostgreSQL](https://www.postgresql.org/download/)
* [Python 3](https://realpython.com/installing-python/)
* [Python Flask Library](https://flask.palletsprojects.com/en/1.1.x/installation/)
* [Python psycopg2 Library](https://www.psycopg.org/docs/install.html)

## Database Setup
Before you run the application, do the following:
* In the terminal, run `createdb projfinal`
* To access the database, enter `psql projfinal` into the terminal
* Now that we are in the database, we populate it:
  * First enter `\i DDL.sql` to create the tables for the database 
  * Then enter `\i DML.sql` to populate our tables
  * **Note: The script files must be in the same directory as the database for it to work**

## Running the Application
1. In the terminal, first navigate to the directory of the project
2. Then navigate to the `code` directory
3. Now run `./run.sh`
4. On a web browser (Google Chrome or Firefox), navigate to http://127.0.0.1:5000/. You should be greeted with a home page that looks like the following:
![image](https://user-images.githubusercontent.com/43418785/117244308-cf8b9400-ae06-11eb-8705-df69f55f7b6b.png)

## Wiki
Need any help? Check the wiki for further information [here](https://github.com/TCNJ-degoodj/stage-2b-group-8/wiki).

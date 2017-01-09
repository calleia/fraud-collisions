# fraud-collisions
Detects if two nodes belong to the same collision network, the user can also add new collisions between nodes.
## Installation
Clone the repository on your machine and you are ready to go. As the scripts are self-sufficients, there is no need for the installation of dependencies. There are no external dependencies.
## Usage
### Stand alone program
* Add new collision between two nodes
```
$ program.py --add Node1 Node2
```
* Answer if two nodes belong to the same collision network
```
$ program.py Node1 Node2
```
### Api Server
From within the project directory, run the following commands:
```
$ api-server.py
```
After that, since the server is a RESTful API, you can interact with it using your favorite web browser.



* Add new collision between two nodes
```
http://localhost/add/Node1/Node2
```
Example:

![Add collision example](https://cloud.githubusercontent.com/assets/3345423/21771935/8ccd1ec6-d670-11e6-8ae1-e129fb3ba435.PNG)
* Answer if two nodes belong to the same collision network
```
http://localhost/search/Node1/Node2
```
Example:

![Search collision example](https://cloud.githubusercontent.com/assets/3345423/21771934/8cb57c62-d670-11e6-8102-5052656b7e58.PNG)

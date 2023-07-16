# 0x00. AirBnB clone - The console.

## The Project
![image](https://drive.google.com/uc?export=view&id=1aeJ00OuWBdqhx456-euGnN7XvBo5M6Pv)
This is the first part of the ALX AirBnB clone project.

## The Command Interpreter
The aim of this project is to build a command line interpreter to manage the project as follows;
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Installing and Running the program
- Clone the repository
```shell
git clone https://{your PAT}@github.com/alyalsayed/AirBnB_clone.git
```

### Interactive Mode
- To start the console in interactive mode
```shell
$ ./console.py
(hbnb)
```

- To get an overview of how to use the console, use ? or help to get the available commands
```shell
(hbnb) ?

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```
- For example, to get help on how to **create** a new class instance
```
(hbnb) help create
Usage: create <class>
        Create a new class instance and print its id.
```
- **Quit** the console with
```shell
(hbnb) quit
```

### Non-Interactive Mode
In [non-interactive](https://unix.stackexchange.com/a/394017) mode the shell is run by reading inputs from a pipe or file.

Running the same **help** command as above
```
vagrant@ubuntu-focal:~/alx/AirBnB_clone$ echo help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
vagrant@ubuntu-focal:~/alx/AirBnB_clone$ 
```


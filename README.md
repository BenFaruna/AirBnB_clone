![HBNB Image](https://camo.githubusercontent.com/70996d3dcffa41c27a6f5d59f56a42d978a4684c/687474703a2f2f696d6775722e636f6d2f4a42434d4844502e706e67)

# AirBnB_clone

## Description
The goal of the project is to deploy on the server a simple copy of the AirBnB website
This is the first step towards building your first full web application: the AirBnB clone.

## Usage
- First, clone the repository into your directory.
    ```
    $ git clone https://github.com/BenFaruna/AirBnB_clone
    ```

- Run the executable `./console.py`

- Type help for a list of the commands available with console.py.
    help is an action provided by default by cmd.
    Enter help + command for information about respective command and usage.

### Documented commands (type help <topic>):
========================================

```
Amenity    City  Place   State  all     destroy  quit  update
BaseModel  EOF   Review  User   create  help   show

(hbnb) create City
4af7890c-007f-42ff-97d8-074214f1094f
(hbnb) show City 4af7890c-007f-42ff-97d8-074214f1094f
[City] (4af7890c-007f-42ff-97d8-074214f1094f) {'id': '4af7890c-007f-42ff-97d8-074214f1094f',
 'updated_at': datetime.datetime(2017, 6, 11, 1, 6, 39, 679386), '__class__': 'City',
 'created_at': datetime.datetime(2017, 6, 11, 1, 6, 39, 679362)}
(hbnb)$
```

- quit -- exits the program

- EOF -- exits the program

### Execution
#### interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
#### non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Files
 | File | Description |
 | ------------- | ------------- |
 | console.py | entry point of the command interpreter |
 | models/init.py | creates an instance of FileStorage |
 | models/base_model.py | class BaseModel that defines all common attributes/methods for other classes |
 | models/amenity.py | class Amenity, inherits from BaseModel |
 | models/city.py | class City, inherits from BaseModel |
 | models/place.py | class Place, inherits from BaseModel |
 | models/review.py | class Review, inherits from BaseModel |
 | models/state.py | class State, inherits from BaseModel |
 | models/user.py | class User, inherits from BaseModel |
 | models/engine/file_storage.py | class FileStorage, serializes instances to a JSON file and deserializes JSON file to instances |
 | models/engine/file_storage.py | class FileStorage, serializes instances to a JSON file and deserializes JSON file to instances |
 | tests/ | folder where are all the tests of the program |

## Tasks
### 0. README, AUTHORS
- Write a README.md
- You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository.

### 1. Be PEP8 compliant!
- Write beautiful code that passes the PEP8 checks.

### 2. Unittests
- All your files, classes, functions must be tested with unit tests

### 3. BaseModel
- Write a class BaseModel that defines all common attributes/methods for other classes

### 4. Create BaseModel from dictionary
- Create an instance with the previous dictionary representation

### 5. Store first object
- recreate a BaseModel from another one by using a dictionary representation

### 6. Console 0.0.1
- Write a program called console.py that contains the entry point of the command interpreter

### 7. Console 0.1
- Update your command interpreter (console.py) to have these commands:
  - create
  - show
  - destroy
  - all
  - update

### 8. First User
- Write a class User that inherits from BaseModel

### 9. More classes!
- Write all those classes that inherit from BaseModel:
  - State
  - City
  - Amenity
  - Place
  - Review

### 10. Console 1.0
- Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

### 11. All instances by class name
- Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all()

### 12. Count instances
- Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count()

### 13. Show
- Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>)

### 14. Destroy
- Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>)

### 15. Update
- Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>)

### 16. Update from dictionary
- pdate your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>)

### 17. Unittests for the Console!
- Write all unittests for console.py, all features!

## Authors
- **Faruna Benjamin Adejo** - [BenFaruna github](https://github.com/BenFaruna)

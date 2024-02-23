# ***IMPORTANT***
To ensure that the program works, you must have mysql workbench installed
Then in MySql workbench: Server -> Data Import and select path to folder dbForGitHub
It is necessary to have a mysql connection with a login and password and to specify the schema name in which the imported data are located.

**NotesApp in Python**

The programme presents a notepad where changes are saved to the local database.

## Necessary libraries

+ mysql.connector
+ tkinter

**Is also used os libraries to assign environment variables to hidden data such as the password to the local host in MySql**
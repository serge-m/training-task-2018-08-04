# Task 1

## How to run
* install requirements 
```
pip3 install -r requirements.txt
```
Probably some libraries like python-dev are required on system level. But I didn't check it. :(

* run 
```
python3 main.py
```

## What is implemented 

* the script loads the cached version of json file.
* it tries to insert each line in a database (sqlite, local one)
* If it fails because of incorrect values then the warning is printed

Probably because of sqlite and insertion one by on it is really slow.

Also error handling is not ok. 

Probably next time I should choose different technology for such a test task :)





# Task 1

## How to run
* install requirements 


    pip3 install -r requirements.txt
  
  
Probably some libraries like python-dev are required on system level. But I didn't check it. :(

* run insertion for the whole database (really slow, maybe just skip it)


    python main.py --connection-string "sqlite:///output_db.sqlite" 


* inserting 10 elements


    python main.py --connection-string "sqlite:///output_db.sqlite"  --limit 10


results can be viewed using sqlitebrowser - https://sqlitebrowser.org/


### Limiting the amount of data to insert:

    python main.py --limit 100


### Writing to memory.

    python main.py --connection-string "sqlite:///:memory:" 

Not really useful but at least if works rather fast.

    2018-08-04 16:16:00,735|data_loader         |INFO |Loading data from local cache './db.json'
    Output is written to database: sqlite:///:memory:. Number of data points inserted: 218635.
 

## What is implemented 

* the script loads the cached version of json file.
* it tries to insert each line in a database (sqlite, local one)
* If it fails because of incorrect values then the warning is printed

Probably because of sqlite and insertion one by on it is really slow.

Also error handling is not ok. 

Probably next time I should choose different technology for such a test task :) 





## Other notes
I analysed the data using `analysis.ipynb` notebook. There I mentioned some of my assumptions.



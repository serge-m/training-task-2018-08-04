# Task 2
Implementation of the function to check if the input string is a valid brackets sequence.

See brackets/validator.py

Developed and tested for Python 3.6.


## Structure of the directory

    task2
    |- brackets
    |  |- validator.py - solution file, contains target funciton "is_valid_string"
    |- tests
    |  |- test_validator.py - tests for is_valid_string
    |- README.md - this file
    |- requirements-test.txt 
    |- run_tests.sh - script to run tests
    
    
## How to run
There is a small console wrapper around the main is_valid_string function that prints to the console "True" or "False" depending on the validity of the first parameter. It can be called from the command line.

Example:
```
# assuming current directory is "task2"

$ python3 brackets/brackets_sequence.py "[()]"
True

$ python3 brackets/brackets_sequence.py "{[()]"
True

```


## How to run tests
Tests are in the `tests` directory. 
Install the dependencies required for testing:
```
# assuming current directory is "task2"

pip install -r requirements-test.txt
./run_tests.sh
```


## Follow up questions
### How to test
I wrote some tests for 
* simple cases
* corner cases
* for (relatively) large input

The tests cover all the branches and lines (see htmlcov/index.html after `run_tests.sh`)

It would be good to 
* test the code in other environments - especially in the environment where it will be running
* set up automated tests on CI/CD
* test for othe python versions
* wrap in a python module.

I assume it is unnecessary for the test task.


If the reliability would be critical we could:

* build a generator for correct strings up to a certain length and validate the code on that strings. Also validate the code on the rest of possible brackets strings (=incorrect strings) up to a certain length. 
That would give us more confidence about input of short strings. 

* use verification techniques, like [SPIN](http://spinroot.com/spin/whatispin.html))  

* Check if there is a reliable solution from the perspective of  formal language theory. Probably there is a parser that takes grammar as input and does the job.


### What is the complexity of the algorithm?
* O(N) where N is a length of the string
* also requires O(N) memory because of the stack

### Is it possible, and how would you parallelize it? 
TBD
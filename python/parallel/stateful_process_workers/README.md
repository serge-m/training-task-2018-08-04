Controllers define a processing graph with 4 interconnected stages:
* detector
* size_estimator (depends on detector)
* classifier (depends on detector)
* aggregator (depends on size_estimator and classifier)

We test sequential execution and parallel execution.
In case of parallel execution size_estimator and classifier work in parallel


## How to run

    pip install -r requirements.txt
    python main.py

Sample output:
    
    sequential
    FPS: 1.7753397948365568
    parallel
    worker started
    worker exited correctly
    FPS: 2.820896038347416

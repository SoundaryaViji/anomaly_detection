# Steps to run the program

src/detection.py contains the logic for finding the anomalous purchases based on the purchase history and socail network

This file takes batch,stream and output file location as arguments, if the args are not specified it takes a default input and output file location.

The Values of D and T are picked from first line of batch_log.json, if its not present it defaults them to 1 and 2
 
Test input and output files are under insight_testsuite, by executing run_tests.sh  all the tests under this folder are run.

To run the main code goto from anomaly_detection and execute ./run.sh (it can be run using ipynb too - use detection.ipynb)

To run the test, goto insight_testsuite and run ./run_tests.sh 



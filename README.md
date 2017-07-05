# Steps to execute the program

src/detection.py is the file which contains the logic for finding the anomalous purchases.

The file takes batch,stream and output file location as command parameters, if the args not specified it takes a default value.

The Values of D and T should be specified are picked from first line of batch_log.json, if not it defaults to 1 and 2 respectively
 
Test input and output files are under insight_testsuite, by executing run_tests.sh  all the tests under this folder are run.

To run the main program goto from anomaly_detection run ./run.sh (can be run using ipynb too)

To run the test, goto  insight_testsuite and run ./run_tests.sh 



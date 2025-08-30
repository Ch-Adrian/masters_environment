#!/bin/bash

#echo "Copying jar file..."
#./copy_jars.sh
#echo -e $done

#./test_algorithm.sh dynamic-connectivity-ett-1.3.0.jar 0 1497134 web-NotreDame.txt
#./test_algorithm.sh dynamic-connectivity-ett-1.3.0.jar 1 1497134 web-NotreDame.txt
#./test_algorithm.sh dynamic-connectivity-ett-1.3.0.jar 2 1497134 web-NotreDame.txt
#./test_algorithm.sh dynamic-connectivity-incremental-1.3.0.jar 0 1497134 web-NotreDame.txt
#./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 0 1497134 web-NotreDame.txt
#./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 1 1497134 web-NotreDame.txt
#./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 2 1497134 web-NotreDame.txt
#./test_algorithm.sh dynamic-mst-ett-decremental-1.3.0.jar 1 1497134 web-NotreDame.txt
#./test_algorithm.sh dynamic-sssp-decremental-1.3.0.jar 1 1497134 web-NotreDame.txt

#./test_algorithm.sh dynamic-connectivity-ett-1.3.0.jar 0 420045 Email-EuAll.txt
#./test_algorithm.sh dynamic-connectivity-ett-1.3.0.jar 1 420045 Email-EuAll.txt
#./test_algorithm.sh dynamic-connectivity-ett-1.3.0.jar 2 420045 Email-EuAll.txt
#./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 0 420045 Email-EuAll.txt
#./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 1 420045 Email-EuAll.txt
./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 2 420045 Email-EuAll.txt
#./test_algorithm.sh dynamic-connectivity-incremental-1.3.0.jar 0 420045 Email-EuAll.txt
#./test_algorithm.sh dynamic-mst-ett-decremental-1.3.0.jar 1 420045 Email-EuAll.txt
#./test_algorithm.sh dynamic-sssp-decremental-1.3.0.jar 1 420045 Email-EuAll.txt

#./test_algorithm.sh dynamic-connectivity-ett-1.3.0.jar 0 88234 facebook_combined.txt
#./test_algorithm.sh dynamic-connectivity-ett-1.3.0.jar 1 88234 facebook_combined.txt
#./test_algorithm.sh dynamic-connectivity-ett-1.3.0.jar 2 88234 facebook_combined.txt
#./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 0 88234 facebook_combined.txt
#./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 1 88234 facebook_combined.txt
#./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 2 88234 facebook_combined.txt
#./test_algorithm.sh dynamic-connectivity-incremental-1.3.0.jar 0 88234 facebook_combined.txt
#./test_algorithm.sh dynamic-mst-ett-decremental-1.3.0.jar 1 88234 facebook_combined.txt
#./test_algorithm.sh dynamic-sssp-decremental-1.3.0.jar 1 88234 facebook_combined.txt




















#./test_algorithm.sh dynamic-connectivity-incremental-1.3.0.jar 0 420045 Email-EuAll.txt
#./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 2 420045 Email-EuAll.txt
#./test_algorithm.sh dynamic-mst-ett-decremental-1.3.0.jar 0 420045 Email-EuAll.txt

#./test_algorithm.sh dynamic-sssp-decremental-1.3.0.jar 1 4245 Email-EuAll-small.txt


#./test_algorithm.sh dynamic-connectivity-ett-1.3.0.jar 2 420045 Email-EuAll.txt
#if [ $? -eq 0 ]; then
#    echo OK
#    echo 'running dynamic connectivity incremental'
#    ./test_algorithm.sh dynamic-connectivity-incremental-1.3.0.jar 0 420045 Email-EuAll.txt
#else
#    echo FAIL
#fi
#
#if [ $? -eq 0 ]; then
#    echo OK
#    ./test_algorithm.sh dynamic-connectivity-lct-1.3.0.jar 2 420045 Email-EuAll.txt
#else
#    echo FAIL
#fi
#
#if [ $? -eq 0 ]; then
#    echo OK
#    ./test_algorithm.sh dynamic-mst-ett-decremental-1.3.0.jar 1 4245 Email-EuAll.txt
#else
#    echo FAIL
#fi
#
#if [ $? -eq 0 ]; then
#    echo OK
#    ./test_algorithm.sh dynamic-sssp-decremental-1.3.0.jar 2 4245 Email-EuAll.txt
#else
#    echo FAIL
#fi
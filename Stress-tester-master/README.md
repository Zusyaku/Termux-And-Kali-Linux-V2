![alt text](https://raw.githubusercontent.com/Leeon123/Stress-tester/master/logo.png)
# Stress-tester
Golang Server Stress Test Tool 

It is a tool for me to test my server's waf. Now just share with you. 

It sucks but it help me a lot when i doing testing.

Improved the all stress test method.

## Statement
This tool only used for testing server and education,

not for any criminal activity.
## Example:
![Example](https://raw.githubusercontent.com/Leeon123/Stress-tester/master/test.png)
## Download:

    git clone https://github.com/Leeon123/Stress-tester.git
    cd Stress-test

## Usage:
Please use command "ulimit -n 999999" before using it in linux. :)

    go build stress.go
    ./stress host/ip port mode threads seconds timeout
    
Mode:

    [1] Tcp connection flood
    [2] Udp flood
    [3] Http/s flood

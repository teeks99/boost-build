Tom's Boost Regression Tests
============================

These regression runs are automated sets of the 
[Boost Regression Test Suite](http://www.boost.org/development/running_regression_tests.html) that have a set of 
python scripts that continuously run them in a loop. 

The results are available here:

*   [mainline branch](https://www.boost.org/development/tests/master/developer/summary.html)
*   [develop branch](https://www.boost.org/development/tests/develop/developer/summary.html)

Each set of runs is controlled by its respective `machine_vars.json` file. 

Linux Regression Configurations
-------------------------------

On Linux we run versions of GCC (4.4 - 14) and Clang (3.0 - 17). 

Linux runs are executed within docker. The various docker images that are use can be found in the corresponding 
[Docker](http://github.com/teeks99/boost-cpp-docker) repo. They all run on the Ubuntu image for the LTS OS version that 
was in common use at the time of the compiler release. Each of these images has multiple compiler configurations 
defined in its `user-config.jam` file. There are too many configurations of compiler + switches to run tests against 
all the combinations.

In general, the teeks99-02 tester will run the most common switches option for each of the compilers against both the 
development and master branches. Then for the most recent version of each compiler only it will perform a run against 
each of the enumerated switch options against both develop and master. In total, this is nearly 100 configurations, 
each taking between 0.9 and 1.6 hours to execute. This results in a revist time for any single configuration of 
approximately five days. So that developers can have some results quicker, every approximately ten runs, the order will 
be paused and four runs will be executed consisiting of the latest version of each compiler, with the most common 
switches, against each of develop and master.

As opposed to the teeks99-02 runner, the teeks99-03 runner is optimized to provide rapid results to developers when 
they commit changes. This runner only has four configurations, the latest version of each of GCC and Clang with their 
most common switches, running against master and develop. This should ensure that a developer can see the results of 
their commit against a current GCC or Clang within three hours (plus a bit extra for the report to generate). 

| Name | Branch | Compiler | Version | Flags | Docker Image |
| ---- | ------ | -------- | ------- | ----- | ------------ |
| dg4.6-98 | develop | gcc | 4.6 | -std=c++98 | teeks99/boost-cpp-docker:gcc-4.6 |
| mg4.6-98 | master | gcc | 4.6 | -std=c++98 | teeks99/boost-cpp-docker:gcc-4.6 |
| dg4.6-0x | develop | gcc | 4.6 | -std=c++0x | teeks99/boost-cpp-docker:gcc-4.6 |
| mg4.6-0x | master | gcc | 4.6 | -std=c++0x | teeks99/boost-cpp-docker:gcc-4.6 |
| dg4.6-g98 | develop | gcc | 4.6 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-4.6 |
| mg4.6-g98 | master | gcc | 4.6 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-4.6 |
| dg4.6-g0x | develop | gcc | 4.6 | -std=gnu++0x | teeks99/boost-cpp-docker:gcc-4.6 |
| mg4.6-g0x | master | gcc | 4.6 | -std=gnu++0x | teeks99/boost-cpp-docker:gcc-4.6 |
| dg4.6-opt | develop | gcc | 4.6 | -std=c++0x -O2 | teeks99/boost-cpp-docker:gcc-4.6 |
| mg4.6-opt | master | gcc | 4.6 | -std=c++0x -O2 | teeks99/boost-cpp-docker:gcc-4.6 |
| dg4.6-warn | develop | gcc | 4.6 | -std=c++0x -Wall -Wextra | teeks99/boost-cpp-docker:gcc-4.6 |
| mg4.6-warn | master | gcc | 4.6 | -std=c++0x -Wall -Wextra | teeks99/boost-cpp-docker:gcc-4.6 |
| dg4.7 | develop | gcc | 4.7 | -std=c++11 | teeks99/boost-cpp-docker:gcc-4.7 |
| mg4.7 | master | gcc | 4.7 | -std=c++11 | teeks99/boost-cpp-docker:gcc-4.7 |
| dg4.8 | develop | gcc | 4.8 | -std=c++11 | teeks99/boost-cpp-docker:gcc-4.8 |
| mg4.8 | master | gcc | 4.8 | -std=c++11 | teeks99/boost-cpp-docker:gcc-4.8 |
| dg4.9 | develop | gcc | 4.9 | -std=c++11 | teeks99/boost-cpp-docker:gcc-4.9 |
| mg4.9 | master | gcc | 4.9 | -std=c++11 | teeks99/boost-cpp-docker:gcc-4.9 |
| dg5 | develop | gcc | 5 | -std=c++14 | teeks99/boost-cpp-docker:gcc-5 |
| mg5 | master | gcc | 5 | -std=c++14 | teeks99/boost-cpp-docker:gcc-5 |
| dg6 | develop | gcc | 6 | -std=c++14 | teeks99/boost-cpp-docker:gcc-6 |
| mg6 | master | gcc | 6 | -std=c++14 | teeks99/boost-cpp-docker:gcc-6 |
| dg7 | develop | gcc | 7 | -std=c++14 | teeks99/boost-cpp-docker:gcc-7 |
| mg7 | master | gcc | 7 | -std=c++14 | teeks99/boost-cpp-docker:gcc-7 |
| dg8 | develop | gcc | 8 | -std=c++17 | teeks99/boost-cpp-docker:gcc-8 |
| mg8 | master | gcc | 8 | -std=c++17 | teeks99/boost-cpp-docker:gcc-8 |
| dg8-14 | develop | gcc | 8 | -std=c++14 | teeks99/boost-cpp-docker:gcc-8 |
| mg8-14 | master | gcc | 8 | -std=c++14 | teeks99/boost-cpp-docker:gcc-8 |
| dg8-g14 | develop | gcc | 8 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-8 |
| mg8-g14 | master | gcc | 8 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-8 |
| dg8-17 | develop | gcc | 8 | -std=c++17 | teeks99/boost-cpp-docker:gcc-8 |
| mg8-17 | master | gcc | 8 | -std=c++17 | teeks99/boost-cpp-docker:gcc-8 |
| dg8-g17 | develop | gcc | 8 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-8 |
| mg8-g17 | master | gcc | 8 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-8 |
| dg8-2a | develop | gcc | 8 | -std=c++2a | teeks99/boost-cpp-docker:gcc-8 |
| mg8-2a | master | gcc | 8 | -std=c++2a | teeks99/boost-cpp-docker:gcc-8 |
| dg8-g2a | develop | gcc | 8 | -std=gnu++2a | teeks99/boost-cpp-docker:gcc-8 |
| mg8-g2a | master | gcc | 8 | -std=gnu++2a | teeks99/boost-cpp-docker:gcc-8 |
| dg8-11 | develop | gcc | 8 | -std=c++11 | teeks99/boost-cpp-docker:gcc-8 |
| mg8-11 | master | gcc | 8 | -std=c++11 | teeks99/boost-cpp-docker:gcc-8 |
| dg8-g11 | develop | gcc | 8 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-8 |
| mg8-g11 | master | gcc | 8 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-8 |
| dg8-98 | develop | gcc | 8 | -std=c++98 | teeks99/boost-cpp-docker:gcc-8 |
| mg8-98 | master | gcc | 8 | -std=c++98 | teeks99/boost-cpp-docker:gcc-8 |
| dg8-g98 | develop | gcc | 8 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-8 |
| mg8-g98 | master | gcc | 8 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-8 |
| dg8-opt | develop | gcc | 8 | -std=c++2a -O2 | teeks99/boost-cpp-docker:gcc-8 |
| mg8-opt | master | gcc | 8 | -std=c++2a -O2 | teeks99/boost-cpp-docker:gcc-8 |
| dg8-warn | develop | gcc | 8 | -std=c++2a -Wall -Wextra | teeks99/boost-cpp-docker:gcc-8 |
| mg8-warn | master | gcc | 8 | -std=c++2a -Wall -Wextra | teeks99/boost-cpp-docker:gcc-8 |
| dg9 | develop | gcc | 9 | -std=c++17 | teeks99/boost-cpp-docker:gcc-9 |
| mg9 | master | gcc | 9 | -std=c++17 | teeks99/boost-cpp-docker:gcc-9 |
| dg9-14 | develop | gcc | 9 | -std=c++14 | teeks99/boost-cpp-docker:gcc-9 |
| mg9-14 | master | gcc | 9 | -std=c++14 | teeks99/boost-cpp-docker:gcc-9 |
| dg9-g14 | develop | gcc | 9 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-9 |
| mg9-g14 | master | gcc | 9 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-9 |
| dg9-17 | develop | gcc | 9 | -std=c++17 | teeks99/boost-cpp-docker:gcc-9 |
| mg9-17 | master | gcc | 9 | -std=c++17 | teeks99/boost-cpp-docker:gcc-9 |
| dg9-g17 | develop | gcc | 9 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-9 |
| mg9-g17 | master | gcc | 9 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-9 |
| dg9-2a | develop | gcc | 9 | -std=c++2a | teeks99/boost-cpp-docker:gcc-9 |
| mg9-2a | master | gcc | 9 | -std=c++2a | teeks99/boost-cpp-docker:gcc-9 |
| dg9-g2a | develop | gcc | 9 | -std=gnu++2a | teeks99/boost-cpp-docker:gcc-9 |
| mg9-g2a | master | gcc | 9 | -std=gnu++2a | teeks99/boost-cpp-docker:gcc-9 |
| dg9-11 | develop | gcc | 9 | -std=c++11 | teeks99/boost-cpp-docker:gcc-9 |
| mg9-11 | master | gcc | 9 | -std=c++11 | teeks99/boost-cpp-docker:gcc-9 |
| dg9-g11 | develop | gcc | 9 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-9 |
| mg9-g11 | master | gcc | 9 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-9 |
| dg9-98 | develop | gcc | 9 | -std=c++98 | teeks99/boost-cpp-docker:gcc-9 |
| mg9-98 | master | gcc | 9 | -std=c++98 | teeks99/boost-cpp-docker:gcc-9 |
| dg9-g98 | develop | gcc | 9 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-9 |
| mg9-g98 | master | gcc | 9 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-9 |
| dg9-opt | develop | gcc | 9 | -std=c++2a -O2 | teeks99/boost-cpp-docker:gcc-9 |
| mg9-opt | master | gcc | 9 | -std=c++2a -O2 | teeks99/boost-cpp-docker:gcc-9 |
| dg9-warn | develop | gcc | 9 | -std=c++2a -Wall -Wextra | teeks99/boost-cpp-docker:gcc-9 |
| mg9-warn | master | gcc | 9 | -std=c++2a -Wall -Wextra | teeks99/boost-cpp-docker:gcc-9 |
| dg10 | develop | gcc | 10 | -std=c++17 | teeks99/boost-cpp-docker:gcc-10 |
| mg10 | master | gcc | 10 | -std=c++17 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-14 | develop | gcc | 10 | -std=c++14 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-14 | master | gcc | 10 | -std=c++14 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-g14 | develop | gcc | 10 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-g14 | master | gcc | 10 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-17 | develop | gcc | 10 | -std=c++17 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-17 | master | gcc | 10 | -std=c++17 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-g17 | develop | gcc | 10 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-g17 | master | gcc | 10 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-20 | develop | gcc | 10 | -std=c++20 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-20 | master | gcc | 10 | -std=c++20 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-g20 | develop | gcc | 10 | -std=gnu++20 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-g20 | master | gcc | 10 | -std=gnu++20 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-11 | develop | gcc | 10 | -std=c++11 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-11 | master | gcc | 10 | -std=c++11 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-g11 | develop | gcc | 10 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-g11 | master | gcc | 10 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-98 | develop | gcc | 10 | -std=c++98 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-98 | master | gcc | 10 | -std=c++98 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-g98 | develop | gcc | 10 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-g98 | master | gcc | 10 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-opt | develop | gcc | 10 | -std=c++20 -O2 | teeks99/boost-cpp-docker:gcc-10 |
| mg10-opt | master | gcc | 10 | -std=c++20 -O2 | teeks99/boost-cpp-docker:gcc-10 |
| dg10-warn | develop | gcc | 10 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:gcc-10 |
| mg10-warn | master | gcc | 10 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:gcc-10 |
| dg11 | develop | gcc | 11 | -std=c++17 | teeks99/boost-cpp-docker:gcc-11 |
| mg11 | master | gcc | 11 | -std=c++17 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-14 | develop | gcc | 11 | -std=c++14 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-14 | master | gcc | 11 | -std=c++14 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-g14 | develop | gcc | 11 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-g14 | master | gcc | 11 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-17 | develop | gcc | 11 | -std=c++17 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-17 | master | gcc | 11 | -std=c++17 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-g17 | develop | gcc | 11 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-g17 | master | gcc | 11 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-20 | develop | gcc | 11 | -std=c++20 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-20 | master | gcc | 11 | -std=c++20 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-g20 | develop | gcc | 11 | -std=gnu++20 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-g20 | master | gcc | 11 | -std=gnu++20 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-11 | develop | gcc | 11 | -std=c++11 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-11 | master | gcc | 11 | -std=c++11 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-g11 | develop | gcc | 11 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-g11 | master | gcc | 11 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-98 | develop | gcc | 11 | -std=c++98 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-98 | master | gcc | 11 | -std=c++98 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-g98 | develop | gcc | 11 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-g98 | master | gcc | 11 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-opt | develop | gcc | 11 | -std=c++20 -O2 | teeks99/boost-cpp-docker:gcc-11 |
| mg11-opt | master | gcc | 11 | -std=c++20 -O2 | teeks99/boost-cpp-docker:gcc-11 |
| dg11-warn | develop | gcc | 11 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:gcc-11 |
| mg11-warn | master | gcc | 11 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:gcc-11 |
| dg12 | develop | gcc | 12 | -std=c++17 | teeks99/boost-cpp-docker:gcc-12 |
| mg12 | master | gcc | 12 | -std=c++17 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-14 | develop | gcc | 12 | -std=c++14 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-14 | master | gcc | 12 | -std=c++14 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-g14 | develop | gcc | 12 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-g14 | master | gcc | 12 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-17 | develop | gcc | 12 | -std=c++17 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-17 | master | gcc | 12 | -std=c++17 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-g17 | develop | gcc | 12 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-g17 | master | gcc | 12 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-20 | develop | gcc | 12 | -std=c++20 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-20 | master | gcc | 12 | -std=c++20 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-g20 | develop | gcc | 12 | -std=gnu++20 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-g20 | master | gcc | 12 | -std=gnu++20 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-11 | develop | gcc | 12 | -std=c++11 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-11 | master | gcc | 12 | -std=c++11 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-g11 | develop | gcc | 12 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-g11 | master | gcc | 12 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-98 | develop | gcc | 12 | -std=c++98 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-98 | master | gcc | 12 | -std=c++98 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-g98 | develop | gcc | 12 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-g98 | master | gcc | 12 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-opt | develop | gcc | 12 | -std=c++20 -O2 | teeks99/boost-cpp-docker:gcc-12 |
| mg12-opt | master | gcc | 12 | -std=c++20 -O2 | teeks99/boost-cpp-docker:gcc-12 |
| dg12-warn | develop | gcc | 12 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:gcc-12 |
| mg12-warn | master | gcc | 12 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:gcc-12 |
| dg13 | develop | gcc | 13 | -std=c++20 | teeks99/boost-cpp-docker:gcc-13 |
| mg13 | master | gcc | 13 | -std=c++20 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-14 | develop | gcc | 13 | -std=c++14 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-14 | master | gcc | 13 | -std=c++14 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-g14 | develop | gcc | 13 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-g14 | master | gcc | 13 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-17 | develop | gcc | 13 | -std=c++17 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-17 | master | gcc | 13 | -std=c++17 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-g17 | develop | gcc | 13 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-g17 | master | gcc | 13 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-20 | develop | gcc | 13 | -std=c++20 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-20 | master | gcc | 13 | -std=c++20 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-g20 | develop | gcc | 13 | -std=gnu++20 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-g20 | master | gcc | 13 | -std=gnu++20 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-2b | develop | gcc | 13 | -std=c++2b | teeks99/boost-cpp-docker:gcc-13 |
| mg13-2b | master | gcc | 13 | -std=c++2b | teeks99/boost-cpp-docker:gcc-13 |
| dg13-g2b | develop | gcc | 13 | -std=gnu++2b | teeks99/boost-cpp-docker:gcc-13 |
| mg13-g2b | master | gcc | 13 | -std=gnu++2b | teeks99/boost-cpp-docker:gcc-13 |
| dg13-11 | develop | gcc | 13 | -std=c++11 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-11 | master | gcc | 13 | -std=c++11 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-g11 | develop | gcc | 13 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-g11 | master | gcc | 13 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-98 | develop | gcc | 13 | -std=c++98 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-98 | master | gcc | 13 | -std=c++98 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-g98 | develop | gcc | 13 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-g98 | master | gcc | 13 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-opt | develop | gcc | 13 | -std=c++20 -O2 | teeks99/boost-cpp-docker:gcc-13 |
| mg13-opt | master | gcc | 13 | -std=c++20 -O2 | teeks99/boost-cpp-docker:gcc-13 |
| dg13-warn | develop | gcc | 13 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:gcc-13 |
| mg13-warn | master | gcc | 13 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:gcc-13 |
| dg14 | develop | gcc | 14 | -std=c++20 | teeks99/boost-cpp-docker:gcc-14 |
| mg14 | master | gcc | 14 | -std=c++20 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-14 | develop | gcc | 14 | -std=c++14 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-14 | master | gcc | 14 | -std=c++14 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-g14 | develop | gcc | 14 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-g14 | master | gcc | 14 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-17 | develop | gcc | 14 | -std=c++17 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-17 | master | gcc | 14 | -std=c++17 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-g17 | develop | gcc | 14 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-g17 | master | gcc | 14 | -std=gnu++17 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-20 | develop | gcc | 14 | -std=c++20 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-20 | master | gcc | 14 | -std=c++20 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-g20 | develop | gcc | 14 | -std=gnu++20 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-g20 | master | gcc | 14 | -std=gnu++20 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-2b | develop | gcc | 14 | -std=c++2b | teeks99/boost-cpp-docker:gcc-14 |
| mg14-2b | master | gcc | 14 | -std=c++2b | teeks99/boost-cpp-docker:gcc-14 |
| dg14-g2b | develop | gcc | 14 | -std=gnu++2b | teeks99/boost-cpp-docker:gcc-14 |
| mg14-g2b | master | gcc | 14 | -std=gnu++2b | teeks99/boost-cpp-docker:gcc-14 |
| dg14-11 | develop | gcc | 14 | -std=c++11 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-11 | master | gcc | 14 | -std=c++11 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-g11 | develop | gcc | 14 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-g11 | master | gcc | 14 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-98 | develop | gcc | 14 | -std=c++98 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-98 | master | gcc | 14 | -std=c++98 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-g98 | develop | gcc | 14 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-g98 | master | gcc | 14 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-opt | develop | gcc | 14 | -std=c++20 -O2 | teeks99/boost-cpp-docker:gcc-14 |
| mg14-opt | master | gcc | 14 | -std=c++20 -O2 | teeks99/boost-cpp-docker:gcc-14 |
| dg14-warn | develop | gcc | 14 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:gcc-14 |
| mg14-warn | master | gcc | 14 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:gcc-14 |
| dc3.4-98 | develop | clang | 3.4 | -std=c++98 | teeks99/boost-cpp-docker:clang-3.4 |
| mc3.4-98 | master | clang | 3.4 | -std=c++98 | teeks99/boost-cpp-docker:clang-3.4 |
| dc3.4-g98 | develop | clang | 3.4 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-3.4 |
| mc3.4-g98 | master | clang | 3.4 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-3.4 |
| dc3.4-11 | develop | clang | 3.4 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.4 |
| mc3.4-11 | master | clang | 3.4 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.4 |
| dc3.4-g11 | develop | clang | 3.4 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-3.4 |
| mc3.4-g11 | master | clang | 3.4 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-3.4 |
| dc3.4-opt | develop | clang | 3.4 | -std=c++11 -O2 | teeks99/boost-cpp-docker:clang-3.4 |
| mc3.4-opt | master | clang | 3.4 | -std=c++11 -O2 | teeks99/boost-cpp-docker:clang-3.4 |
| dc3.4-warn | develop | clang | 3.4 | -std=c++11 -Wall -Wextra | teeks99/boost-cpp-docker:clang-3.4 |
| mc3.4-warn | master | clang | 3.4 | -std=c++11 -Wall -Wextra | teeks99/boost-cpp-docker:clang-3.4 |
| dc3.5-14 | develop | clang | 3.5 | -std=c++14 | teeks99/boost-cpp-docker:clang-3.5 |
| mc3.5-14 | master | clang | 3.5 | -std=c++14 | teeks99/boost-cpp-docker:clang-3.5 |
| dc3.6-14 | develop | clang | 3.6 | -std=c++14 | teeks99/boost-cpp-docker:clang-3.6 |
| mc3.6-14 | master | clang | 3.6 | -std=c++14 | teeks99/boost-cpp-docker:clang-3.6 |
| dc3.7-14 | develop | clang | 3.7 | -std=c++14 | teeks99/boost-cpp-docker:clang-3.7 |
| mc3.7-14 | master | clang | 3.7 | -std=c++14 | teeks99/boost-cpp-docker:clang-3.7 |
| dc3.8-14 | develop | clang | 3.8 | -std=c++14 | teeks99/boost-cpp-docker:clang-3.8 |
| mc3.8-14 | master | clang | 3.8 | -std=c++14 | teeks99/boost-cpp-docker:clang-3.8 |
| dc3.9-14 | develop | clang | 3.9 | -std=c++14 | teeks99/boost-cpp-docker:clang-3.9 |
| mc3.9-14 | master | clang | 3.9 | -std=c++14 | teeks99/boost-cpp-docker:clang-3.9 |
| dc4-14 | develop | clang | 4.0 | -std=c++14 | teeks99/boost-cpp-docker:clang-4 |
| mc4-14 | master | clang | 4.0 | -std=c++14 | teeks99/boost-cpp-docker:clang-4 |
| dc5-14 | develop | clang | 5.0 | -std=c++14 | teeks99/boost-cpp-docker:clang-5 |
| mc5-14 | master | clang | 5.0 | -std=c++14 | teeks99/boost-cpp-docker:clang-5 |
| dc6-17 | develop | clang | 6.0 | -std=c++17 | teeks99/boost-cpp-docker:clang-6 |
| mc6-17 | master | clang | 6.0 | -std=c++17 | teeks99/boost-cpp-docker:clang-6 |
| dc7-17 | develop | clang | 7 | -std=c++17 | teeks99/boost-cpp-docker:clang-7 |
| mc7-17 | master | clang | 7 | -std=c++17 | teeks99/boost-cpp-docker:clang-7 |
| dc8 | develop | clang | 8 | -std=c++17 | teeks99/boost-cpp-docker:clang-8 |
| mc8 | master | clang | 8 | -std=c++17 | teeks99/boost-cpp-docker:clang-8 |
| dc8-2a | develop | clang | 8 | -std=c++2a | teeks99/boost-cpp-docker:clang-8 |
| mc8-2a | master | clang | 8 | -std=c++2a | teeks99/boost-cpp-docker:clang-8 |
| dc8-14 | develop | clang | 8 | -std=c++14 | teeks99/boost-cpp-docker:clang-8 |
| mc8-14 | master | clang | 8 | -std=c++14 | teeks99/boost-cpp-docker:clang-8 |
| dc8-g14 | develop | clang | 8 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-8 |
| mc8-g14 | master | clang | 8 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-8 |
| dc8-17 | develop | clang | 8 | -std=c++17 | teeks99/boost-cpp-docker:clang-8 |
| mc8-17 | master | clang | 8 | -std=c++17 | teeks99/boost-cpp-docker:clang-8 |
| dc8-g17 | develop | clang | 8 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-8 |
| mc8-g17 | master | clang | 8 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-8 |
| dc8-11 | develop | clang | 8 | -std=c++11 | teeks99/boost-cpp-docker:clang-8 |
| mc8-11 | master | clang | 8 | -std=c++11 | teeks99/boost-cpp-docker:clang-8 |
| dc8-g11 | develop | clang | 8 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-8 |
| mc8-g11 | master | clang | 8 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-8 |
| dc8-98 | develop | clang | 8 | -std=c++98 | teeks99/boost-cpp-docker:clang-8 |
| mc8-98 | master | clang | 8 | -std=c++98 | teeks99/boost-cpp-docker:clang-8 |
| dc8-g98 | develop | clang | 8 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-8 |
| mc8-g98 | master | clang | 8 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-8 |
| dc8-opt | develop | clang | 8 | -std=c++2a -O2 | teeks99/boost-cpp-docker:clang-8 |
| mc8-opt | master | clang | 8 | -std=c++2a -O2 | teeks99/boost-cpp-docker:clang-8 |
| dc8-warn | develop | clang | 8 | -std=c++2a -Wall -Wextra | teeks99/boost-cpp-docker:clang-8 |
| mc8-warn | master | clang | 8 | -std=c++2a -Wall -Wextra | teeks99/boost-cpp-docker:clang-8 |
| dc8-2a-lc | develop | clang | 8 | -std=c++2a -stdlib=libc++ | teeks99/boost-cpp-docker:clang-8 |
| mc8-2a-lc | master | clang | 8 | -std=c++2a -stdlib=libc++ | teeks99/boost-cpp-docker:clang-8 |
| dc9 | develop | clang | 9 | -std=c++17 | teeks99/boost-cpp-docker:clang-9 |
| mc9 | master | clang | 9 | -std=c++17 | teeks99/boost-cpp-docker:clang-9 |
| dc9-2a | develop | clang | 9 | -std=c++2a | teeks99/boost-cpp-docker:clang-9 |
| mc9-2a | master | clang | 9 | -std=c++2a | teeks99/boost-cpp-docker:clang-9 |
| dc9-14 | develop | clang | 9 | -std=c++14 | teeks99/boost-cpp-docker:clang-9 |
| mc9-14 | master | clang | 9 | -std=c++14 | teeks99/boost-cpp-docker:clang-9 |
| dc9-g14 | develop | clang | 9 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-9 |
| mc9-g14 | master | clang | 9 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-9 |
| dc9-17 | develop | clang | 9 | -std=c++17 | teeks99/boost-cpp-docker:clang-9 |
| mc9-17 | master | clang | 9 | -std=c++17 | teeks99/boost-cpp-docker:clang-9 |
| dc9-g17 | develop | clang | 9 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-9 |
| mc9-g17 | master | clang | 9 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-9 |
| dc9-11 | develop | clang | 9 | -std=c++11 | teeks99/boost-cpp-docker:clang-9 |
| mc9-11 | master | clang | 9 | -std=c++11 | teeks99/boost-cpp-docker:clang-9 |
| dc9-g11 | develop | clang | 9 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-9 |
| mc9-g11 | master | clang | 9 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-9 |
| dc9-98 | develop | clang | 9 | -std=c++98 | teeks99/boost-cpp-docker:clang-9 |
| mc9-98 | master | clang | 9 | -std=c++98 | teeks99/boost-cpp-docker:clang-9 |
| dc9-g98 | develop | clang | 9 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-9 |
| mc9-g98 | master | clang | 9 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-9 |
| dc9-opt | develop | clang | 9 | -std=c++2a -O2 | teeks99/boost-cpp-docker:clang-9 |
| mc9-opt | master | clang | 9 | -std=c++2a -O2 | teeks99/boost-cpp-docker:clang-9 |
| dc9-warn | develop | clang | 9 | -std=c++2a -Wall -Wextra | teeks99/boost-cpp-docker:clang-9 |
| mc9-warn | master | clang | 9 | -std=c++2a -Wall -Wextra | teeks99/boost-cpp-docker:clang-9 |
| dc9-2a-lc | develop | clang | 9 | -std=c++2a -stdlib=libc++ | teeks99/boost-cpp-docker:clang-9 |
| mc9-2a-lc | master | clang | 9 | -std=c++2a -stdlib=libc++ | teeks99/boost-cpp-docker:clang-9 |
| dc10 | develop | clang | 10 | -std=c++17 | teeks99/boost-cpp-docker:clang-10 |
| mc10 | master | clang | 10 | -std=c++17 | teeks99/boost-cpp-docker:clang-10 |
| dc10-2a | develop | clang | 10 | -std=c++2a | teeks99/boost-cpp-docker:clang-10 |
| mc10-2a | master | clang | 10 | -std=c++2a | teeks99/boost-cpp-docker:clang-10 |
| dc10-14 | develop | clang | 10 | -std=c++14 | teeks99/boost-cpp-docker:clang-10 |
| mc10-14 | master | clang | 10 | -std=c++14 | teeks99/boost-cpp-docker:clang-10 |
| dc10-g14 | develop | clang | 10 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-10 |
| mc10-g14 | master | clang | 10 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-10 |
| dc10-17 | develop | clang | 10 | -std=c++17 | teeks99/boost-cpp-docker:clang-10 |
| mc10-17 | master | clang | 10 | -std=c++17 | teeks99/boost-cpp-docker:clang-10 |
| dc10-g17 | develop | clang | 10 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-10 |
| mc10-g17 | master | clang | 10 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-10 |
| dc10-11 | develop | clang | 10 | -std=c++11 | teeks99/boost-cpp-docker:clang-10 |
| mc10-11 | master | clang | 10 | -std=c++11 | teeks99/boost-cpp-docker:clang-10 |
| dc10-g11 | develop | clang | 10 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-10 |
| mc10-g11 | master | clang | 10 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-10 |
| dc10-98 | develop | clang | 10 | -std=c++98 | teeks99/boost-cpp-docker:clang-10 |
| mc10-98 | master | clang | 10 | -std=c++98 | teeks99/boost-cpp-docker:clang-10 |
| dc10-g98 | develop | clang | 10 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-10 |
| mc10-g98 | master | clang | 10 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-10 |
| dc10-opt | develop | clang | 10 | -std=c++2a -O2 | teeks99/boost-cpp-docker:clang-10 |
| mc10-opt | master | clang | 10 | -std=c++2a -O2 | teeks99/boost-cpp-docker:clang-10 |
| dc10-warn | develop | clang | 10 | -std=c++2a -Wall -Wextra | teeks99/boost-cpp-docker:clang-10 |
| mc10-warn | master | clang | 10 | -std=c++2a -Wall -Wextra | teeks99/boost-cpp-docker:clang-10 |
| dc10-2a-lc | develop | clang | 10 | -std=c++2a -stdlib=libc++ | teeks99/boost-cpp-docker:clang-10 |
| mc10-2a-lc | master | clang | 10 | -std=c++2a -stdlib=libc++ | teeks99/boost-cpp-docker:clang-10 |
| dc11 | develop | clang | 11 | -std=c++20 | teeks99/boost-cpp-docker:clang-11 |
| mc11 | master | clang | 11 | -std=c++20 | teeks99/boost-cpp-docker:clang-11 |
| dc11-20 | develop | clang | 11 | -std=c++20 | teeks99/boost-cpp-docker:clang-11 |
| mc11-20 | master | clang | 11 | -std=c++20 | teeks99/boost-cpp-docker:clang-11 |
| dc11-g20 | develop | clang | 11 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-11 |
| mc11-g20 | master | clang | 11 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-11 |
| dc11-17 | develop | clang | 11 | -std=c++17 | teeks99/boost-cpp-docker:clang-11 |
| mc11-17 | master | clang | 11 | -std=c++17 | teeks99/boost-cpp-docker:clang-11 |
| dc11-g17 | develop | clang | 11 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-11 |
| mc11-g17 | master | clang | 11 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-11 |
| dc11-14 | develop | clang | 11 | -std=c++14 | teeks99/boost-cpp-docker:clang-11 |
| mc11-14 | master | clang | 11 | -std=c++14 | teeks99/boost-cpp-docker:clang-11 |
| dc11-g14 | develop | clang | 11 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-11 |
| mc11-g14 | master | clang | 11 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-11 |
| dc11-11 | develop | clang | 11 | -std=c++11 | teeks99/boost-cpp-docker:clang-11 |
| mc11-11 | master | clang | 11 | -std=c++11 | teeks99/boost-cpp-docker:clang-11 |
| dc11-g11 | develop | clang | 11 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-11 |
| mc11-g11 | master | clang | 11 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-11 |
| dc11-98 | develop | clang | 11 | -std=c++98 | teeks99/boost-cpp-docker:clang-11 |
| mc11-98 | master | clang | 11 | -std=c++98 | teeks99/boost-cpp-docker:clang-11 |
| dc11-g98 | develop | clang | 11 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-11 |
| mc11-g98 | master | clang | 11 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-11 |
| dc11-opt | develop | clang | 11 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-11 |
| mc11-opt | master | clang | 11 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-11 |
| dc11-warn | develop | clang | 11 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-11 |
| mc11-warn | master | clang | 11 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-11 |
| dc11-20-lc | develop | clang | 11 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-11 |
| mc11-20-lc | master | clang | 11 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-11 |
| dc12 | develop | clang | 12 | -std=c++20 | teeks99/boost-cpp-docker:clang-12 |
| mc12 | master | clang | 12 | -std=c++20 | teeks99/boost-cpp-docker:clang-12 |
| dc12-20 | develop | clang | 12 | -std=c++20 | teeks99/boost-cpp-docker:clang-12 |
| mc12-20 | master | clang | 12 | -std=c++20 | teeks99/boost-cpp-docker:clang-12 |
| dc12-g20 | develop | clang | 12 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-12 |
| mc12-g20 | master | clang | 12 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-12 |
| dc12-17 | develop | clang | 12 | -std=c++17 | teeks99/boost-cpp-docker:clang-12 |
| mc12-17 | master | clang | 12 | -std=c++17 | teeks99/boost-cpp-docker:clang-12 |
| dc12-g17 | develop | clang | 12 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-12 |
| mc12-g17 | master | clang | 12 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-12 |
| dc12-14 | develop | clang | 12 | -std=c++14 | teeks99/boost-cpp-docker:clang-12 |
| mc12-14 | master | clang | 12 | -std=c++14 | teeks99/boost-cpp-docker:clang-12 |
| dc12-g14 | develop | clang | 12 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-12 |
| mc12-g14 | master | clang | 12 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-12 |
| dc12-11 | develop | clang | 12 | -std=c++11 | teeks99/boost-cpp-docker:clang-12 |
| mc12-11 | master | clang | 12 | -std=c++11 | teeks99/boost-cpp-docker:clang-12 |
| dc12-g11 | develop | clang | 12 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-12 |
| mc12-g11 | master | clang | 12 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-12 |
| dc12-98 | develop | clang | 12 | -std=c++98 | teeks99/boost-cpp-docker:clang-12 |
| mc12-98 | master | clang | 12 | -std=c++98 | teeks99/boost-cpp-docker:clang-12 |
| dc12-g98 | develop | clang | 12 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-12 |
| mc12-g98 | master | clang | 12 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-12 |
| dc12-opt | develop | clang | 12 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-12 |
| mc12-opt | master | clang | 12 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-12 |
| dc12-warn | develop | clang | 12 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-12 |
| mc12-warn | master | clang | 12 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-12 |
| dc12-20-lc | develop | clang | 12 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-12 |
| mc12-20-lc | master | clang | 12 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-12 |
| dc13 | develop | clang | 13 | -std=c++20 | teeks99/boost-cpp-docker:clang-13 |
| mc13 | master | clang | 13 | -std=c++20 | teeks99/boost-cpp-docker:clang-13 |
| dc13-20 | develop | clang | 13 | -std=c++20 | teeks99/boost-cpp-docker:clang-13 |
| mc13-20 | master | clang | 13 | -std=c++20 | teeks99/boost-cpp-docker:clang-13 |
| dc13-g20 | develop | clang | 13 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-13 |
| mc13-g20 | master | clang | 13 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-13 |
| dc13-17 | develop | clang | 13 | -std=c++17 | teeks99/boost-cpp-docker:clang-13 |
| mc13-17 | master | clang | 13 | -std=c++17 | teeks99/boost-cpp-docker:clang-13 |
| dc13-g17 | develop | clang | 13 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-13 |
| mc13-g17 | master | clang | 13 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-13 |
| dc13-14 | develop | clang | 13 | -std=c++14 | teeks99/boost-cpp-docker:clang-13 |
| mc13-14 | master | clang | 13 | -std=c++14 | teeks99/boost-cpp-docker:clang-13 |
| dc13-g14 | develop | clang | 13 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-13 |
| mc13-g14 | master | clang | 13 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-13 |
| dc13-11 | develop | clang | 13 | -std=c++11 | teeks99/boost-cpp-docker:clang-13 |
| mc13-11 | master | clang | 13 | -std=c++11 | teeks99/boost-cpp-docker:clang-13 |
| dc13-g11 | develop | clang | 13 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-13 |
| mc13-g11 | master | clang | 13 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-13 |
| dc13-98 | develop | clang | 13 | -std=c++98 | teeks99/boost-cpp-docker:clang-13 |
| mc13-98 | master | clang | 13 | -std=c++98 | teeks99/boost-cpp-docker:clang-13 |
| dc13-g98 | develop | clang | 13 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-13 |
| mc13-g98 | master | clang | 13 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-13 |
| dc13-opt | develop | clang | 13 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-13 |
| mc13-opt | master | clang | 13 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-13 |
| dc13-warn | develop | clang | 13 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-13 |
| mc13-warn | master | clang | 13 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-13 |
| dc13-20-lc | develop | clang | 13 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-13 |
| mc13-20-lc | master | clang | 13 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-13 |
| dc14 | develop | clang | 14 | -std=c++20 | teeks99/boost-cpp-docker:clang-14 |
| mc14 | master | clang | 14 | -std=c++20 | teeks99/boost-cpp-docker:clang-14 |
| dc14-2b | develop | clang | 14 | -std=c++2b | teeks99/boost-cpp-docker:clang-14 |
| mc14-2b | master | clang | 14 | -std=c++2b | teeks99/boost-cpp-docker:clang-14 |
| dc14-g2b | develop | clang | 14 | -std=gnu++2b | teeks99/boost-cpp-docker:clang-14 |
| mc14-g2b | master | clang | 14 | -std=gnu++2b | teeks99/boost-cpp-docker:clang-14 |
| dc14-20 | develop | clang | 14 | -std=c++20 | teeks99/boost-cpp-docker:clang-14 |
| mc14-20 | master | clang | 14 | -std=c++20 | teeks99/boost-cpp-docker:clang-14 |
| dc14-g20 | develop | clang | 14 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-14 |
| mc14-g20 | master | clang | 14 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-14 |
| dc14-17 | develop | clang | 14 | -std=c++17 | teeks99/boost-cpp-docker:clang-14 |
| mc14-17 | master | clang | 14 | -std=c++17 | teeks99/boost-cpp-docker:clang-14 |
| dc14-g17 | develop | clang | 14 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-14 |
| mc14-g17 | master | clang | 14 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-14 |
| dc14-14 | develop | clang | 14 | -std=c++14 | teeks99/boost-cpp-docker:clang-14 |
| mc14-14 | master | clang | 14 | -std=c++14 | teeks99/boost-cpp-docker:clang-14 |
| dc14-g14 | develop | clang | 14 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-14 |
| mc14-g14 | master | clang | 14 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-14 |
| dc14-11 | develop | clang | 14 | -std=c++11 | teeks99/boost-cpp-docker:clang-14 |
| mc14-11 | master | clang | 14 | -std=c++11 | teeks99/boost-cpp-docker:clang-14 |
| dc14-g11 | develop | clang | 14 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-14 |
| mc14-g11 | master | clang | 14 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-14 |
| dc14-98 | develop | clang | 14 | -std=c++98 | teeks99/boost-cpp-docker:clang-14 |
| mc14-98 | master | clang | 14 | -std=c++98 | teeks99/boost-cpp-docker:clang-14 |
| dc14-g98 | develop | clang | 14 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-14 |
| mc14-g98 | master | clang | 14 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-14 |
| dc14-opt | develop | clang | 14 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-14 |
| mc14-opt | master | clang | 14 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-14 |
| dc14-warn | develop | clang | 14 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-14 |
| mc14-warn | master | clang | 14 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-14 |
| dc14-20-lc | develop | clang | 14 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-14 |
| mc14-20-lc | master | clang | 14 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-14 |
| dc15 | develop | clang | 15 | -std=c++20 | teeks99/boost-cpp-docker:clang-15 |
| mc15 | master | clang | 15 | -std=c++20 | teeks99/boost-cpp-docker:clang-15 |
| dc15-2b | develop | clang | 15 | -std=c++2b | teeks99/boost-cpp-docker:clang-15 |
| mc15-2b | master | clang | 15 | -std=c++2b | teeks99/boost-cpp-docker:clang-15 |
| dc15-g2b | develop | clang | 15 | -std=gnu++2b | teeks99/boost-cpp-docker:clang-15 |
| mc15-g2b | master | clang | 15 | -std=gnu++2b | teeks99/boost-cpp-docker:clang-15 |
| dc15-20 | develop | clang | 15 | -std=c++20 | teeks99/boost-cpp-docker:clang-15 |
| mc15-20 | master | clang | 15 | -std=c++20 | teeks99/boost-cpp-docker:clang-15 |
| dc15-g20 | develop | clang | 15 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-15 |
| mc15-g20 | master | clang | 15 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-15 |
| dc15-17 | develop | clang | 15 | -std=c++17 | teeks99/boost-cpp-docker:clang-15 |
| mc15-17 | master | clang | 15 | -std=c++17 | teeks99/boost-cpp-docker:clang-15 |
| dc15-g17 | develop | clang | 15 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-15 |
| mc15-g17 | master | clang | 15 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-15 |
| dc15-14 | develop | clang | 15 | -std=c++14 | teeks99/boost-cpp-docker:clang-15 |
| mc15-14 | master | clang | 15 | -std=c++14 | teeks99/boost-cpp-docker:clang-15 |
| dc15-g14 | develop | clang | 15 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-15 |
| mc15-g14 | master | clang | 15 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-15 |
| dc15-11 | develop | clang | 15 | -std=c++11 | teeks99/boost-cpp-docker:clang-15 |
| mc15-11 | master | clang | 15 | -std=c++11 | teeks99/boost-cpp-docker:clang-15 |
| dc15-g11 | develop | clang | 15 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-15 |
| mc15-g11 | master | clang | 15 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-15 |
| dc15-98 | develop | clang | 15 | -std=c++98 | teeks99/boost-cpp-docker:clang-15 |
| mc15-98 | master | clang | 15 | -std=c++98 | teeks99/boost-cpp-docker:clang-15 |
| dc15-g98 | develop | clang | 15 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-15 |
| mc15-g98 | master | clang | 15 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-15 |
| dc15-opt | develop | clang | 15 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-15 |
| mc15-opt | master | clang | 15 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-15 |
| dc15-warn | develop | clang | 15 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-15 |
| mc15-warn | master | clang | 15 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-15 |
| dc15-20-lc | develop | clang | 15 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-15 |
| mc15-20-lc | master | clang | 15 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-15 |
| dc16 | develop | clang | 16 | -std=c++20 | teeks99/boost-cpp-docker:clang-16 |
| mc16 | master | clang | 16 | -std=c++20 | teeks99/boost-cpp-docker:clang-16 |
| dc16-2b | develop | clang | 16 | -std=c++2b | teeks99/boost-cpp-docker:clang-16 |
| mc16-2b | master | clang | 16 | -std=c++2b | teeks99/boost-cpp-docker:clang-16 |
| dc16-g2b | develop | clang | 16 | -std=gnu++2b | teeks99/boost-cpp-docker:clang-16 |
| mc16-g2b | master | clang | 16 | -std=gnu++2b | teeks99/boost-cpp-docker:clang-16 |
| dc16-20 | develop | clang | 16 | -std=c++20 | teeks99/boost-cpp-docker:clang-16 |
| mc16-20 | master | clang | 16 | -std=c++20 | teeks99/boost-cpp-docker:clang-16 |
| dc16-g20 | develop | clang | 16 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-16 |
| mc16-g20 | master | clang | 16 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-16 |
| dc16-17 | develop | clang | 16 | -std=c++17 | teeks99/boost-cpp-docker:clang-16 |
| mc16-17 | master | clang | 16 | -std=c++17 | teeks99/boost-cpp-docker:clang-16 |
| dc16-g17 | develop | clang | 16 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-16 |
| mc16-g17 | master | clang | 16 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-16 |
| dc16-14 | develop | clang | 16 | -std=c++14 | teeks99/boost-cpp-docker:clang-16 |
| mc16-14 | master | clang | 16 | -std=c++14 | teeks99/boost-cpp-docker:clang-16 |
| dc16-g14 | develop | clang | 16 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-16 |
| mc16-g14 | master | clang | 16 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-16 |
| dc16-11 | develop | clang | 16 | -std=c++11 | teeks99/boost-cpp-docker:clang-16 |
| mc16-11 | master | clang | 16 | -std=c++11 | teeks99/boost-cpp-docker:clang-16 |
| dc16-g11 | develop | clang | 16 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-16 |
| mc16-g11 | master | clang | 16 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-16 |
| dc16-98 | develop | clang | 16 | -std=c++98 | teeks99/boost-cpp-docker:clang-16 |
| mc16-98 | master | clang | 16 | -std=c++98 | teeks99/boost-cpp-docker:clang-16 |
| dc16-g98 | develop | clang | 16 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-16 |
| mc16-g98 | master | clang | 16 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-16 |
| dc16-opt | develop | clang | 16 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-16 |
| mc16-opt | master | clang | 16 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-16 |
| dc16-warn | develop | clang | 16 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-16 |
| mc16-warn | master | clang | 16 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-16 |
| dc16-20-lc | develop | clang | 16 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-16 |
| mc16-20-lc | master | clang | 16 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-16 |
| dc17 | develop | clang | 17 | -std=c++20 | teeks99/boost-cpp-docker:clang-17 |
| mc17 | master | clang | 17 | -std=c++20 | teeks99/boost-cpp-docker:clang-17 |
| dc17-2b | develop | clang | 17 | -std=c++2b | teeks99/boost-cpp-docker:clang-17 |
| mc17-2b | master | clang | 17 | -std=c++2b | teeks99/boost-cpp-docker:clang-17 |
| dc17-g2b | develop | clang | 17 | -std=gnu++2b | teeks99/boost-cpp-docker:clang-17 |
| mc17-g2b | master | clang | 17 | -std=gnu++2b | teeks99/boost-cpp-docker:clang-17 |
| dc17-20 | develop | clang | 17 | -std=c++20 | teeks99/boost-cpp-docker:clang-17 |
| mc17-20 | master | clang | 17 | -std=c++20 | teeks99/boost-cpp-docker:clang-17 |
| dc17-g20 | develop | clang | 17 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-17 |
| mc17-g20 | master | clang | 17 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-17 |
| dc17-17 | develop | clang | 17 | -std=c++17 | teeks99/boost-cpp-docker:clang-17 |
| mc17-17 | master | clang | 17 | -std=c++17 | teeks99/boost-cpp-docker:clang-17 |
| dc17-g17 | develop | clang | 17 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-17 |
| mc17-g17 | master | clang | 17 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-17 |
| dc17-14 | develop | clang | 17 | -std=c++14 | teeks99/boost-cpp-docker:clang-17 |
| mc17-14 | master | clang | 17 | -std=c++14 | teeks99/boost-cpp-docker:clang-17 |
| dc17-g14 | develop | clang | 17 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-17 |
| mc17-g14 | master | clang | 17 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-17 |
| dc17-11 | develop | clang | 17 | -std=c++11 | teeks99/boost-cpp-docker:clang-17 |
| mc17-11 | master | clang | 17 | -std=c++11 | teeks99/boost-cpp-docker:clang-17 |
| dc17-g11 | develop | clang | 17 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-17 |
| mc17-g11 | master | clang | 17 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-17 |
| dc17-98 | develop | clang | 17 | -std=c++98 | teeks99/boost-cpp-docker:clang-17 |
| mc17-98 | master | clang | 17 | -std=c++98 | teeks99/boost-cpp-docker:clang-17 |
| dc17-g98 | develop | clang | 17 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-17 |
| mc17-g98 | master | clang | 17 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-17 |
| dc17-opt | develop | clang | 17 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-17 |
| mc17-opt | master | clang | 17 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-17 |
| dc17-warn | develop | clang | 17 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-17 |
| mc17-warn | master | clang | 17 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-17 |
| dc17-20-lc | develop | clang | 17 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-17 |
| mc17-20-lc | master | clang | 17 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-17 |
| dc18 | develop | clang | 18 | -std=c++20 | teeks99/boost-cpp-docker:clang-18 |
| mc18 | master | clang | 18 | -std=c++20 | teeks99/boost-cpp-docker:clang-18 |
| dc18-2b | develop | clang | 18 | -std=c++2b | teeks99/boost-cpp-docker:clang-18 |
| mc18-2b | master | clang | 18 | -std=c++2b | teeks99/boost-cpp-docker:clang-18 |
| dc18-g2b | develop | clang | 18 | -std=gnu++2b | teeks99/boost-cpp-docker:clang-18 |
| mc18-g2b | master | clang | 18 | -std=gnu++2b | teeks99/boost-cpp-docker:clang-18 |
| dc18-20 | develop | clang | 18 | -std=c++20 | teeks99/boost-cpp-docker:clang-18 |
| mc18-20 | master | clang | 18 | -std=c++20 | teeks99/boost-cpp-docker:clang-18 |
| dc18-g20 | develop | clang | 18 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-18 |
| mc18-g20 | master | clang | 18 | -std=gnu++20 | teeks99/boost-cpp-docker:clang-18 |
| dc18-17 | develop | clang | 18 | -std=c++17 | teeks99/boost-cpp-docker:clang-18 |
| mc18-17 | master | clang | 18 | -std=c++17 | teeks99/boost-cpp-docker:clang-18 |
| dc18-g17 | develop | clang | 18 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-18 |
| mc18-g17 | master | clang | 18 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-18 |
| dc18-14 | develop | clang | 18 | -std=c++14 | teeks99/boost-cpp-docker:clang-18 |
| mc18-14 | master | clang | 18 | -std=c++14 | teeks99/boost-cpp-docker:clang-18 |
| dc18-g14 | develop | clang | 18 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-18 |
| mc18-g14 | master | clang | 18 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-18 |
| dc18-11 | develop | clang | 18 | -std=c++11 | teeks99/boost-cpp-docker:clang-18 |
| mc18-11 | master | clang | 18 | -std=c++11 | teeks99/boost-cpp-docker:clang-18 |
| dc18-g11 | develop | clang | 18 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-18 |
| mc18-g11 | master | clang | 18 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-18 |
| dc18-98 | develop | clang | 18 | -std=c++98 | teeks99/boost-cpp-docker:clang-18 |
| mc18-98 | master | clang | 18 | -std=c++98 | teeks99/boost-cpp-docker:clang-18 |
| dc18-g98 | develop | clang | 18 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-18 |
| mc18-g98 | master | clang | 18 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-18 |
| dc18-opt | develop | clang | 18 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-18 |
| mc18-opt | master | clang | 18 | -std=c++20 -O2 | teeks99/boost-cpp-docker:clang-18 |
| dc18-warn | develop | clang | 18 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-18 |
| mc18-warn | master | clang | 18 | -std=c++20 -Wall -Wextra | teeks99/boost-cpp-docker:clang-18 |
| dc18-20-lc | develop | clang | 18 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-18 |
| mc18-20-lc | master | clang | 18 | -std=c++20 -stdlib=libc++ | teeks99/boost-cpp-docker:clang-18 |



Windows Regression Configurations
---------------------------------

The teeks99-09 tester will cycle through the various visual studio configurations msvc-10.0 through msvc-14.3.
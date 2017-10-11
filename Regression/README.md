Tom's Boost Regression Tests
============================

These regression runs are automated sets of the [Boost Regression Test Suite](http://www.boost.org/development/running_regression_tests.html) that have a set of python scripts that continuously run them in a loop. 

Each set of runs is controlled by its respective `machine_vars.json` file. 

Linux Regression Configurations
-------------------------------

On Linux we run versions of GCC (4.4 - 6) and Clang (3.0 - 3.9). 

Linux runs are executed within docker. The various docker images that are use can be found in the [Docker](..\Docker) directory of this git repo. They all run on the Ubuntu image for the LTS OS version that was in common use at the time of the compiler release. Each of these images has multiple compiler configurations defined in its `user-config.jam` file. There are too many configurations of compiler + switches to run tests against all the combinations.

In general, the teeks99-02 tester will run the most common switches option for each of the compilers against both the development and master branches. Then for the most recent version of each compiler only it will perform a run against each of the enumerated switch options against both develop and master. In total, this is nearly 100 configurations, each taking between 0.9 and 1.6 hours to execute. This results in a revist time for any single configuration of approximately five days. So that developers can have some results quicker, every approximately ten runs, the order will be paused and four runs will be executed consisiting of the latest version of each compiler, with the most common switches, against each of develop and master.

As opposed to the teeks99-02 runner, the teeks99-03 runner is optimized to provide rapid results to developers when they commit changes. This runner only has four configurations, the latest version of each of GCC and Clang with their most common switches, running against master and develop. This should ensure that a developer can see the results of their commit against a current GCC or Clang within three hours (plus a bit extra for the report to generate). 

| Name | Branch | Compiler | Version | Flags | Docker Image |
| ---- | ------ | -------- | ------- | ----- | ------------ |
| dg4.4-98 | develop | gcc | 4.4 | -std=c++98 | teeks99/boost-cpp-docker:gcc-4.4 |
| mg4.4-98 | master | gcc | 4.4 | -std=c++98 | teeks99/boost-cpp-docker:gcc-4.4 |
| dg4.4-0x | develop | gcc | 4.4 | -std=c++0x | teeks99/boost-cpp-docker:gcc-4.4 |
| mg4.4-0x | master | gcc | 4.4 | -std=c++0x | teeks99/boost-cpp-docker:gcc-4.4 |
| dg4.4-g98 | develop | gcc | 4.4 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-4.4 |
| mg4.4-g98 | master | gcc | 4.4 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-4.4 |
| dg4.4-g0x | develop | gcc | 4.4 | -std=gnu++0x | teeks99/boost-cpp-docker:gcc-4.4 |
| mg4.4-g0x | master | gcc | 4.4 | -std=gnu++0x | teeks99/boost-cpp-docker:gcc-4.4 |
| dg4.4-opt | develop | gcc | 4.4 | -std=c++0x -O2 | teeks99/boost-cpp-docker:gcc-4.4 |
| mg4.4-opt | master | gcc | 4.4 | -std=c++0x -O2 | teeks99/boost-cpp-docker:gcc-4.4 |
| dg4.4-warn | develop | gcc | 4.4 | -std=c++0x -Wall -Wextra | teeks99/boost-cpp-docker:gcc-4.4 |
| mg4.4-warn | master | gcc | 4.4 | -std=c++0x -Wall -Wextra | teeks99/boost-cpp-docker:gcc-4.4 |
| dg4.5 | develop | gcc | 4.5 |  | teeks99/boost-cpp-docker:gcc-4.5 |
| mg4.5 | master | gcc | 4.5 |  | teeks99/boost-cpp-docker:gcc-4.5 |
| dg4.6 | develop | gcc | 4.6 |  | teeks99/boost-cpp-docker:gcc-4.6 |
| mg4.6 | master | gcc | 4.6 |  | teeks99/boost-cpp-docker:gcc-4.6 |
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
| dg7-14 | develop | gcc | 7 | -std=c++14 | teeks99/boost-cpp-docker:gcc-7 |
| mg7-14 | master | gcc | 7 | -std=c++14 | teeks99/boost-cpp-docker:gcc-7 |
| dg7-g14 | develop | gcc | 7 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-7 |
| mg7-g14 | master | gcc | 7 | -std=gnu++14 | teeks99/boost-cpp-docker:gcc-7 |
| dg7-1z | develop | gcc | 7 | -std=c++1z | teeks99/boost-cpp-docker:gcc-7 |
| mg7-1z | master | gcc | 7 | -std=c++1z | teeks99/boost-cpp-docker:gcc-7 |
| dg7-g1z | develop | gcc | 7 | -std=gnu++1z | teeks99/boost-cpp-docker:gcc-7 |
| mg7-g1z | master | gcc | 7 | -std=gnu++1z | teeks99/boost-cpp-docker:gcc-7 |
| dg7-11 | develop | gcc | 7 | -std=c++11 | teeks99/boost-cpp-docker:gcc-7 |
| mg7-11 | master | gcc | 7 | -std=c++11 | teeks99/boost-cpp-docker:gcc-7 |
| dg7-g11 | develop | gcc | 7 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-7 |
| mg7-g11 | master | gcc | 7 | -std=gnu++11 | teeks99/boost-cpp-docker:gcc-7 |
| dg7-98 | develop | gcc | 7 | -std=c++98 | teeks99/boost-cpp-docker:gcc-7 |
| mg7-98 | master | gcc | 7 | -std=c++98 | teeks99/boost-cpp-docker:gcc-7 |
| dg7-g98 | develop | gcc | 7 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-7 |
| mg7-g98 | master | gcc | 7 | -std=gnu++98 | teeks99/boost-cpp-docker:gcc-7 |
| dg7-opt | develop | gcc | 7 | -std=c++1z -O2 | teeks99/boost-cpp-docker:gcc-7 |
| mg7-opt | master | gcc | 7 | -std=c++1z -O2 | teeks99/boost-cpp-docker:gcc-7 |
| dg7-warn | develop | gcc | 7 | -std=c++1z -Wall -Wextra | teeks99/boost-cpp-docker:gcc-7 |
| mg7-warn | master | gcc | 7 | -std=c++1z -Wall -Wextra | teeks99/boost-cpp-docker:gcc-7 |
| dc3.0-98 | develop | clang | 3.0 | -std=c++98 | teeks99/boost-cpp-docker:clang-3.0 |
| mc3.0-98 | master | clang | 3.0 | -std=c++98 | teeks99/boost-cpp-docker:clang-3.0 |
| dc3.0-g98 | develop | clang | 3.0 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-3.0 |
| mc3.0-g98 | master | clang | 3.0 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-3.0 |
| dc3.0-11 | develop | clang | 3.0 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.0 |
| mc3.0-11 | master | clang | 3.0 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.0 |
| dc3.0-g11 | develop | clang | 3.0 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-3.0 |
| mc3.0-g11 | master | clang | 3.0 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-3.0 |
| dc3.0-opt | develop | clang | 3.0 | -std=c++11 -O2 | teeks99/boost-cpp-docker:clang-3.0 |
| mc3.0-opt | master | clang | 3.0 | -std=c++11 -O2 | teeks99/boost-cpp-docker:clang-3.0 |
| dc3.0-warn | develop | clang | 3.0 | -std=c++11 -Wall -Wextra | teeks99/boost-cpp-docker:clang-3.0 |
| mc3.0-warn | master | clang | 3.0 | -std=c++11 -Wall -Wextra | teeks99/boost-cpp-docker:clang-3.0 |
| dc3.1-11 | develop | clang | 3.1 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.1 |
| mc3.1-11 | master | clang | 3.1 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.1 |
| dc3.2-11 | develop | clang | 3.2 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.2 |
| mc3.2-11 | master | clang | 3.2 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.2 |
| dc3.3-11 | develop | clang | 3.3 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.3 |
| mc3.3-11 | master | clang | 3.3 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.3 |
| dc3.4-11 | develop | clang | 3.4 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.4 |
| mc3.4-11 | master | clang | 3.4 | -std=c++11 | teeks99/boost-cpp-docker:clang-3.4 |
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
| dc5-g14 | develop | clang | 5.0 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-5 |
| mc5-g14 | master | clang | 5.0 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-5 |
| dc5-1z | develop | clang | 5.0 | -std=c++1z | teeks99/boost-cpp-docker:clang-5 |
| mc5-1z | master | clang | 5.0 | -std=c++1z | teeks99/boost-cpp-docker:clang-5 |
| dc5-g1z | develop | clang | 5.0 | -std=gnu++1z | teeks99/boost-cpp-docker:clang-5 |
| mc5-g1z | master | clang | 5.0 | -std=gnu++1z | teeks99/boost-cpp-docker:clang-5 |
| dc5-11 | develop | clang | 5.0 | -std=c++11 | teeks99/boost-cpp-docker:clang-5 |
| mc5-11 | master | clang | 5.0 | -std=c++11 | teeks99/boost-cpp-docker:clang-5 |
| dc5-g11 | develop | clang | 5.0 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-5 |
| mc5-g11 | master | clang | 5.0 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-5 |
| dc5-98 | develop | clang | 5.0 | -std=c++98 | teeks99/boost-cpp-docker:clang-5 |
| mc5-98 | master | clang | 5.0 | -std=c++98 | teeks99/boost-cpp-docker:clang-5 |
| dc5-g98 | develop | clang | 5.0 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-5 |
| mc5-g98 | master | clang | 5.0 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-5 |
| dc5-opt | develop | clang | 5.0 | -std=c++1z -O2 | teeks99/boost-cpp-docker:clang-5 |
| mc5-opt | master | clang | 5.0 | -std=c++1z -O2 | teeks99/boost-cpp-docker:clang-5 |
| dc5-warn | develop | clang | 5.0 | -std=c++1z -Wall -Wextra | teeks99/boost-cpp-docker:clang-5 |
| mc5-warn | master | clang | 5.0 | -std=c++1z -Wall -Wextra | teeks99/boost-cpp-docker:clang-5 |
| dc5-1z-lc | develop | clang | 5.0 | -std=c++1z -stdlib=libc++ | teeks99/boost-cpp-docker:clang-5 |
| mc5-1z-lc | master | clang | 5.0 | -std=c++1z -stdlib=libc++ | teeks99/boost-cpp-docker:clang-5 |
| dc6-14 | develop | clang | 6.0 | -std=c++14 | teeks99/boost-cpp-docker:clang-6 |
| mc6-14 | master | clang | 6.0 | -std=c++14 | teeks99/boost-cpp-docker:clang-6 |
| dc6-g14 | develop | clang | 6.0 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-6 |
| mc6-g14 | master | clang | 6.0 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-6 |
| dc6-1z | develop | clang | 6.0 | -std=c++1z | teeks99/boost-cpp-docker:clang-6 |
| mc6-1z | master | clang | 6.0 | -std=c++1z | teeks99/boost-cpp-docker:clang-6 |
| dc6-g1z | develop | clang | 6.0 | -std=gnu++1z | teeks99/boost-cpp-docker:clang-6 |
| mc6-g1z | master | clang | 6.0 | -std=gnu++1z | teeks99/boost-cpp-docker:clang-6 |
| dc6-11 | develop | clang | 6.0 | -std=c++11 | teeks99/boost-cpp-docker:clang-6 |
| mc6-11 | master | clang | 6.0 | -std=c++11 | teeks99/boost-cpp-docker:clang-6 |
| dc6-g11 | develop | clang | 6.0 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-6 |
| mc6-g11 | master | clang | 6.0 | -std=gnu++11 | teeks99/boost-cpp-docker:clang-6 |
| dc6-98 | develop | clang | 6.0 | -std=c++98 | teeks99/boost-cpp-docker:clang-6 |
| mc6-98 | master | clang | 6.0 | -std=c++98 | teeks99/boost-cpp-docker:clang-6 |
| dc6-g98 | develop | clang | 6.0 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-6 |
| mc6-g98 | master | clang | 6.0 | -std=gnu++98 | teeks99/boost-cpp-docker:clang-6 |
| dc6-opt | develop | clang | 6.0 | -std=c++1z -O2 | teeks99/boost-cpp-docker:clang-6 |
| mc6-opt | master | clang | 6.0 | -std=c++1z -O2 | teeks99/boost-cpp-docker:clang-6 |
| dc6-warn | develop | clang | 6.0 | -std=c++1z -Wall -Wextra | teeks99/boost-cpp-docker:clang-6 |
| mc6-warn | master | clang | 6.0 | -std=c++1z -Wall -Wextra | teeks99/boost-cpp-docker:clang-6 |
| dc6-1z-lc | develop | clang | 6.0 | -std=c++1z -stdlib=libc++ | teeks99/boost-cpp-docker:clang-6 |
| mc6-1z-lc | master | clang | 6.0 | -std=c++1z -stdlib=libc++ | teeks99/boost-cpp-docker:clang-6 |



Windows Regression Configurations
---------------------------------

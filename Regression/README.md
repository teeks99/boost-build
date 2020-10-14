Tom's Boost Regression Tests
============================

These regression runs are automated sets of the [Boost Regression Test Suite](http://www.boost.org/development/running_regression_tests.html) that have a set of python scripts that continuously run them in a loop. 

Each set of runs is controlled by its respective `machine_vars.json` file. 

Linux Regression Configurations
-------------------------------

On Linux we run versions of GCC (4.4 - 7) and Clang (3.0 - 6). 

Linux runs are executed within docker. The various docker images that are use can be found in the corresponding [Docker](http://github.com/teeks99/boost-cpp-docker) repo. They all run on the Ubuntu image for the LTS OS version that was in common use at the time of the compiler release. Each of these images has multiple compiler configurations defined in its `user-config.jam` file. There are too many configurations of compiler + switches to run tests against all the combinations.

In general, the teeks99-02 tester will run the most common switches option for each of the compilers against both the development and master branches. Then for the most recent version of each compiler only it will perform a run against each of the enumerated switch options against both develop and master. In total, this is nearly 100 configurations, each taking between 0.9 and 1.6 hours to execute. This results in a revist time for any single configuration of approximately five days. So that developers can have some results quicker, every approximately ten runs, the order will be paused and four runs will be executed consisiting of the latest version of each compiler, with the most common switches, against each of develop and master.

As opposed to the teeks99-02 runner, the teeks99-03 runner is optimized to provide rapid results to developers when they commit changes. This runner only has four configurations, the latest version of each of GCC and Clang with their most common switches, running against master and develop. This should ensure that a developer can see the results of their commit against a current GCC or Clang within three hours (plus a bit extra for the report to generate). 

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
| dc11 | develop | clang | 11 | -std=c++17 | teeks99/boost-cpp-docker:clang-11 |
| mc11 | master | clang | 11 | -std=c++17 | teeks99/boost-cpp-docker:clang-11 |
| dc11-20 | develop | clang | 11 | -std=c++20 | teeks99/boost-cpp-docker:clang-11 |
| mc11-20 | master | clang | 11 | -std=c++20 | teeks99/boost-cpp-docker:clang-11 |
| dc11-14 | develop | clang | 11 | -std=c++14 | teeks99/boost-cpp-docker:clang-11 |
| mc11-14 | master | clang | 11 | -std=c++14 | teeks99/boost-cpp-docker:clang-11 |
| dc11-g14 | develop | clang | 11 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-11 |
| mc11-g14 | master | clang | 11 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-11 |
| dc11-17 | develop | clang | 11 | -std=c++17 | teeks99/boost-cpp-docker:clang-11 |
| mc11-17 | master | clang | 11 | -std=c++17 | teeks99/boost-cpp-docker:clang-11 |
| dc11-g17 | develop | clang | 11 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-11 |
| mc11-g17 | master | clang | 11 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-11 |
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
| dc12 | develop | clang | 12 | -std=c++17 | teeks99/boost-cpp-docker:clang-12 |
| mc12 | master | clang | 12 | -std=c++17 | teeks99/boost-cpp-docker:clang-12 |
| dc12-20 | develop | clang | 12 | -std=c++20 | teeks99/boost-cpp-docker:clang-12 |
| mc12-20 | master | clang | 12 | -std=c++20 | teeks99/boost-cpp-docker:clang-12 |
| dc12-14 | develop | clang | 12 | -std=c++14 | teeks99/boost-cpp-docker:clang-12 |
| mc12-14 | master | clang | 12 | -std=c++14 | teeks99/boost-cpp-docker:clang-12 |
| dc12-g14 | develop | clang | 12 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-12 |
| mc12-g14 | master | clang | 12 | -std=gnu++14 | teeks99/boost-cpp-docker:clang-12 |
| dc12-17 | develop | clang | 12 | -std=c++17 | teeks99/boost-cpp-docker:clang-12 |
| mc12-17 | master | clang | 12 | -std=c++17 | teeks99/boost-cpp-docker:clang-12 |
| dc12-g17 | develop | clang | 12 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-12 |
| mc12-g17 | master | clang | 12 | -std=gnu++17 | teeks99/boost-cpp-docker:clang-12 |
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



Windows Regression Configurations
---------------------------------

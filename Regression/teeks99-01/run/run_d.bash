TMP=/var/boost/tmp
export TMP

cd /var/boost/run/
#python2.7 run.py --runner=teeks99-01b-Ubuntu14.04-64 --bjam-toolset=gcc --pjl-toolset=gcc --toolsets=clang-3.6 --tag=develop --bjam-options=-j4 --comment=info.html 2>&1 | tee output.log
python2.7 run.py --runner=teeks99-01d-Ubuntu14.04-64 --toolsets=clang-3.6 --tag=master --bjam-options=-j4 --comment=info.html 2>&1 | tee output.log

rm -rf boost_bb
rm -rf boost_regression*
rm -rf results


TMP=/var/boost/tmp
export TMP

cd /var/boost/run/
python2.7 run.py --runner=teeks99-01b-Ubuntu14.04-64 --toolsets=clang-3.6 --tag=develop --bjam-options=-j4 --comment=info.html 2>&1 | tee output.log


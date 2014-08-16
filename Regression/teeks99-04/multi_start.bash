rm output.log
echo Starting at: `date` > run_started.log

rsync -a ../boost_root/ boost_root/
pushd boost_root
git checkout develop
popd

source vars.bash

python run.py --runner=teeks99-04${id}-Ubuntu12.04-64 --toolsets=${tools} --force-update --bjam-options=-j2 --tag=develop --comment=../info.html 2>&1 | tee output.log

rm -rf boost_root/ results/
rm -rf tmp/*.cpp

mv run_started.log last_run.log
echo Finished at: `date` >> last_run.log

rm output.log
echo Starting at: `date` > run_started.log

python run.py --runner=teeks99-06b-Ubuntu12.04-64 --toolsets=gcc-4.5 --force-update --bjam-options=-j2 --comment=info.html 2>&1 | tee output.log

mv run_started.log last_run.log
echo Finished at: `date` >> last_run.log

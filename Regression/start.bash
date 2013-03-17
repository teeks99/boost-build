rm last_run.log
rm output.log

echo Starting at: `date` > run_started.log

#python run.py --runner=teeks99-5-Ubuntu12.04-64 --toolsets=gcc-4.4,gcc-4.5,gcc-4.6,gcc-4.7,clang-3.0 --comment=info.html 2>&1 | tee output.log

python run.py --runner=teeks99-5-Ubuntu12.04-64 --toolsets=gcc-4.4 --comment=info.html 2>&1 | tee output.log

mv run_started.log last_run.log
echo Finished at: `date` >> last_run.log

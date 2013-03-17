cd C:\local\regression
echo Starting at: %DATE% %TIME% > run_started.log

python run.py --runner=teeks99-08-win7-64on64 --incremental --toolsets=msvc-11.0 --bjam-options=address-model=64 --comment=info.html 2>&1 | wtee output.log

del last_run.log
move run_started.log last_run.log
echo Finished at: %DATE% %TIME% >> last_run.log

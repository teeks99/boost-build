cd C:\local\regression
del last_run.log
echo Starting at: %DATE% %TIME% > run_started.log

python run.py --runner=teeks99-01a-win7-32on64 --incremental --toolsets=msvc-10.0,msvc-11.0 --bjam-options=-j2 --comment=info.html 2>&1 | wtee output.log

move run_started.log last_run.log
echo Finished at: %DATE% %TIME% >> last_run.log

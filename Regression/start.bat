cd C:\local\regression
del last_run.log
echo Starting at: %DATE% %TIME% > run_started.log

echo "python run.py --runner=teeks99-2-win7-64 --toolsets=msvc-8.0,msvc-9.0,msvc-10.0 --comment=info.html 2>&1 | wtee output.log"
python run.py --runner=teeks99-2-win7-64 --toolsets=msvc-8.0,msvc-9.0,msvc-10.0 --comment=info.html 2>&1 | wtee output.log

move run_started.log last_run.log
echo Finished at: %DATE% %TIME% >> last_run.log
cd C:\local\regression
echo Starting at: %DATE% %TIME% > run_started.log

python run.py --runner=teeks99-03-win7-64on64 --incremental --toolsets=msvc-8.0,msvc-9.0 --bjam-options="-j2 address-model=64" --comment=info.html 2>&1 | wtee output.log

del last_run.log
move run_started.log last_run.log
echo Finished at: %DATE% %TIME% >> last_run.log

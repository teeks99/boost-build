cd C:\local\regression
echo Starting at: %DATE% %TIME% > run_started.log

call vars.bat

python run.py --runner=teeks99-03%id%-win7-64on64 --force-update --toolsets=%toolset% --bjam-options="-j4 address-model=64" --comment=..\info.html 2>&1 | ..\wtee output.log

rd /s/q results
rd /s/q %TEMP%

del last_run.log
move run_started.log last_run.log
echo Finished at: %DATE% %TIME% >> last_run.log

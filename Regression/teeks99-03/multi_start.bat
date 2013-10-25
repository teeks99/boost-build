echo Starting at: %DATE% %TIME% > run_started.log

call vars.bat

python run.py --timeout=10 --runner=teeks99-03%id%-win2008-64on64 --force-update --toolsets=%toolset% --bjam-options="-j2 address-model=64" --comment=..\info.html 2>&1 | ..\wtee output.log

copy results\bjam.log .\
rd /s/q results
rd /s/q %TEMP%
mkdir %TEMP%

del last_run.log
move run_started.log last_run.log
echo Finished at: %DATE% %TIME% >> last_run.log

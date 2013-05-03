del loop_finished.log
:loop
cd d
call multi_start.bat
cd ..

echo %DATE% %TIME% >> loop_finished.log
goto loop

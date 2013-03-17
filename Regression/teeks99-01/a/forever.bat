del loop_finished.log
:loop
call start.bat
echo %DATE% %TIME% >> loop_finished.log
goto loop

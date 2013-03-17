del loop_finished.log
:loop
cd a
call start.bat
cd ..

cd b
call start.bat
cd ..

echo %DATE% %TIME% >> loop_finished.log
goto loop

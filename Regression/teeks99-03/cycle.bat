del loop_finished.log
:loop
cd a
call multi_start.bat
cd ..

cd b
call multi_start.bat
cd ..

cd c
call multi_start.bat
cd ..

cd d
call multi_start.bat
cd ..

echo %DATE% %TIME% >> loop_finished.log
goto loop

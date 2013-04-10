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

cd e
call multi_start_release.bat
cd ..

cd f
call multi_start_release.bat
cd ..

cd g
call multi_start_release.bat
cd ..

cd h
call multi_start_release.bat
cd ..

echo %DATE% %TIME% >> loop_finished.log
goto loop

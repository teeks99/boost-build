
set boost_version=%1
set buildRoot=C:\BoostBuilding
::set bjam="%buildRoot%\boost-jam-3.1.18-1-ntx86\bjam.exe"
set bjam=.\bjam
set zip="%buildRoot%\7z465\7z.exe"
set inno="C:\Program Files (x86)\Inno Setup 5\Compil32.exe"
set sed="%buildRoot%\bin-sed\sed.exe"


IF "_%boost_version%"=="_" (
	echo "You must enter the boost version (e.g. boost_1_41_0) as an argument"
	pause
	exit
)

REM If you've already done this you can skip it (and the overwrite prompts)
::set SKIP_UNZIP=TRUE
IF NOT "%SKIP_UNZIP%"=="TRUE" (
	::%zip% x Python26-32.tar.gz
	::%zip% x Python26-32.tar
	::%zip% x Python26-64.tar.gz
	::%zip% x Python26-64.tar
        %zip% x Python27-32.7z
        %zip% x Python27-64.7z
	%zip% x zlib-1.2.8.tar.gz
	%zip% x zlib-1.2.8.tar
	%zip% x bzip2-1.0.6.tar.gz
	%zip% x bzip2-1.0.6.tar
)

REM Enables the zlib and bz2 libraries for the iostream library
set ZLIB_SOURCE="%buildRoot%\zlib-1.2.8"
set BZIP2_SOURCE="%buildRoot%\bzip2-1.0.6"

%zip% x %boost_version%.tar.*
%zip% x %boost_version%.tar

cd %boost_version%

call .\bootstrap.bat

del %boost_version%\32bitlog.txt
del %boost_version%\64bitlog.txt

call:BuildVersion 8.0 32
call:BuildVersion 9.0 32
call:BuildVersion 10.0 32
call:BuildVersion 11.0 32
call:BuildVersion 12.0 32
call:BuildVersion 14.0 32
call:BuildVersion 8.0 64
call:BuildVersion 9.0 64
call:BuildVersion 10.0 64
call:BuildVersion 11.0 64
call:BuildVersion 12.0 64
call:BuildVersion 14.0 64

cd ..

copy %boost_version%\32bitlog.txt %boost_version%-32bitlog.txt
copy %boost_version%\64bitlog.txt %boost_version%-64bitlog.txt

start "Build Output" notepad %boost_version%-32bitlog.txt
start "Build Output" notepad %boost_version%-64bitlog.txt

rd /S/Q %boost_version%\garbage_headers

copy DEPENDENCY_VERSIONS.txt %boost_version%

move %boost_version%\bin.v2 .\
%zip% a %boost_version%-bin-msvc-all-32-64.7z %boost_version%
move bin.v2 %boost_version%\

move %boost_version% %boost_version%_complete
%zip% x %boost_version%.tar

call:MakeInstaller 8.0 32
call:MakeInstaller 9.0 32
call:MakeInstaller 10.0 32
call:MakeInstaller 11.0 32
call:MakeInstaller 12.0 32
call:MakeInstaller 14.0 32
call:MakeInstaller 8.0 64
call:MakeInstaller 9.0 64
call:MakeInstaller 10.0 64
call:MakeInstaller 11.0 64
call:MakeInstaller 12.0 64
call:MakeInstaller 14.0 64

rd /S/Q %boost_version%
move %boost_version%_complete %boost_version%

echo Build Complete

goto:EOF

:BuildVersion
REM %bjam% -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-8.0 stage
REM mkdir lib32-msvc-8.0
REM move stage\lib\* lib32-msvc-8.0\

%bjam% -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-%~1 address-model=%~2 architecture=x86 --prefix=.\ --libdir=lib%~2-msvc-%~1 --includedir=garbage_headers install

REM Build again to log any errors in the build process
echo Build for msvc-%~1 >> %~2bitlog.txt
%bjam% --without-mpi --build-type=complete toolset=msvc-%~1 address-model=%~2 architecture=x86 --prefix=.\ --libdir=lib%~2-msvc-%~1 --includedir=garbage_headers install >> %~2bitlog.txt 2<&1

copy ..\DEPENDENCY_VERSIONS.txt lib%~2-msvc-%~1\

goto:EOF

:MakeInstaller
REM xcopy /E/Z/Y/I %boost_version%_complete\lib32-msvc-8.0 %boost_version%\lib32-msvc-8.0
REM %zip% a -tzip %boost_version%-msvc-8.0-32.7z %boost_version%
REM rd /S/Q %boost_version%\lib32-msvc-8.0

echo xcopy /E/Z/Y/I %boost_version%_complete\lib%~2-msvc-%~1 %boost_version%\lib%~2-msvc-%~1
xcopy /E/Z/Y/I %boost_version%_complete\lib%~2-msvc-%~1 %boost_version%\lib%~2-msvc-%~1

::echo %zip% a -tzip %boost_version%-msvc-%~1-%~2.zip %boost_version%
::%zip% a -tzip %boost_version%-msvc-%~1-%~2.zip %boost_version%

%sed% s/FILL_VERSION/%boost_version%/g BoostWinInstaller-Template.iss > tmp1.iss
%sed% s/FILL_CONFIG/msvc-%~1-%~2/g tmp1.iss > tmp2.iss
del tmp1.iss
move tmp2.iss BoostWinInstaller-msvc-%~1-%~2.iss
echo %inno% /cc BoostWinInstaller-msvc-%~1-%~2.iss
%inno% /cc BoostWinInstaller-msvc-%~1-%~2.iss
::del BoostWinInstaller-msvc-%~1-%~2.iss

echo rd /S/Q %boost_version%\lib%~2-msvc-%~1
rd /S/Q %boost_version%\lib%~2-msvc-%~1
goto:EOF

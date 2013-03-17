
set boost_version=%1
set buildRoot=C:\BoostBuilding
::set bjam="%buildRoot%\boost-jam-3.1.18-1-ntx86\bjam.exe"
set bjam=.\bjam
set zip="%buildRoot%\7z465\7z.exe"

IF "_%boost_version%"=="_" (
	echo "You must enter the boost version (e.g. boost_1_41_0) as an argument"
	pause
	exit
)

REM If you've already done this you can skip it (and the overwrite prompts)
::set SKIP_UNZIP=TRUE
IF NOT "%SKIP_UNZIP%"=="TRUE" (
	%zip% x Python26-32.tar.gz
	%zip% x Python26-32.tar
	%zip% x Python26-64.tar.gz
	%zip% x Python26-64.tar
	%zip% x zlib-1.2.6.tar.gz
	%zip% x zlib-1.2.6.tar
	%zip% x bzip2-1.0.6.tar.gz
	%zip% x bzip2-1.0.6.tar
)

REM Enables the zlib and bz2 libraries for the iostream library
set ZLIB_SOURCE="%buildRoot%\zlib-1.2.6"
set BZIP2_SOURCE="%buildRoot%\bzip2-1.0.6"

%zip% x %boost_version%.tar.*
%zip% x %boost_version%.tar

cd %boost_version%

call .\bootstrap.bat

%bjam% -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-8.0 stage
%bjam% -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-9.0 stage
%bjam% -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-10.0 stage
%bjam% -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-11.0 stage

echo 32-Bit Log > 32bitlog.txt
%bjam% --without-mpi --build-type=complete toolset=msvc-8.0 stage >> 32bitlog.txt 2<&1
%bjam% --without-mpi --build-type=complete toolset=msvc-9.0 stage >> 32bitlog.txt 2<&1
%bjam% --without-mpi --build-type=complete toolset=msvc-10.0 stage >> 32bitlog.txt 2<&1
%bjam% --without-mpi --build-type=complete toolset=msvc-11.0 stage >> 32bitlog.txt 2<&1

mkdir lib32
move stage\lib\* lib32\

%bjam% -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-8.0 address-model=64 stage
%bjam% -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-9.0 address-model=64 stage
%bjam% -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-10.0 address-model=64 stage
%bjam% -j%NUMBER_OF_PROCESSORS% --without-mpi --build-type=complete toolset=msvc-11.0 address-model=64 stage

echo 64-Bit Log > 64bitlog.txt
%bjam% --without-mpi --build-type=complete toolset=msvc-8.0 address-model=64 stage >> 64bitlog.txt 2<&1
%bjam% --without-mpi --build-type=complete toolset=msvc-9.0 address-model=64 stage >> 64bitlog.txt 2<&1
%bjam% --without-mpi --build-type=complete toolset=msvc-10.0 address-model=64 stage >> 64bitlog.txt 2<&1
%bjam% --without-mpi --build-type=complete toolset=msvc-11.0 address-model=64 stage >> 64bitlog.txt 2<&1

mkdir lib64
move stage\lib\* lib64\

REM create a self-extracting (-sfx), ultra compression level (-mx9) zip file for each set of binaries
%zip% a -sfx -mx9 %boost_version%-vc32-bin.exe lib32
%zip% a -sfx -mx9 %boost_version%-vc64-bin.exe lib64

start "Build Output" notepad 32bitlog.txt
start "Build Output" notepad 64bitlog.txt

cd ..

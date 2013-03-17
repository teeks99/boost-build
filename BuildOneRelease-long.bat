
set boost_version=%1
set bjam="C:\Program Files\boost-jam-3.1.17-1-ntx86\bjam.exe"
set zip="C:\Program Files\7-Zip\7z.exe"

IF "_%boost_version%"=="_" (
	echo "You must enter the boost version (e.g. boost_1_41_0) as an argument"
	pause
	exit
)

%zip% x %boost_version%.tar.gz
%zip% x %boost_version%.tar

cd %boost_version%

%bjam% toolset=msvc-7.1 variant=debug threading=multi link=shared runtime-link=shared stage
%bjam% toolset=msvc-7.1 variant=debug threading=multi link=static runtime-link=shared stage
%bjam% toolset=msvc-7.1 variant=debug threading=multi link=static runtime-link=static stage
%bjam% toolset=msvc-7.1 variant=debug threading=single link=static runtime-link=static stage
%bjam% toolset=msvc-7.1 variant=release threading=multi link=shared runtime-link=shared stage
%bjam% toolset=msvc-7.1 variant=release threading=multi link=static runtime-link=shared stage
%bjam% toolset=msvc-7.1 variant=release threading=multi link=static runtime-link=static stage
%bjam% toolset=msvc-7.1 variant=release threading=single link=static runtime-link=static stage
%bjam% toolset=msvc-8.0 variant=debug threading=multi link=shared runtime-link=shared stage
%bjam% toolset=msvc-8.0 variant=debug threading=multi link=static runtime-link=shared stage
%bjam% toolset=msvc-8.0 variant=debug threading=multi link=static runtime-link=static stage
%bjam% toolset=msvc-8.0 variant=debug threading=single link=static runtime-link=static stage
%bjam% toolset=msvc-8.0 variant=release threading=multi link=shared runtime-link=shared stage
%bjam% toolset=msvc-8.0 variant=release threading=multi link=static runtime-link=shared stage
%bjam% toolset=msvc-8.0 variant=release threading=multi link=static runtime-link=static stage
%bjam% toolset=msvc-8.0 variant=release threading=single link=static runtime-link=static stage
%bjam% toolset=msvc-9.0 variant=debug threading=multi link=shared runtime-link=shared stage
%bjam% toolset=msvc-9.0 variant=debug threading=multi link=static runtime-link=shared stage
%bjam% toolset=msvc-9.0 variant=debug threading=multi link=static runtime-link=static stage
%bjam% toolset=msvc-9.0 variant=debug threading=single link=static runtime-link=static stage
%bjam% toolset=msvc-9.0 variant=release threading=multi link=shared runtime-link=shared stage
%bjam% toolset=msvc-9.0 variant=release threading=multi link=static runtime-link=shared stage
%bjam% toolset=msvc-9.0 variant=release threading=multi link=static runtime-link=static stage
%bjam% toolset=msvc-9.0 variant=release threading=single link=static runtime-link=static stage

echo 32-Bit Log > 32bitlog.txt
%bjam% toolset=msvc-7.1 variant=debug threading=multi link=shared runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-7.1 variant=debug threading=multi link=static runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-7.1 variant=debug threading=multi link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-7.1 variant=debug threading=single link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-7.1 variant=release threading=multi link=shared runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-7.1 variant=release threading=multi link=static runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-7.1 variant=release threading=multi link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-7.1 variant=release threading=single link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 variant=debug threading=multi link=shared runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 variant=debug threading=multi link=static runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 variant=debug threading=multi link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 variant=debug threading=single link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 variant=release threading=multi link=shared runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 variant=release threading=multi link=static runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 variant=release threading=multi link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 variant=release threading=single link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 variant=debug threading=multi link=shared runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 variant=debug threading=multi link=static runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 variant=debug threading=multi link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 variant=debug threading=single link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 variant=release threading=multi link=shared runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 variant=release threading=multi link=static runtime-link=shared stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 variant=release threading=multi link=static runtime-link=static stage >> 32bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 variant=release threading=single link=static runtime-link=static stage >> 32bitlog.txt 2<&1

move stage\lib lib32

%bjam% toolset=msvc-8.0 address-model=64 variant=debug threading=multi link=shared runtime-link=shared stage
%bjam% toolset=msvc-8.0 address-model=64 variant=debug threading=multi link=static runtime-link=shared stage
%bjam% toolset=msvc-8.0 address-model=64 variant=debug threading=multi link=static runtime-link=static stage
%bjam% toolset=msvc-8.0 address-model=64 variant=debug threading=single link=static runtime-link=static stage
%bjam% toolset=msvc-8.0 address-model=64 variant=release threading=multi link=shared runtime-link=shared stage
%bjam% toolset=msvc-8.0 address-model=64 variant=release threading=multi link=static runtime-link=shared stage
%bjam% toolset=msvc-8.0 address-model=64 variant=release threading=multi link=static runtime-link=static stage
%bjam% toolset=msvc-8.0 address-model=64 variant=release threading=single link=static runtime-link=static stage
%bjam% toolset=msvc-9.0 address-model=64 variant=debug threading=multi link=shared runtime-link=shared stage
%bjam% toolset=msvc-9.0 address-model=64 variant=debug threading=multi link=static runtime-link=shared stage
%bjam% toolset=msvc-9.0 address-model=64 variant=debug threading=multi link=static runtime-link=static stage
%bjam% toolset=msvc-9.0 address-model=64 variant=debug threading=single link=static runtime-link=static stage
%bjam% toolset=msvc-9.0 address-model=64 variant=release threading=multi link=shared runtime-link=shared stage
%bjam% toolset=msvc-9.0 address-model=64 variant=release threading=multi link=static runtime-link=shared stage
%bjam% toolset=msvc-9.0 address-model=64 variant=release threading=multi link=static runtime-link=static stage
%bjam% toolset=msvc-9.0 address-model=64 variant=release threading=single link=static runtime-link=static stage

echo 64-Bit Log > 64bitlog.txt
%bjam% toolset=msvc-8.0 address-model=64 variant=debug threading=multi link=shared runtime-link=shared stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 address-model=64 variant=debug threading=multi link=static runtime-link=shared stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 address-model=64 variant=debug threading=multi link=static runtime-link=static stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 address-model=64 variant=debug threading=single link=static runtime-link=static stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 address-model=64 variant=release threading=multi link=shared runtime-link=shared stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 address-model=64 variant=release threading=multi link=static runtime-link=shared stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 address-model=64 variant=release threading=multi link=static runtime-link=static stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-8.0 address-model=64 variant=release threading=single link=static runtime-link=static stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 address-model=64 variant=debug threading=multi link=shared runtime-link=shared stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 address-model=64 variant=debug threading=multi link=static runtime-link=shared stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 address-model=64 variant=debug threading=multi link=static runtime-link=static stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 address-model=64 variant=debug threading=single link=static runtime-link=static stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 address-model=64 variant=release threading=multi link=shared runtime-link=shared stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 address-model=64 variant=release threading=multi link=static runtime-link=shared stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 address-model=64 variant=release threading=multi link=static runtime-link=static stage >> 64bitlog.txt 2<&1
%bjam% toolset=msvc-9.0 address-model=64 variant=release threading=single link=static runtime-link=static stage >> 64bitlog.txt 2<&1

move stage\lib lib64

REM create a self-extracting (-sfx), ultra compression level (-mx9) zip file for each set of binaries
%zip% a -sfx -mx9 %boost_version%-vc32-bin.exe lib32
%zip% a -sfx -mx9 %boost_version%-vc64-bin.exe lib64

start "Build Output" notepad 32bitlog.txt
start "Build Output" notepad 64bitlog.txt

cd ..

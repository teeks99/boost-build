::echo off 
sed\sed.exe -i "s/FILL_INC_PATH/C:\/local\/boost_1_45_0/g" sedTest.txt
sed\sed.exe -i "s/FILL_32_LINK_PATH/C:\/local\/boost_1_45_0\/lib32/g" sedTest.txt
sed\sed.exe -i "s/FILL_64_LINK_PATH/C:\/local\/boost_1_45_0\/lib64/g" sedTest.txt

::%comspec% /k ""C:\Program Files\Microsoft Visual Studio 8\VC\vcvarsall.bat"" x86
set vc8="%ProgramFiles%"\"Microsoft Visual Studio 8"\Common7\IDE\devenv.com
set vc9="%ProgramFiles%"\"Microsoft Visual Studio 9"\Common7\IDE\devenv.com
set vc10="%ProgramFiles%"\"Microsoft Visual Studio 10"\Common7\IDE\devenv.com

set vc8_debug_32_build=NOT_STARTED
set vc8_debug_32_run=NOT_STARTED
set vc8_release_32_build=NOT_STARTED
set vc8_release_32_run=NOT_STARTED
set vc8_debug_64_build=NOT_STARTED
set vc8_debug_64_run=NOT_STARTED
set vc8_release_64_build=NOT_STARTED
set vc8_release_64_run=NOT_STARTED

set vc9_debug_32_build=NOT_STARTED
set vc9_debug_32_run=NOT_STARTED
set vc9_release_32_build=NOT_STARTED
set vc9_release_32_run=NOT_STARTED
set vc9_debug_64_build=NOT_STARTED
set vc9_debug_64_run=NOT_STARTED
set vc9_release_64_build=NOT_STARTED
set vc9_release_64_run=NOT_STARTED

set vc10_debug_32_build=NOT_STARTED
set vc10_debug_32_run=NOT_STARTED
set vc10_release_32_build=NOT_STARTED
set vc10_release_32_run=NOT_STARTED
set vc10_debug_64_build=NOT_STARTED
set vc10_debug_64_run=NOT_STARTED
set vc10_release_64_build=NOT_STARTED
set vc10_release_64_run=NOT_STARTED

set ORIGIN_PATH=%PATH%
set ORIGIN_INCLUDE=%INCLUDE%
set ORIGIN_LIB=%LIB%
set ORIGIN_LIBPATH=%LIBPATH%
pause
:vc8-32
echo Starting VC 8 - 32

SET VSINSTALLDIR=C:\Program Files\Microsoft Visual Studio 8
SET VCINSTALLDIR=C:\Program Files\Microsoft Visual Studio 8\VC
SET FrameworkDir=C:\Windows\Microsoft.NET\Framework
SET FrameworkVersion=v2.0.50727
SET FrameworkSDKDir=C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0
set DevEnvDir=C:\Program Files\Microsoft Visual Studio 8\Common7\IDE

set PATH=C:\Program Files\Microsoft Visual Studio 8\Common7\IDE;C:\Program Files\Microsoft Visual Studio 8\VC\BIN;C:\Program Files\Microsoft Visual Studio 8\Common7\Tools;C:\Program Files\Microsoft Visual Studio 8\Common7\Tools\bin;C:\Program Files\Microsoft Visual Studio 8\VC\PlatformSDK\bin;C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\bin;C:\Windows\Microsoft.NET\Framework\v2.0.50727;C:\Program Files\Microsoft Visual Studio 8\VC\VCPackages;%ORIGIN_PATH%
set INCLUDE=C:\Program Files\Microsoft Visual Studio 8\VC\ATLMFC\INCLUDE;C:\Program Files\Microsoft Visual Studio 8\VC\INCLUDE;C:\Program Files\Microsoft Visual Studio 8\VC\PlatformSDK\include;C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\include;%ORIGIN_INCLUDE%
set LIB=C:\Program Files\Microsoft Visual Studio 8\VC\ATLMFC\LIB;C:\Program Files\Microsoft Visual Studio 8\VC\LIB;C:\Program Files\Microsoft Visual Studio 8\VC\PlatformSDK\lib;C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\lib;%ORIGIN_LIB%
set LIBPATH=C:\Windows\Microsoft.NET\Framework\v2.0.50727;C:\Program Files\Microsoft Visual Studio 8\VC\ATLMFC\LIB
pause
%vc8% BoostLibraryCheck-VC8.vcproj /build "Debug|Win32"
IF ERRORLEVEL 1 (set vc8_debug_32_build=FAIL) ELSE (set vc8_debug_32_build=PASS)
Debug\BoostLibraryCheck.exe
IF ERRORLEVEL 0 (set vc8_debug_32_run=FAIL) ELSE (set vc8_debug_32_run=PASS)
%vc8% BoostLibraryCheck-VC8.vcproj /build "Release|Win32"
IF ERRORLEVEL 0 (set vc8_release_32_build=FAIL) ELSE (set vc8_release_32_build=PASS)
Release\BoostLibraryCheck.exe
IF ERRORLEVEL 0 (set vc8_release_32_run=FAIL) ELSE (set vc8_release_32_run=PASS)
pause

goto results

:vc8-64
echo VC 8 - 64
@SET VSINSTALLDIR=C:\Program Files\Microsoft Visual Studio 8
@SET VCINSTALLDIR=C:\Program Files\Microsoft Visual Studio 8\VC
@SET FrameworkDir=C:\Windows\Microsoft.NET\Framework
@SET FrameworkVersion=v2.0.50727
@SET FrameworkSDKDir=C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0
@if "%VSINSTALLDIR%"=="" goto error_no_VSINSTALLDIR
@if "%VCINSTALLDIR%"=="" goto error_no_VCINSTALLDIR

@echo Setting environment for using Microsoft Visual Studio 2005 x64 cross tools.

@rem
@rem Root of Visual Studio IDE installed files.
@rem
@set DevEnvDir=C:\Program Files\Microsoft Visual Studio 8\Common7\IDE

@set PATH=C:\Program Files\Microsoft Visual Studio 8\Common7\IDE;C:\Program Files\Microsoft Visual Studio 8\VC\BIN\x86_amd64;C:\Program Files\Microsoft Visual Studio 8\VC\BIN;C:\Program Files\Microsoft Visual Studio 8\Common7\Tools;C:\Program Files\Microsoft Visual Studio 8\Common7\Tools\bin;C:\Program Files\Microsoft Visual Studio 8\VC\PlatformSDK\bin;C:\Windows\Microsoft.NET\Framework\v2.0.50727;C:\Program Files\Microsoft Visual Studio 8\VC\VCPackages;C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\bin;%ORIGIN_PATH%
@set INCLUDE=C:\Program Files\Microsoft Visual Studio 8\VC\ATLMFC\INCLUDE;C:\Program Files\Microsoft Visual Studio 8\VC\INCLUDE;C:\Program Files\Microsoft Visual Studio 8\VC\PlatformSDK\include;C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\include;%ORIGIN_INCLUDE%
@set LIB=C:\Program Files\Microsoft Visual Studio 8\VC\ATLMFC\LIB\amd64;C:\Program Files\Microsoft Visual Studio 8\VC\LIB\amd64;C:\Program Files\Microsoft Visual Studio 8\VC\PlatformSDK\lib\amd64;C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\LIB\AMD64;%ORIGIN_LIB%

@set LIBPATH=C:\Program Files\Microsoft Visual Studio 8\VC\ATLMFC\LIB\amd64;%ORIGIN_LIBPATH%





:results
echo Test Results
echo vc8_debug_32_build %vc8_debug_32_build%
echo vc8_debug_32_run %vc8_debug_32_run%
echo vc8_release_32_build %vc8_release_32_build%
echo vc8_release_32_run %vc8_release_32_run%
echo vc8_debug_64_build %vc8_debug_64_build%
echo vc8_debug_64_run %vc8_debug_64_run%
echo vc8_release_64_build %vc8_release_64_build%
echo vc8_release_64_run %vc8_release_64_run%

goto eof
echo vc9_debug_32_build %vc9_debug_32_build%
echo vc9_debug_32_run %vc9_debug_32_run%
echo vc9_release_32_build %vc9_release_32_build%
echo vc9_release_32_run %vc9_release_32_run%
echo vc9_debug_64_build %vc9_debug_64_build%
echo vc9_debug_64_run %vc9_debug_64_run%
echo vc9_release_64_build %vc9_release_64_build%
echo vc9_release_64_run %vc9_release_64_run%

echo vc10_debug_32_build %vc10_debug_32_build%
echo vc10_debug_32_run %vc10_debug_32_run%
echo vc10_release_32_build %vc10_release_32_build%
echo vc10_release_32_run %vc10_release_32_run%
echo vc10_debug_64_build %vc10_debug_64_build%
echo vc10_debug_64_run %vc10_debug_64_run%
echo vc10_release_64_build %vc10_release_64_build%
echo vc10_release_64_run %vc10_release_64_run%

:eof

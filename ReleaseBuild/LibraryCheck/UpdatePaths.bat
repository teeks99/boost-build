::echo off 

REM --- Enter Paths Here ---
REM The paths must use the windows format '\' backslash, and they must be escaped (a.k.a use
REM two of them in a row any time you would ordinarily use one)
set BOOST_PATH=D:\\ReleaseBuild\\boost_1_
set BOOST_LIB32_PATH=%BOOST_PATH%\\lib32
set BOOST_LIB64_PATH=%BOOST_PATH%\\lib64

REM You shouldn't need to edit below here
bin-sed\sed.exe -i "s/FILL_INC_PATH/%BOOST_PATH%/g" BoostLibraryCheck-VC8.vcproj
bin-sed\sed.exe -i "s/FILL_32_LINK_PATH/%BOOST_LIB32_PATH%-msvc-8.0/g" BoostLibraryCheck-VC8.vcproj
bin-sed\sed.exe -i "s/FILL_64_LINK_PATH/%BOOST_LIB64_PATH%-msvc-8.0/g" BoostLibraryCheck-VC8.vcproj

bin-sed\sed.exe -i "s/FILL_INC_PATH/%BOOST_PATH%/g" BoostLibraryCheck-VC9.vcproj
bin-sed\sed.exe -i "s/FILL_32_LINK_PATH/%BOOST_LIB32_PATH%-msvc-9.0/g" BoostLibraryCheck-VC9.vcproj
bin-sed\sed.exe -i "s/FILL_64_LINK_PATH/%BOOST_LIB64_PATH%-msvc-9.0/g" BoostLibraryCheck-VC9.vcproj

bin-sed\sed.exe -i "s/FILL_INC_PATH/%BOOST_PATH%/g" BoostLibraryCheck-VC10.vcxproj
bin-sed\sed.exe -i "s/FILL_32_LINK_PATH/%BOOST_LIB32_PATH%-msvc-10.0/g" BoostLibraryCheck-VC10.vcxproj
bin-sed\sed.exe -i "s/FILL_64_LINK_PATH/%BOOST_LIB64_PATH%-msvc-10.0/g" BoostLibraryCheck-VC10.vcxproj

bin-sed\sed.exe -i "s/FILL_INC_PATH/%BOOST_PATH%/g" BoostLibraryCheck-VC11.vcxproj
bin-sed\sed.exe -i "s/FILL_32_LINK_PATH/%BOOST_LIB32_PATH%-msvc-11.0/g" BoostLibraryCheck-VC11.vcxproj
bin-sed\sed.exe -i "s/FILL_64_LINK_PATH/%BOOST_LIB64_PATH%-msvc-11.0/g" BoostLibraryCheck-VC11.vcxproj

bin-sed\sed.exe -i "s/FILL_INC_PATH/%BOOST_PATH%/g" BoostLibraryCheck-VC12.vcxproj
bin-sed\sed.exe -i "s/FILL_32_LINK_PATH/%BOOST_LIB32_PATH%-msvc-12.0/g" BoostLibraryCheck-VC12.vcxproj
bin-sed\sed.exe -i "s/FILL_64_LINK_PATH/%BOOST_LIB64_PATH%-msvc-12.0/g" BoostLibraryCheck-VC12.vcxproj

bin-sed\sed.exe -i "s/FILL_INC_PATH/%BOOST_PATH%/g" BoostLibraryCheck-VC14.vcxproj
bin-sed\sed.exe -i "s/FILL_32_LINK_PATH/%BOOST_LIB32_PATH%-msvc-14.0/g" BoostLibraryCheck-VC14.vcxproj
bin-sed\sed.exe -i "s/FILL_64_LINK_PATH/%BOOST_LIB64_PATH%-msvc-14.0/g" BoostLibraryCheck-VC14.vcxproj

bin-sed\sed.exe -i "s/FILL_INC_PATH/%BOOST_PATH%/g" BoostLibraryCheck-VC14.1.vcxproj
bin-sed\sed.exe -i "s/FILL_32_LINK_PATH/%BOOST_LIB32_PATH%-msvc-14.1/g" BoostLibraryCheck-VC14.1.vcxproj
bin-sed\sed.exe -i "s/FILL_64_LINK_PATH/%BOOST_LIB64_PATH%-msvc-14.1/g" BoostLibraryCheck-VC14.1.vcxproj

REM Cleanup garbage leftover by sed
del sed*

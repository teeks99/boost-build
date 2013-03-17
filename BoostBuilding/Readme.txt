To Setup Build Environment:
1) Install python to the machine (run the python-2.6.4.msi installer for x86)
2) Update the buildRoot variable in BuildOneRelease.bat to point to the root of the build area.  (If you've installed everything to C:\BoostBuilding this isn't necessary)
3) Update the drive path in user-config.jam to point to the python interperters (If you've installed everything to C:\BoostBuilding this isn't necessary)
4) Copy user-config.jam to %USERPROFILE% (usually C:\Documents and Settings\username)
5) Download the boost source for the version you want to run from sourceforge
6) Open a command prompt and run BuildOneRelease.bat [boost-version] (i.e. C:\BoostBuilding\> BuildOneRelease.bat boost_1_41_0 )

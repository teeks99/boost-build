Building Boost on Windows
----------

Pre-requisites:
*   Have MSVC (Microsoft Visual C++, usually Visual Studio), I'm currently using msvc-8.0 (Visual Studio 2005 Team Edition for Software Developers, with SP1 and Vista compatibility), msvc-9.0 (Visual Studio 2008 Team System Development Edition, with SP1), msvc-10.0 (Visual Studio 2010 Ultimate, with SP1), and msvc-11.0 (Visual Studio 2012 Ultimate) and building on Windows Server 2008 R2. 
    For some of the older versions of VS, you can use the free Express Edition (or even the compilier that comes with the platform development kit?), but as of VS 2012 that doesn't work anymore.
*   Python (I have worked with python-2.6.4.msi and python-2.7.5.msi installers, both of which are x86), the version installed here is different from the one that will be used for building boost-python, which is in a zip file with the build scripts.
*   Inno Setup should be installed if you wish to create the installers. Set its path in the top of BuildOneRelease.bat



To Setup Build Environment:
1.  Copy the BoostBuilding directory to the place you want to build from. When I'm running on an Azure VM, I put this on the D: drive so I don't have to pay for the storage it uses (it will get big!). 
2.  Update the DEPENDENCY\_VERSIONS.txt file to include the versions of msvc that are installed on the machine.
2.  Update the buildRoot variable in BuildOneRelease.bat to point to the root of the build area.  (If you've installed everything to C:\BoostBuilding this isn't necessary)
3.  Update the drive path in user-config.jam to point to the python interperters (If you've installed everything to C:\BoostBuilding this isn't necessary)
4.  Copy user-config.jam to %USERPROFILE% (usually C:\Users\username)
5.  Download the boost source for the version you want to run from sourceforge
6.  Open a command prompt and run BuildOneRelease.bat \[boost-version\] (i.e. C:\BoostBuilding\> BuildOneRelease.bat boost_1_41_0 )

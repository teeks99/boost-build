Builds a sample application then links with boost and executes
==============

This project will check that boost libraries that were built correctly link and
execute with a very simple sample application under the various supported 
versions of visual studio.

Running

1. Modify UpdatePaths.bat so that the BOOST_PATH variable points to your install
   of boost.
2. From the command line (inside the BoostLibraryCheck directory) run UpdatePaths.bat
3. From the command line, run msbuild make.msbuild (if you don't have msbuild
   in your path, it may be at 
   C:\Windows\Microsoft.NET\Framework\v4.0.30319\msbuild.exe)
4. Verify that there were no errors
; This is a template for an installer for the Behemoth tools
; it is meant to be automatically called from a script.
;  The script should replace the following: $FILL_VERSION $FILL_CONFIG

[Setup]
AppName=Boost-Windows
AppVerName=$FILL_VERSION-$FILL_CONFIG
AppPublisher=Boost Org
DefaultDirName=C:\local\$FILL_VERSION
DefaultGroupName=none
DirExistsWarning=no
DisableStartupPrompt=yes
DisableProgramGroupPage=yes
DisableReadyMemo=yes
DisableReadyPage=yes
Compression=lzma2/ultra64
OutputDir=.
OutputBaseFilename=$FILL_VERSION-$FILL_CONFIG
Uninstallable=no
PrivilegesRequired=lowest
VersionInfoTextVersion=$FILL_VERSION
VersionInfoVersion=1.0

[Files]
Source: "$FILL_SOURCE/*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs ignoreversion

[Messages]
SelectDirLabel3=Setup will install [name] into the following folder. If you are installing multiple architectures of this version (e.g. msvc-8.0-32 and msvc-11.0-64 of boost_1_50_0) you can install them to the same directory and they will both work from there.

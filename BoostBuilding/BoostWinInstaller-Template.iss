; This is a template for an installer for the Behemoth tools
; it is meant to be automatically called from a script.
;  The script should replace the following: FILL_VERSION FILL_CONFIG

[Setup]
AppName=BoostWindows
AppVerName=FILL_VERSION-FILL_CONFIG
AppPublisher=FltSim-Behemoth
DefaultDirName=C:\local\FILL_VERSION
DefaultGroupName=none
DisableStartupPrompt=yes
DisableProgramGroupPage=yes
DisableReadyMemo=yes
DisableReadyPage=yes
Compression=lzma2/ultra64
OutputDir=.
OutputBaseFilename=FILL_VERSION-FILL_CONFIG
Uninstallable=no
PrivilegesRequired=lowest
VersionInfoTextVersion=FILL_VERSION
VersionInfoVersion=1.0

[Files]
Source: "FILL_VERSION/*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

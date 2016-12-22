; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{DA28A292-836D-4869-8A0C-580CE8BFA3B8}
AppName=Asteroid
AppVersion=1.0.0
;AppVerName=Asteroid 1.0.0
AppPublisher=JJAEWOOK
AppPublisherURL=http://www.example.com/
AppSupportURL=http://www.example.com/
AppUpdatesURL=http://www.example.com/
DefaultDirName={pf}\Asteroid
DefaultGroupName=Asteroid
OutputDir=C:\Users\Mado\Desktop
OutputBaseFilename=Asteroid_setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\2DGP\2DGP\161014\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\2DGP\2DGP\161014\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Asteroid"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Asteroid"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,Asteroid}"; Flags: nowait postinstall skipifsilent

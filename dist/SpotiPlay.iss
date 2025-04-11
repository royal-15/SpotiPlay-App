#define AppVer "1.3.0"  ; Define version at the top

[Setup]
AppName=SpotiPlay
AppVersion={#AppVer}
DefaultDirName={commonpf}\SpotiPlay
DefaultGroupName=SpotiPlay
UninstallDisplayIcon={app}\SpotiPlay.exe
OutputDir=.\installers
OutputBaseFilename=SpotiPlay v{#AppVer}
Compression=lzma2
SolidCompression=yes
ChangesEnvironment=yes
PrivilegesRequired=admin

[InstallDelete]
Type: filesandordirs; Name: "{app}\ffmpeg.exe"

[Files]
Source: "SpotiPlay.exe"; DestDir: "{app}"
Source: "ffmpeg.exe"; DestDir: "{app}"
Source: "resources\*"; DestDir: "{app}\resources"; Flags: recursesubdirs
Source: "PortablePython\*"; DestDir: "{app}\PortablePython"; Flags: recursesubdirs

[Icons]
; Desktop Shortcut
Name: "{commondesktop}\SpotiPlay"; Filename: "{app}\SpotiPlay.exe"; Tasks: desktopicon

; Start Menu Folder & Shortcut (Creates an entry in Start Menu > Programs)
Name: "{group}\SpotiPlay"; Filename: "{app}\SpotiPlay.exe"

; Uninstaller shortcut in Start Menu
Name: "{group}\Uninstall SpotiPlay"; Filename: "{uninstallexe}"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"

[Run]
Filename: "{app}\SpotiPlay.exe"; Description: "Launch SpotiPlay"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}\resources"

[Registry]
; Add application directory to PATH
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Check: NeedsAddPath(ExpandConstant('{app}'))

; Add ffmpeg.exe path for the application
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "FFMPEG_PATH"; ValueData: "{app}\ffmpeg.exe"

; Remove environment variables during uninstall
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: none; ValueName: "FFMPEG_PATH"; Flags: uninsdeletevalue

[Code]
function NeedsAddPath(Param: string): Boolean;
var
  OrigPath: string;
  ParamExpanded: string;
begin
  ParamExpanded := ExpandConstant(Param);
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path', OrigPath)
  then begin
    Result := True;
    exit;
  end;
  // Remove quotes and expand environment variables
  StringChangeEx(OrigPath, '"', '', True);
  // Convert to uppercase for case-insensitive comparison
  Result := Pos(';' + Uppercase(ParamExpanded) + ';', ';' + Uppercase(OrigPath) + ';') = 0;
end;

[Messages]
SetupWindowTitle=SpotiPlay Installer
WelcomeLabel2=This will install SpotiPlay on your computer and add ffmpeg to your system PATH.

[CustomMessages]
InstallingLabel=Installing SpotiPlay and configuring ffmpeg...

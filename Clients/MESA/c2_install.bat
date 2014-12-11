reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Construct 2_is1"
IF %ERRORLEVEL%==1 (

	echo successful install on %computername% >> "\\MESADC02\CharterTS\Construct 2\c2_install_log.txt"
)
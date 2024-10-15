call c:\nssm-2.24\nssm.exe install recommendation_system_service "%cd%\run_server.bat"
call c:\nssm-2.24\nssm.exe set recommendation_system_service AppStdout "%cd%\logs\recommendation_system_service.log"
call c:\nssm-2.24\nssm.exe set recommendation_system_service AppStderr "%cd%\logs\recommendation_system_service_error.log"
call sc start recommendation_system_service
rem call c:\nssm-2.24\nssm.exe edit recommendation_system_service
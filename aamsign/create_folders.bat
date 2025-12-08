@echo off
cd static\images

REM Create main folders
mkdir channel-letters 2>nul
mkdir neon-signs 2>nul
mkdir light-boxes 2>nul
mkdir logo-signs 2>nul
mkdir factory 2>nul
mkdir portfolio 2>nul

REM Create channel-letters subfolders
mkdir channel-letters\front-lit 2>nul
mkdir channel-letters\back-lit 2>nul
mkdir channel-letters\front-back-lit 2>nul
mkdir channel-letters\open-face 2>nul
mkdir channel-letters\non-illuminated 2>nul
mkdir channel-letters\rgb-programmable 2>nul

REM Create neon-signs subfolders
mkdir neon-signs\custom-neon 2>nul
mkdir neon-signs\neon-lamps 2>nul

REM Create light-boxes subfolders
mkdir light-boxes\slim 2>nul
mkdir light-boxes\blade 2>nul
mkdir light-boxes\fabric 2>nul

REM Create logo-signs subfolders
mkdir logo-signs\metal-acrylic 2>nul

REM Create factory subfolders
mkdir factory\production 2>nul
mkdir factory\facilities 2>nul

REM Create portfolio subfolders
mkdir portfolio\retail 2>nul
mkdir portfolio\restaurant 2>nul
mkdir portfolio\hotel 2>nul
mkdir portfolio\corporate 2>nul

REM Create general subfolders
mkdir general\hero 2>nul
mkdir general\icons 2>nul
mkdir general\misc 2>nul

echo Folder structure created successfully!
dir /ad /b

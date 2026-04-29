@ECHO OFF

REM encoding utf-8
chcp 65001

set to_find=*.ipynb

cd "C:\Users\ilyao\JupyterLab\cmd"

where /t /r C:\Users\ilyao\JupyterLab %to_find% > .\search_result.txt

REM Launch python
REM C:\\Users\\ilyao\\AppData\\Local\\Programs\\Python\\Python311\\python.exe .\py_converter.py
py .\py_converter.py

del .\search_result.txt

REM cmd /d
@ECHO OFF
echo current path - %cd%
echo INITIALIZING INSTALLER....
cd "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python39\Scripts"
echo installation path -  %cd%
start pip install Pillow
start pip install mysql-connector-python
echo DONE!
PAUSE
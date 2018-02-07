echo off
title Fetch CRM User Number File
:: See the title at the top. And this comment will not appear in the command prompt.
cd %cd%\Desktop\GitHub\CRM-UserNumber-Fetch
python main.py
start notepad "output.txt"
pause

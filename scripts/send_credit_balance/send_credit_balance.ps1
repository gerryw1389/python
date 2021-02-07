
Set-Location "c:\scripts\schedtasks\send_credit_balance"
.\venv\Scripts\activate
python main.py
# if the script had arguments
# $arg = "-f " + $currentFileName
# Start-Process -FilePath .\main.py -ArgumentList $arg -Wait

Set-Location "c:\_gwill\repo-home\h0python\schedtasks\check_mutual_funds"
.\venv\Scripts\activate
python main.py
# if the script had arguments
# $arg = "-f " + $currentFileName
# Start-Process -FilePath .\main.py -ArgumentList $arg -Wait
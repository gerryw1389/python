### Bitcoin

This script will use Alpha Vantage API to get the current price of bitcion each day.

#### To create:

1. Type the following:

   ```powershell

   cd C:\scripts\schedtasks
   mkdir check_bitcoin

   # create an active venv
   python -m venv ./venv
   .\venv\Scripts\activate

   # upgrade pip
   C:\scripts\schedtasks\check_bitcoin\venv\scripts\python.exe -m pip install --upgrade pip

   # install stuff
   pip install requests
   pip install python-dotenv

   # deactivate venv
   deactivate

   ```

2. Create a `.gitignore` with `.env`, `venv`, `__pycache`, and `logs` so that it is not tracked with git.t.

3. Develop script and test with `python main.py`

4. Once done, create `requirements.txt` by typing:

   ```powershell
   cd C:\scripts\schedtasks\check_bitcoin
   .\venv\Scripts\activate
   C:\scripts\schedtasks\check_bitcoin\venv\scripts\python.exe -m pip freeze > requirements.txt
   # deactivate venv
   deactivate
   ```

5. Next create `.bat` and `.ps1` scripts and name them exactly the same

   - Batch file:

   ```bash
   pushd "%~dp0"
   @ECHO OFF
   PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dpn0.ps1""'}"
   popd
   ```

   - Powershell file:

   ```powershell
   Set-Location "C:\scripts\schedtasks\check_bitcoin"
   .\venv\Scripts\activate
   python main.py
   ```

6. Open up powershell as administrator and type `control schedtasks` to open Windows Task Scheduler.
   - Create a task in the Task Scheduler that runs as the administrator since we need `logon as batch` rights and have it point to the batch script at whatever interval you want.

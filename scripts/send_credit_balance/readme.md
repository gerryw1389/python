### Send Credit Balance

This repo is an updated version (powershell => python) of my previous post about [Send me my credit balance](https://automationadmin.com/2018/02/ps-send-me-my-credit-balance/). This script will read messages using Gmail Rest API (no modules) from `me@gmail.com` sent from USAA automatically that tells you how much credit is available for each of your credit cards.

- In this theoretical example, I have two credit cards:
  - `buying_cc` which has a credit limit of `$5,500` which is defined around line 91 in main.py
  - `buying_cc` has a number that ends in `9999` which is defined around line 168 in helpers.py
  - We need this information because when parsing multiple emails that are similar, we need a unique value to filter on. Hopefully if you have two cards they have a different set of last four numbers.
  - `bills_cc` which has a credit limit of `$4,500` which is defined around line 93 in main.py

It parses the available credit amount and sends an email to `you@gmail.com` and a SMS message (optional) with the current budget.

Budget is defined around line 39 and the script works like this:

- Get the current day of the month
- If it is the first, there are 0 days until payday
  - Send an email with your budget which is `your defined budget - (current credit card usage + upcoming bills)`
  - On the first the upcoming bills amount is 0
- If it is not the first:
  - Send an email with your budget which is `your defined budget - (current credit card usage + upcoming bills)`
  - Bills are a list object defined around lines 115 in main.py

Pre-Requirements:

- You must login to USAA and set a daily email alert of your credit card available balances.
  - Unfortunately, this script is highly dependent on their automated email structure and will most likely break if anything changes.
- You must register an application with Gmail and ensure that you have a refresh token. See my previous post about this [here](https://automationadmin.com/2018/01/using-powershell-to-access-gmail-api/)
  - If your token expires, follow [something like this](https://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html) to get a new refresh token.
- This assumes you have python 3.6+ installed on Windows 10 client OS.

#### To create:

1. Type the following:

   ```powershell

   cd C:\scripts\schedtasks
   mkdir send_credit_balance

   # create an active venv
   python -m venv ./venv
   .\venv\Scripts\activate

   # upgrade pip
   C:\scripts\schedtasks\send_credit_balance\venv\scripts\python.exe -m pip install --upgrade pip

   # install stuff
   pip install requests
   pip install python-dotenv

   # deactivate venv
   deactivate

   ```

2. Create a `.gitignore` with `.env`, `venv`, `__pycache`, and `logs` so that it is not tracked with git.

3. Develop script and test with `python main.py`

4. Once done, create `requirements.txt` by typing:

   ```powershell
   cd C:\scripts\schedtasks\send_credit_balance
   .\venv\Scripts\activate
   C:\scripts\schedtasks\send_credit_balance\venv\scripts\python.exe -m pip freeze > requirements.txt
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
   Set-Location "C:\scripts\schedtasks\send_credit_balance"
   .\venv\Scripts\activate
   python main.py
   ```

6. Open up powershell as administrator and type `control schedtasks` to open Windows Task Scheduler.
   - Create a task in the Task Scheduler that runs as the administrator since we need `logon as batch` rights and have it point to the batch script at whatever interval you want.

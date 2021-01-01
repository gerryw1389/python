#!/usr/bin/env python3

################################################################
# Example of using python to replace my powershell function at https://automationadmin.com/2017/12/use-powershell-to-get-weather-using-wttr-in/

# Powershell to convert:
# If ($City)
# {
# Write-Log "Getting weather for $City"
# (curl http://wttr.in/$City -UserAgent "curl" ).Content
# # Cannot substitue "curl" for "Invoke-WebRequest -URI" ....
# }
# ElseIf ($JustToday)
# {
# Write-Log "Getting weather for today's current location"
# (curl http://wttr.in/?0 -UserAgent "curl" ).Content
# }
# ElseIf ($TwoDays)
# {
# Write-Log "Getting two days weather forcast for current location"
# (curl http://wttr.in/?2 -UserAgent "curl" ).Content
# }
# ElseIf ($ByZip)
# {
# Write-Log "Getting weather for zipcode $ByZip"
# (curl http://wttr.in/$ByZip -UserAgent "curl" ).Content
# }
# ElseIf ($Moon)
# {
# Write-Log "Getting today's moon phase"
# (curl http://wttr.in/moon -UserAgent "curl" ).Content
# }
# ElseIf ($MoonOnDate)
# {
# Write-Log "Getting moon phase for $MoonOnDate"
# (curl http://wttr.in/moon@$MoonOnDate -UserAgent "curl" ).Content
# }
# Else
# {
# Write-Log "Getting weather for current location"
# (curl http://wttr.in -UserAgent "curl" ).Content
# }
################################################################

import requests

url = "http://wttr.in/FortWorth.json"
payload = {}
headers = {
'Content-Type': 'application/json',
}
r = requests.request("GET", url, headers=headers, data=payload)

## why is this not showing?
# print(r)
# print(r.json)
# print(r.content)

# Lol, https://raw.githubusercontent.com/hasha2982/wttr.py/master/wttrpy/__init__.py shows this
print(r.text)

#print(dir(r))


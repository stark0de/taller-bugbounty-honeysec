import requests
import sys


headers = {"X-Original-Url":"127.0.0.1",
           "X-Forwarded-Server":"127.0.0.1",
           "X-Host":"127.0.0.1",
           "X-Forwarded-Host":"127.0.0.1",
           "X-Real-IP":"127.0.0.1",
           "X-Forwarded-For":"127.0.0.1"}
counter=0

r_first= requests.get(sys.argv[1]) #copy as Python request in Burp if you are testing an authenticated thing/POST request/API
for x, y in headers.items():
    z = {x:y}
    r = requests.get(sys.argv[1], headers=z)
    resta = len(r.text) - len(r_first.text)
    if r.status_code != r_first.status_code or resta > 50:
       print("Difference found in :" + sys.argv[1] + " with headers:")
       print(r.request.headers)
       counter+=1
if counter == 0:
   print("No relevant results")

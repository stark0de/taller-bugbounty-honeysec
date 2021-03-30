import requests
import sys

onetwosevendict={}
localhostdict={}

complete_header_list = [
    "Proxy-Host","Request-Uri","X-Forwarded","X-Forwarded-By","X-Forwarded-For",
    "X-Forwarded-For-Original","X-Forwarded-Host","X-Forwarded-Server","X-Forwarder-For",
    "X-Forward-For","Base-Url","Http-Url","Proxy-Url","Redirect","Real-Ip","Referer",
    "Referrer","Uri","Url","X-Host","X-Http-Destinationurl","X-Http-Host-Override",
    "X-Original-Remote-Addr","X-Original-Url","X-Proxy-Url","X-Rewrite-Url","X-Real-Ip","X-Remote-Addr", "X-Proxy-URL", "X-Original-Host", "X-Originally-Forwarded-For", "X-Forwarded-For-Original",
    "X-Originating-Ip","X-Ip", "X-Client-Ip"
    ]
for i in complete_header_list:
    onetwosevendict.update({i: "127.0.0.1"})
for i in complete_header_list:
    localhostdict.update({i: "localhost"})
           
counter=0

r_first= requests.get(sys.argv[1]) #copy as Python request in Burp if you are testing an authenticated thing/POST request/API
for x, y in onetwosevendict.items():
    z = {x:y}
    r = requests.get(sys.argv[1], headers=z)
    resta = len(r.text) - len(r_first.text)
    if r.status_code != r_first.status_code or resta > 50:
       print("Difference found in :" + sys.argv[1] + " with headers:")
       print(r.request.headers)
       counter+=1
if counter == 0:
   print("No relevant results for 127.0.0.1 tests")

counter=0

r_first= requests.get(sys.argv[1]) #copy as Python request in Burp if you are testing an authenticated thing/POST request/API
for x, y in localhostdict.items():
    z = {x:y}
    r = requests.get(sys.argv[1], headers=z)
    resta = len(r.text) - len(r_first.text)
    if r.status_code != r_first.status_code or resta > 50:
       print("Difference found in :" + sys.argv[1] + " with headers:")
       print(r.request.headers)
       counter+=1
if counter == 0:
   print("No relevant results for localhost tests")


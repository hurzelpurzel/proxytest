import http.client
import os

# printing environment variables
print(os.environ)

conn = http.client.HTTPSConnection("httpbin.org",443)

conn.request("GET", "/headers")

r1 = conn.getresponse()

print(r1.status, r1.reason)

data = r1.read()

print(data)



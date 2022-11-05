#/usr/bin/bash

podman run --rm -it -p 8090:8080 mitmproxy/mitmproxy

#test
#https_proxy=http://localhost:8090/ curl -k https://database.clamav.net/
https_proxy=http://localhost:8090/ curl -k https://httpbin.org/headers

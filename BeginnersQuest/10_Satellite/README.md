# Satellite
- inspecting the README.pdf reveals the satellite name:
    osmium
- the link in the console output doesn't lead to a flag..
- the binary doesn't contain any strings related to the output, so it maybe fetches data from the internet
- sniffing the network traffic of the application and filtering by the ipaddress 34.76.101.29 reveals the message in cleartext:
```
    Username: brewtoot
    password: CTF{4efcc72090af28fd33a2118985541f92e793477f}
    166.00 IS-19 2019/05/09 00:00:00
    Swath 640km	Revisit capacity twice daily, anywhere
    Resolution panchromatic: 30cm multispectral: 1.2m
    Daily acquisition capacity: 220,000km
    Remaining config data written to: https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E
```
## further investigation notes
```
satellite.ctfcompetition.com:1337
brewtoot@29.101.76.34
```
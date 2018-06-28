import urllib.request


x = open("request.xml","r")

url = "https://api.privatbank.ua/p24api/rest_fiz"

req = urllib.request.Request(url , x)

with urllib.request.urlopen(req) as response:
    the_page = response.read()
print(the_page)

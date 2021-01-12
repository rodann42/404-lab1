import requests

# does the request lib actually work
print(requests.__version__)

# get google homepage
response = requests.get("http://google.com")


gitResponse = requests.get("https://raw.githubusercontent.com/kobitoko/cmput404lab1/master/lab1.py")
print gitResponse.text

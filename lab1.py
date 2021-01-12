import requests

# does the request lib actually work
print(requests.__version__)

# get google homepage
response = requests.get("http://google.com")

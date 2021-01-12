import requests

# does the request lib actually work
print(requests.__version__)

# get google homepage
response = requests.get("http://google.com")


# get script from github
gitResponse = requests.get("https://raw.githubusercontent.com/rodann42/404-lab1/master/lab1.py")
print(gitResponse.text)

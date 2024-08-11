# Requests module
The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.
## Installation 
```bash
pip install requests
```
## Get Request
Once you have installed the Requests module, you can start using it to send HTTP requests. Here is a simple example that sends a GET request to the Google homepage:
```py
import requests
response = requests.get("https://www.google.com")
print(response.text) # Prints google's html code
```
## Post Request
Here is another example that sends a POST request to a web service and includes a custom header:
```py
import requests

url = "https://api.example.com/login"
headers = {
    "Content-Type": "application/json"
}
data = {
    "username": "myusername",
    "password": "mypassword"
}

response = requests.post(url, headers=headers, json=data)

print(response.text)
```

In this example, we send a POST request to a web service to authenticate a user. We include a custom User-Agent header and a JSON payload with the user's credentials.

## bs4 Module
There is another module called BeautifulSoup which is used for web scraping in Python.
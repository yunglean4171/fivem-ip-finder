import requests

url = input('provide cfx.re link: ')

repsonse = requests.get("https://" + url)

print(repsonse.headers["X-Citizenfx-Url"])

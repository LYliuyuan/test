import requests

res = requests.get('https://api.github.com/events')

print(res.text)
print(res.json())
# print(res.raw)

import urllib.parse
import urllib.request

url = 'http://192.168.50.1'
with urllib.request.urlopen(url) as response:
    content = response.read()

print(content)

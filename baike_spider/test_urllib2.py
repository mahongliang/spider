import urllib.request
import http.cookiejar

url = "http://www.baidu.com"
print("第一种方法url")
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print("第二种方法req")
req = urllib.request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法cookies")
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(req)
print(response3.getcode())
print(cj)
print(len(response3.read()))


from urllib.request import urlopen

url="http://www.baidu.com"
resp=urlopen(url)

with open("mybaidu.html",mode="w",encoding="utf-8")as fp:
    fp.write(resp.read().decode())
print("over!!!!")
import urllib.request
import urllib.parse


#用代理防止反爬

def main():
    url = "https://blog.csdn.net/u012195214/article/details/78889602"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    handler = urllib.request.HTTPHandler()
    opener = urllib.request.build_opener(handler)

    resp = opener.open(url)
    print(resp)

    data = resp.read().decode("utf-8")   #read读到2进制数据,decode解码,在网页上查找是哪个类型编码
    #print(data)
    with open("handler_opener01.html","w") as f:
        f.write(data)

if __name__ == "__main__":
    main()
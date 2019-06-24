import urllib.request

#   用代理防止反爬

def main():
    #  url
    url = "https://blog.csdn.net/u012195214/article/details/78889602"

    #   user agent
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    #   request
    request = urllib.request.Request(url,headers=header)


    #   proxy
    proxy = {
        "http":"http://163.204.242.234:9999"
    }

    #   build a proxy handler
    handler = urllib.request.HTTPHandler(proxy)

    # build a proxy opener
    opener = urllib.request.build_opener(handler)

    #   conn
    # read读到2进制数据,decode解码,在网页上查找是哪个类型编码
    data = opener.open(request).read().decode("utf-8")

    #print(data)
    with open("addip01.html","w") as f:
        f.write(data)

if __name__ == "__main__":
    main()
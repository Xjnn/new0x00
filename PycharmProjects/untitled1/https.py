import urllib.request
import urllib.parse
import string

#用百度搜索大数据
def main():
    url = "https://www.baidu.com/s?wd="
    url += "大数据"
    #url += "%E5%A4%A7%E6%95%B0%E6%8D%AE"
    print(url)

    #中文解析
    url = urllib.parse.quote(url,safe=string.printable)      #中文-->ascii
    print(url)

    # headers
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    # request
    request = urllib.request.Request(url, headers=header)


    resp = urllib.request.urlopen(request)   #打开url返回response
    print(resp)   #一个类

    data = resp.read().decode("utf-8")   #read读到2进制数据,decode解码,在网页上查找是哪个类型编码
    #print(data)
    with open("https02.html","w") as f:
        f.write(data)

if __name__ == "__main__":
    main()
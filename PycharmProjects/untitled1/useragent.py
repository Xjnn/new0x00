import urllib.request
import urllib.parse
import string
import random

#用百度搜索大数据
def main():
    url = "https://www.baidu.com/s?wd="
    url += "大数据"
    #url += "%E5%A4%A7%E6%95%B0%E6%8D%AE"
    print(url)

    #中文解析
    url = urllib.parse.quote(url,safe=string.printable)      #中文-->ascii
    print(url)

    user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    ]
    user_agent = random.choice(user_agents)
    print(user_agent)

    # headers
    header = {
        "User-Agent": random.choice(user_agents)
    }
    # request
    request = urllib.request.Request(url, headers=header)


    resp = urllib.request.urlopen(request)   #打开url返回response
    print(resp)   #一个类

    data = resp.read().decode("utf-8")   #read读到2进制数据,decode解码,在网页上查找是哪个类型编码
    #print(data)
    with open("useragent01.html","w") as f:
        f.write(data)

if __name__ == "__main__":
    main()
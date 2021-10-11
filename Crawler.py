import time
import requests

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# webdriver & browser(Chrome) 準備
driver = webdriver.Chrome(ChromeDriverManager().install())

# # webdriver & browser(Headless Chrome)　準備
# chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = True
# driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

# ドメインを指定
start_domain = "http://localhost:3000/"

# URLを整形
# "http://" + URL + "/"
# 整形したurlをcurrent_urlに保存
current_url = start_domain
if not current_url.startswith("http://"):
    if not current_url.startswith("https://"):
        current_url = "http://" + current_url
if not current_url.endswith("/"):
    current_url = current_url + "/"

# 整形したurl_collectorリストと未整形のraw_url_collectorリスト
url_collector = []
url_collector.append(current_url)
raw_url_collector = []
raw_url_collector.append(start_domain)

# 整形したurlをテスト、失敗の場合はプログラムを停止
r = requests.get(current_url)
if r.status_code != requests.codes.ok:
    print("URL incorrect!")
    exit()

# webdriver(Chrome)でURLを開く
driver.get(start_domain)
time.sleep(5)

# htmlソースコードを保存
html = driver.page_source
time.sleep(5)



# # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # #                                 # # # # # 
# # # # #        TESTING START            # # # # # 
# # # # #                                 # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # 

# Print rendered html source code
# # soup = BeautifulSoup(html, "html.parser")
# # soup = soup.prettify()
# # print(soup)

# Print all "button" tag
# # for item in str(html).split(">"):
# #     if "<button " in item:
# #         print(item.strip(),end=">\n")

# Print all "a" tag
# # for item in str(html).split(">"):
# #     if "<a " in item:
# #         print(item.strip(),end=">\n")

# # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # #                                 # # # # # 
# # # # #        TESTING END              # # # # # 
# # # # #                                 # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # 



# ソースコードの中の"href"属性を取り出す
# 所得したURLをテスト
# 200(success)が出たら,url_collectorリストに保存
for item in str(html).split(" "):
    if "href=" in item:
        item = item.split("\"",2)[1]
        try:
            r = requests.get(item)
        except:
            pass
        else:
            if r.status_code == requests.codes.ok:
                url_collector.append(item)
                continue
# 失敗の場合, URLを整形して試す
# max_try整形して試す回数: 2
        max_try = 2
        current_try = 0
        while current_try <= max_try:
            current_try += 1
# 整形が必要なURL:
# 0. //url
# 1. /sub-url
# 2. ./sub-url
# 3. ../sub-url
# 4. #/sub-url
# 5. sub-url
# 以上のURLを　http://url/　のパターンに整形してみる
# Fix 0~4.
            # Fix 0.
            if item.startswith("//"):
                item = "http:" + item
            # Fix 1.
            elif item.startswith("/"):
                item = current_url + item.split("/",1)[1]
            # Fix 2.
            elif item.startswith("./"):
                item = current_url + item.split("./",1)[1]
            # Fix 3.
            elif item.startswith("../"):
                item = current_url.rsplit("/",2)[0] + item.split("../",1)[1]
            # Fix 4.
            elif item.startswith("#/"):
                item = current_url + item
# 整形したURLをテスト( if r.status_code == requests.codes.ok)
# Fix 5.はexceptの中にやる
            try:
                r = requests.get(item)
            except:
                # Fix 5.
                r = requests.get(current_url + item)
                if r.status_code == requests.codes.ok:
                    item = current_url + item
                    url_collector.append(item)
                    break
            else:
                if r.status_code == requests.codes.ok:
                    url_collector.append(item)
                    break



# # 結果をプリントしてプログラムを終了
# for url in url_collector:
#     print(url,end="\n")
# driver.quit()
# exit()

